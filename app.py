# --- IMPORT PACKAGES ---
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import altair as alt
import statsmodels


# --- LOAD IN DATA ---
locations = pd.read_csv("locations.csv")
data = pd.read_csv("data_v1.csv")


# --- CONSTANTS ---
mcdonalds_color = "#FF2D08"
subway_color = "#009743"


# --- DATA WRANGLING CACHE ---
@st.cache
def income_data_wrangle():
    df = data.copy()

    income_columns = [s for s in data.columns if "annual_income_" in s]

    low_income = [
        "annual_income_less_than_$10_000",
        "annual_income_$10_000_to_$14_999",
        "annual_income_$15_000_to_$19_999",
        "annual_income_$20_000_to_$24_999",
        "annual_income_$25_000_to_$29_999",
        "annual_income_$30_000_to_$34_999",
        "annual_income_$35_000_to_$39_999",
        "annual_income_$40_000_to_$44_999",
        "annual_income_$45_000_to_$49_999",
    ]

    high_income = [
        "annual_income_$50_000_to_$59_999",
        "annual_income_$60_000_to_$74_999",
        "annual_income_$75_000_to_$99_999",
        "annual_income_$100_000_to_$124_999",
        "annual_income_$125_000_to_$149_999",
        "annual_income_$150_000_to_$199_999",
        "annual_income_$200_000_or_more",
    ]

    df["low"] = df[low_income].sum(axis=1)
    df["high"] = df[high_income].sum(axis=1)
    df["income"] = df.apply(lambda x: "low" if x.low > x.high else "high", axis=1)
    df["total_income"] = df.apply(
        lambda x: (
            (x["annual_income_less_than_$10_000"] * 10000)
            + (x["annual_income_$100_000_to_$124_999"] * 112500)
            + (x["annual_income_$10_000_to_$14_999"] * 12500)
            + (x["annual_income_$125_000_to_$149_999"] * 137500)
            + (x["annual_income_$150_000_to_$199_999"] * 175000)
            + (x["annual_income_$15_000_to_$19_999"] * 17500)
            + (x["annual_income_$200_000_or_more"] * 200000)
            + (x["annual_income_$20_000_to_$24_999"] * 22500)
            + (x["annual_income_$25_000_to_$29_999"] * 27500)
            + (x["annual_income_$30_000_to_$34_999"] * 32500)
            + (x["annual_income_$35_000_to_$39_999"] * 37500)
            + (x["annual_income_$40_000_to_$44_999"] * 42500)
            + (x["annual_income_$45_000_to_$49_999"] * 47500)
            + (x["annual_income_$50_000_to_$59_999"] * 55000)
            + (x["annual_income_$60_000_to_$74_999"] * 67500)
            + (x["annual_income_$75_000_to_$99_999"] * 87500)
        ),
        axis=1,
    )

    df["total_people"] = df[income_columns].sum(axis=1)

    df["weighted_average"] = df["total_income"] / df["total_people"]

    df = df.rename(columns={"n_subway.2": "subway", "n_mcdonalds.2": "mcdonalds"})

    income_df = pd.melt(
        df,
        id_vars=[
            "tract",
            "region",
            "income",
            "weighted_average",
            "total_businesses",
            "average_visitors",
            "new_business_proportion",
        ],
        value_vars=["subway", "mcdonalds"],
        var_name="restaurant",
        value_name="restaurant_count",
        ignore_index=False,
    )

    # income_df = income_df[income_df["restaurant_count"] > 0]
    income_df["ks"] = income_df["weighted_average"].round(decimals=-4)
    income_df["has_restaurant"] = income_df["restaurant_count"].apply(
        lambda x: 1 if x > 0 else 0
    )

    return income_df


income_df = income_data_wrangle()


@st.cache
def new_loc_wrangle():
    new_loc = locations.rename(columns={"location_name": "restaurant"})
    new_loc["restaurant"] = new_loc["restaurant"].apply(
        lambda x: "mcdonalds" if x == "McDonald's" else "subway"
    )  # .reset_index()
    new_loc = new_loc.merge(income_df, on=["tract", "restaurant"]).dropna()
    most_visits = (
        new_loc.sort_values("average_visitors", ascending=False)
        .head(10)["tract"]
        .unique()
        .tolist()
    )

    new_loc["most_visits"] = new_loc["tract"].apply(
        lambda x: 1 if x in most_visits else 0
    )

    return new_loc


new_loc = new_loc_wrangle()


# --- DEFINING CONTAINERS ---
top = st.container()
demos = st.container()
income = st.container()
visitors = st.container()
analysis = st.container()


