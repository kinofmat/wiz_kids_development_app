#%%
# import sys
# !{sys.executable} -m pip install plotly-geo

#%%
from matplotlib.pyplot import xlabel, ylabel
import pandas as pd
import numpy as np

import plotly.express as px
import statsmodels

import plotly.figure_factory as ff


# %%
data = pd.read_csv("data_v1.csv")
data

locations = pd.read_csv("locations.csv")
locations


#%%

#%%


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

    return income_df


income_df = income_data_wrangle()
income_df

#%%
new_loc = locations.rename(columns={"location_name": "restaurant"})
new_loc["restaurant"] = new_loc["restaurant"].apply(
    lambda x: "mcdonalds" if x == "McDonald's" else "subway"
)  # .reset_index()
new_loc = new_loc.merge(income_df, on=["tract", "restaurant"])
new_loc
#%%

fig = px.scatter(
    income_df,
    x="weighted_average",
    y="restaurant_count",
    opacity=0.65,
    trendline="ols",
    trendline_color_override="darkblue",
)
fig.show()
# %%

data.columns

#%%
gender_columns = ["median_age_total", "median_age_male", "median_age_female"]

race_columns = [
    "unknown_race",
    "white_alone",
    "black_or_african_american_alone",
    "american_indian_and_alaska_native_alone",
    "asian_alone",
    "native_hawaiian_and_other_pacific_islander_alone",
    "some_other_race_alone",
    "two_or_more_races",
    "two_races_including_some_other_race",
    "two_races_excluding_some_other_race_and_three_or_more_races",
]
commute_columns = [
    "commute_unkown",
    "commute_less_than_5_minutes",
    "commute_5_to_9_minutes",
    "commute_10_to_14_minutes",
    "commute_15_to_19_minutes",
    "commute_20_to_24_minutes",
    "commute_25_to_29_minutes",
    "commute_30_to_34_minutes",
    "commute_35_to_39_minutes",
    "commute_40_to_44_minutes",
    "commute_45_to_59_minutes",
    "commute_60_to_89_minutes",
    "commute_90_or_more_minutes",
]

#%%

# --- GENDER STUFF ---

df = data.rename(columns={"n_subway.2": "subway", "n_mcdonalds.2": "mcdonalds"})

g_df = df.rename(
    columns={
        "median_age_total": "both",
        "median_age_male": "male",
        "median_age_female": "female",
    }
)

gender_df = pd.melt(
    g_df,
    id_vars=["tract", "region", "subway", "mcdonalds"],
    value_vars=["both", "male", "female"],
    var_name="gender",
    value_name="median_age",
    ignore_index=False,
)

gender_df

#%%
restraunt_df = pd.melt(
    gender_df,
    id_vars=["tract", "region", "gender", "median_age"],
    value_vars=["subway", "mcdonalds"],
    var_name="restaurant",
    value_name="restaurant_count",
    ignore_index=False,
)
restraunt_df

#%%

mcdonalds_color = "#FF2D08"
subway_color = "#009743"

fig = px.histogram(
    restraunt_df,
    x="median_age",
    y="restaurant_count",
    facet_col="gender",
    color="restaurant",
    color_discrete_map={"mcdonalds": mcdonalds_color, "subway": subway_color},
)

fig.show()

# %%

# restraunt_df_f = restraunt_df[restraunt_df['restaurant_count'] > 0]

fig = px.scatter(
    restraunt_df,
    x="median_age",
    y="restaurant_count",
    facet_col="gender",
    color="restaurant",
    opacity=0.65,
    trendline="ols",
    trendline_color_override="darkblue",
)
fig.show()
# %%
income_df
# %%
locations
#%%
#%%
fig1 = px.density_mapbox(
    locations,
    lat="latitude",
    lon="longitude",
    radius=10,
    center=dict(lat=40.6592988, lon=-108.63106623175966),
    zoom=4,
    mapbox_style="carto-positron",
    hover_name="location_name",
    hover_data=["city"],
)
fig1.show()

#%%
fig2 = px.scatter_mapbox(
    locations,
    lat="latitude",
    lon="longitude",
    # radius=10,
    center=dict(lat=40.6592988, lon=-108.63106623175966),
    zoom=4,
    mapbox_style="open-street-map",
    hover_name="location_name",
    hover_data=["city"],
    color="location_name",
)
fig2.show()
#%%

# %%
new = (
    income_df.groupby(["region", "income", "restaurant"])["restaurant_count"]
    .mean()
    .reset_index()
)

fig = px.scatter(
    new,
    x="income",
    y="restaurant_count",
    # facet_col="region",
    color="restaurant",
    opacity=0.65,
    trendline="ols",
    trendline_color_override="darkblue",
)
fig.show()

#%%
income_df = income_data_wrangle()

income_df
#%%
def custom_round(x, base=5):
    return int(base * round(float(x) / base))


income_df["ks"] = income_df["weighted_average"].round(decimals=-4)
income_df["has_restaurant"] = income_df["restaurant_count"].apply(
    lambda x: 1 if x > 0 else 0
)
income_df

new = (
    income_df.groupby(["region", "ks", "restaurant"])["restaurant_count"]
    .mean()
    .reset_index()
)

#%%
fig = px.scatter(
    new,
    x="ks",
    y="restaurant_count",
    facet_col="restaurant",
    color="restaurant",
    opacity=0.65,
    trendline="ols",
    trendline_color_override="darkblue",
    labels=dict(
        ks="Median Income\n(rounded to the nearest 10k)",
        restaurant_count="% that have a Restraunt",
        restaurant="Restraunt",
    ),
)
fig.show()

#%%
income_df_business = income_df  # [income_df["restaurant_count"] > 0].reset_index()
income_df_business

fig = px.scatter(
    income_df_business,
    x="total_businesses",
    y="has_restaurant",
    facet_col="restaurant",
    color="restaurant",
    opacity=0.65,
    trendline="ols",
    trendline_color_override="darkblue",
)
fig.show()

# %%


fig = px.scatter(
    income_df,
    x="average_visitors",
    y="has_restaurant",
    facet_col="restaurant",
    color="restaurant",
    opacity=0.65,
    trendline="ols",
    hover_name="restaurant",
    hover_data=["region", "tract", "average_visitors", "has_restaurant"],
    trendline_color_override="darkblue",
)
fig.update_layout(
    hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell")
)
fig.show()

# %%
new_loc = locations.rename(columns={"location_name": "restaurant"})
new_loc["restaurant"] = new_loc["restaurant"].apply(
    lambda x: "mcdonalds" if x == "McDonald's" else "subway"
)  # .reset_index()
new_loc

#%%
new_loc.columns

#%%
new_loc = new_loc.dropna()

fig1 = px.scatter_mapbox(
    new_loc,
    lat="latitude",
    lon="longitude",
    # radius=10,
    center=dict(lat=40.6592988, lon=-108.63106623175966),
    zoom=4,
    mapbox_style="carto-positron",
    hover_name="restaurant",
    hover_data=["city"],
    size="weighted_average",
    color="restaurant",
)
fig1.show()

#%%
most_visits = (
    new_loc.sort_values("average_visitors", ascending=False)
    .head(10)["tract"]
    .unique()
    .tolist()
)
most_visits

new_loc["most_visits"] = new_loc["tract"].apply(lambda x: 1 if x in most_visits else 0)
new_loc

#%%
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
    size="average_visitors"
    # color_discrete_map={"McDonald's": mcdonalds_color, "Subway": subway_color},
)
fig.update_layout(title_text="Location Map")
fig.show()

#%%
i
