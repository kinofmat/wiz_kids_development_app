import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


locations = pd.read_csv("locations.csv")
data = pd.read_csv("data_v1.csv")


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
        id_vars=["tract", "region", "income", "weighted_average"],
        value_vars=["subway", "mcdonalds"],
        var_name="restaurant",
        value_name="restaurant_count",
        ignore_index=False,
    )

    return income_df


top = st.container()
income = st.container()

with top:
    st.title("Subway & McDonalds Analysis")

    st.write("Data")
    st.dataframe(data=data, width=None, height=None)

    st.write(
        "Here are all of the Subway and McDonalds locations 4 states: Utah, Colorado, Idaho, and Wyoming"
    )
    st.map(data=locations, zoom=None, use_container_width=True)


with income:
    income_df = income_data_wrangle()

    fig = px.histogram(
        income_df,
        x="weighted_average",
        y="restaurant_count",
        color="restaurant",
        # colors=colors,
        marginal="violin",  # or rug, box
        hover_data=income_df.columns,
        color_discrete_map={"mcdonalds": "#FF2D08", "subway": "#009743"},
        labels=dict(
            weighted_average="Average Income per Tract",
            restaurant_count="Restraunt Count",
            restaurant="Restraunt",
        ),
    )

    fig.update_layout(title_text="Income vs. Store Count")
    fig.update_traces(opacity=0.75)
    st.plotly_chart(fig, use_container_width=True)