# --- ACTUAL STUFF ON PAGE ---
with top:
    st.title("Subway & McDonalds Analysis")

    st.write("Data")
    st.dataframe(data=data, width=None, height=None)

    st.write(
        "Here are all of the Subway and McDonalds locations 4 states: Utah, Colorado, Idaho, and Wyoming"
    )
    # st.map(data=locations, zoom=None, use_container_width=True)

    fig = px.scatter_mapbox(
        new_loc,
        lat="latitude",
        lon="longitude",
        # radius=10,
        center=dict(lat=43.2218, lon=-111.3939),
        zoom=3.70,
        mapbox_style="carto-positron",
        hover_name="restaurant",
        hover_data=["city"],
        color="restaurant",
        color_discrete_map={"mcdonalds": mcdonalds_color, "subway": subway_color},
    )
    fig.update_layout(title_text="Location Map")
    st.plotly_chart(fig, use_container_width=True)

    fig = px.density_mapbox(
        new_loc,
        lat="latitude",
        lon="longitude",
        radius=10,
        center=dict(lat=43.2218, lon=-111.3939),
        zoom=3.70,
        mapbox_style="carto-positron",
        hover_name="restaurant",
        hover_data=["city"],
    )
    fig.update_layout(title_text="Density Map")
    st.plotly_chart(fig, use_container_width=True)


with income:
    st.header("INCOME")
    no0_df = income_df[income_df["restaurant_count"] > 0]
    # RESTRAUNT HISTOGRAM
    fig = px.histogram(
        no0_df,
        x="weighted_average",
        y="restaurant_count",
        color="restaurant",
        # colors=colors,
        marginal="violin",  # or rug, box
        hover_data=income_df.columns,
        color_discrete_map={"mcdonalds": mcdonalds_color, "subway": subway_color},
        labels=dict(
            weighted_average="Average Income per Tract",
            restaurant_count="Restraunt Count",
            restaurant="Restraunt",
        ),
    )

    fig.update_layout(title_text="Income vs. Store Count")
    fig.update_traces(opacity=0.75)
    st.plotly_chart(fig, use_container_width=True)

    # INCOME  REGRESSION
    new = (
        income_df.groupby(["region", "ks", "restaurant"])["restaurant_count"]
        .mean()
        .reset_index()
    )
    fig = px.scatter(
        new,
        x="ks",
        y="restaurant_count",
        facet_col="restaurant",
        color="restaurant",
        opacity=0.65,
        trendline="ols",
        trendline_color_override="darkblue",
        color_discrete_map={"mcdonalds": mcdonalds_color, "subway": subway_color},
        labels=dict(
            ks="Median Income\n(rounded to the nearest 10k)",
            restaurant_count="% that have a Restraunt",
            restaurant="Restraunt",
        ),
    )
    fig.update_layout(title_text="As Income goes up, the odds it has a subway go up")
    st.plotly_chart(fig, use_container_width=True)

    # Total Businesses Regression
    fig = px.scatter(
        income_df,
        x="total_businesses",
        y="has_restaurant",
        facet_col="restaurant",
        color="restaurant",
        opacity=0.65,
        trendline="ols",
        trendline_color_override="darkblue",
        color_discrete_map={"mcdonalds": mcdonalds_color, "subway": subway_color},
        labels=dict(
            total_businesses="Num Business per Tract",
            has_restaurant="Tract Has Restaurant",
            restaurant="Restraunt",
        ),
    )
    fig.update_layout(
        title_text="As Number of Business Go Up, so do Restaurants",
        annotations=[
            dict(
                xref="paper",
                yref="paper",
                x=0.5,
                y=-0.25,
                showarrow=False,
                text="(0=No, 1=Yes)",
            )
        ],
    )

    st.plotly_chart(fig, use_container_width=True)

with visitors:
    st.header("How about Average Visitors?")
    # AVERAGE VISITORS
    fig = px.scatter(
        income_df,
        x="average_visitors",
        y="has_restaurant",
        facet_col="restaurant",
        color="restaurant",
        opacity=0.65,
        trendline="ols",
        trendline_color_override="darkblue",
        color_discrete_map={"mcdonalds": mcdonalds_color, "subway": subway_color},
        hover_name="restaurant",
        hover_data=["region", "tract", "average_visitors", "has_restaurant"],
        labels=dict(
            average_visitors="Avg Visitors per Tract",
            has_restaurant="Tract Has Restaurant",
            restaurant="Restraunt",
        ),
    )
    fig.update_layout(
        title_text="Does Average Visitor Count affect Restraunt Placement?",
        # hoverlabel=dict(bgcolor="white"),
    )
    st.plotly_chart(fig, use_container_width=True)

    # average visits map
    fig = px.scatter_mapbox(
        new_loc,
        lat="latitude",
        lon="longitude",
        # radius=10,
        center=dict(lat=43.2218, lon=-111.3939),
        zoom=3.70,
        mapbox_style="carto-positron",
        hover_name="restaurant",
        hover_data=["city"],
        color="average_visitors",
        size="average_visitors",
    )

    fig.update_layout(title_text="Average Visitors Map")
    st.plotly_chart(fig, use_container_width=True)


with analysis:
    st.header("Something for Interesting graphs")

    chart = (
        alt.Chart(data)
        .encode(
            alt.X("n_lsRestaurants", axis=alt.Axis(title="Restaurant Count")),
            alt.Y("total_population_estimate", axis=alt.Axis(title="Pop")),
            color=alt.Color("region", title="State"),
        )
        .mark_circle()
        .configure_axis(labelFontSize=18, titleFontSize=18)
        .configure_title(fontSize=20)
        .configure_legend(titleFontSize=18, labelFontSize=18)
    )
    st.altair_chart(chart)
    st.write("Chart Explanation")

    chart = (
        alt.Chart(data)
        .encode(
            alt.X("n_lsRestaurants", axis=alt.Axis(title="Restaurant Count")),
            alt.Y("median_age_total", axis=alt.Axis(title="Age")),
            color=alt.Color("region", title="State"),
        )
        .mark_circle()
        .configure_axis(labelFontSize=18, titleFontSize=18)
        .configure_title(fontSize=20)
        .configure_legend(titleFontSize=18, labelFontSize=18)
    )
    st.altair_chart(chart)
    st.write("Chart Explanation")

    chart = (
        alt.Chart(data)
        .encode(
            alt.X("n_lsRestaurants", axis=alt.Axis(title="Restaurant Count")),
            alt.Y("count_bigger_places_by_tract", axis=alt.Axis(title="Big Places")),
            color=alt.Color("region", title="State"),
        )
        .mark_circle()
        .configure_axis(labelFontSize=18, titleFontSize=18)
        .configure_title(fontSize=20)
        .configure_legend(titleFontSize=18, labelFontSize=18)
    )
    st.altair_chart(chart)
    st.write("Chart Explanation")

    chart = (
        alt.Chart(data)
        .encode(
            alt.X("n_lsRestaurants", axis=alt.Axis(title="Restaurant Count")),
            alt.Y("commute_less_than_5_minutes", axis=alt.Axis(title="5 min Commute")),
            color=alt.Color("region", title="State"),
        )
        .mark_circle()
        .configure_axis(labelFontSize=18, titleFontSize=18)
        .configure_title(fontSize=20)
        .configure_legend(titleFontSize=18, labelFontSize=18)
    )
    st.altair_chart(chart)
    st.write("Chart Explanation")

    chart = (
        alt.Chart(data)
        .encode(
            alt.X("n_lsRestaurants", axis=alt.Axis(title="Restaurant Count")),
            alt.Y("commute_10_to_14_minutes", axis=alt.Axis(title="10-14 min Commute")),
            color=alt.Color("region", title="State"),
        )
        .mark_circle()
        .configure_axis(labelFontSize=18, titleFontSize=18)
        .configure_title(fontSize=20)
        .configure_legend(titleFontSize=18, labelFontSize=18)
    )
    st.altair_chart(chart)
    st.write("Chart Explanation")

    chart = (
        alt.Chart(data)
        .encode(
            alt.X("n_lsRestaurants", axis=alt.Axis(title="Restaurant Count")),
            alt.Y("commute_30_to_34_minutes", axis=alt.Axis(title="30-34 min Commute")),
            color=alt.Color("region", title="State"),
        )
        .mark_circle()
        .configure_axis(labelFontSize=18, titleFontSize=18)
        .configure_title(fontSize=20)
        .configure_legend(titleFontSize=18, labelFontSize=18)
    )
    st.altair_chart(chart)
    st.write("Chart Explanation")

    chart = (
        alt.Chart(data)
        .encode(
            alt.X("n_lsRestaurants", axis=alt.Axis(title="Restaurant Count")),
            alt.Y("count_new_bus_past_year", axis=alt.Axis(title="New Bussinesses")),
            color=alt.Color("region", title="State"),
        )
        .mark_circle()
        .configure_axis(labelFontSize=18, titleFontSize=18)
        .configure_title(fontSize=20)
        .configure_legend(titleFontSize=18, labelFontSize=18)
    )
    st.altair_chart(chart)
    st.write("Chart Explanation")


# %%
