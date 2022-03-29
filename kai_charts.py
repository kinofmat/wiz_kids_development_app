# %%
import pandas as pd
import numpy as np

import altair as alt

# %%
pd.set_option('display.max_columns', None)
df = pd.read_csv("data_v1.csv")
df

# %%
chart = (
    alt.Chart(df)
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
chart

# %%
chart = (
    alt.Chart(df)
    .encode(
        alt.X("n_subway", axis=alt.Axis(title="Subway Count")),
        alt.Y("total_population_estimate", axis=alt.Axis(title="Pop")),
        color=alt.Color("region", title="State"),
    )
    .mark_circle()
    .configure_axis(labelFontSize=18, titleFontSize=18)
    .configure_title(fontSize=20)
    .configure_legend(titleFontSize=18, labelFontSize=18)
)
chart

# %%
chart = (
    alt.Chart(df)
    .encode(
        alt.X("n_mcdonalds", axis=alt.Axis(title="McDonalds Count")),
        alt.Y("total_population_estimate", axis=alt.Axis(title="Pop")),
        color=alt.Color("region", title="State"),
    )
    .mark_circle()
    .configure_axis(labelFontSize=18, titleFontSize=18)
    .configure_title(fontSize=20)
    .configure_legend(titleFontSize=18, labelFontSize=18)
)
chart




# %%
chart = (
    alt.Chart(df)
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
chart

# %%
chart = (
    alt.Chart(df)
    .encode(
        alt.X("n_subway", axis=alt.Axis(title="Subway Count")),
        alt.Y("median_age_total", axis=alt.Axis(title="Age")),
        color=alt.Color("region", title="State"),
    )
    .mark_circle()
    .configure_axis(labelFontSize=18, titleFontSize=18)
    .configure_title(fontSize=20)
    .configure_legend(titleFontSize=18, labelFontSize=18)
)
chart

# %%
chart = (
    alt.Chart(df)
    .encode(
        alt.X("n_mcdonalds", axis=alt.Axis(title="McDonalds Count")),
        alt.Y("median_age_total", axis=alt.Axis(title="Age")),
        color=alt.Color("region", title="State"),
    )
    .mark_circle()
    .configure_axis(labelFontSize=18, titleFontSize=18)
    .configure_title(fontSize=20)
    .configure_legend(titleFontSize=18, labelFontSize=18)
)
chart




# %%
chart = (
    alt.Chart(df)
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
chart

# %%
chart = (
    alt.Chart(df)
    .encode(
        alt.X("n_subway", axis=alt.Axis(title="Subway Count")),
        alt.Y("count_bigger_places_by_tract", axis=alt.Axis(title="Big Places")),
        color=alt.Color("region", title="State"),
    )
    .mark_circle()
    .configure_axis(labelFontSize=18, titleFontSize=18)
    .configure_title(fontSize=20)
    .configure_legend(titleFontSize=18, labelFontSize=18)
)
chart

# %%
chart = (
    alt.Chart(df)
    .encode(
        alt.X("n_mcdonalds", axis=alt.Axis(title="McDonald Count")),
        alt.Y("count_bigger_places_by_tract", axis=alt.Axis(title="Big Places")),
        color=alt.Color("region", title="State"),
    )
    .mark_circle()
    .configure_axis(labelFontSize=18, titleFontSize=18)
    .configure_title(fontSize=20)
    .configure_legend(titleFontSize=18, labelFontSize=18)
)
chart




# %%
chart = (
    alt.Chart(df)
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
chart

# %%
chart = (
    alt.Chart(df)
    .encode(
        alt.X("n_subway", axis=alt.Axis(title="Subway Count")),
        alt.Y("commute_less_than_5_minutes", axis=alt.Axis(title="5 min Commute")),
        color=alt.Color("region", title="State"),
    )
    .mark_circle()
    .configure_axis(labelFontSize=18, titleFontSize=18)
    .configure_title(fontSize=20)
    .configure_legend(titleFontSize=18, labelFontSize=18)
)
chart

# %%
chart = (
    alt.Chart(df)
    .encode(
        alt.X("n_mcdonalds", axis=alt.Axis(title="McDonald Count")),
        alt.Y("commute_less_than_5_minutes", axis=alt.Axis(title="5 min Commute")),
        color=alt.Color("region", title="State"),
    )
    .mark_circle()
    .configure_axis(labelFontSize=18, titleFontSize=18)
    .configure_title(fontSize=20)
    .configure_legend(titleFontSize=18, labelFontSize=18)
)
chart




# %%
chart = (
    alt.Chart(df)
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
chart

# %%
chart = (
    alt.Chart(df)
    .encode(
        alt.X("n_subway", axis=alt.Axis(title="Subway Count")),
        alt.Y("commute_10_to_14_minutes", axis=alt.Axis(title="10-14 min Commute")),
        color=alt.Color("region", title="State"),
    )
    .mark_circle()
    .configure_axis(labelFontSize=18, titleFontSize=18)
    .configure_title(fontSize=20)
    .configure_legend(titleFontSize=18, labelFontSize=18)
)
chart

# %%
chart = (
    alt.Chart(df)
    .encode(
        alt.X("n_mcdonalds", axis=alt.Axis(title="McDonald Count")),
        alt.Y("commute_10_to_14_minutes", axis=alt.Axis(title="10-14 min Commute")),
        color=alt.Color("region", title="State"),
    )
    .mark_circle()
    .configure_axis(labelFontSize=18, titleFontSize=18)
    .configure_title(fontSize=20)
    .configure_legend(titleFontSize=18, labelFontSize=18)
)
chart




# %%
chart = (
    alt.Chart(df)
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
chart

# %%
chart = (
    alt.Chart(df)
    .encode(
        alt.X("n_subway", axis=alt.Axis(title="Subway Count")),
        alt.Y("commute_30_to_34_minutes", axis=alt.Axis(title="30-34 min Commute")),
        color=alt.Color("region", title="State"),
    )
    .mark_circle()
    .configure_axis(labelFontSize=18, titleFontSize=18)
    .configure_title(fontSize=20)
    .configure_legend(titleFontSize=18, labelFontSize=18)
)
chart

# %%
chart = (
    alt.Chart(df)
    .encode(
        alt.X("n_mcdonalds", axis=alt.Axis(title="McDonald Count")),
        alt.Y("commute_30_to_34_minutes", axis=alt.Axis(title="30-34 min Commute")),
        color=alt.Color("region", title="State"),
    )
    .mark_circle()
    .configure_axis(labelFontSize=18, titleFontSize=18)
    .configure_title(fontSize=20)
    .configure_legend(titleFontSize=18, labelFontSize=18)
)
chart




# %%
chart = (
    alt.Chart(df)
    .encode(
        alt.X("n_lsRestaurants", axis=alt.Axis(title="Restaurant Count")),
        alt.Y("annual_income_$45_000_to_$49_999", axis=alt.Axis(title="45-49k Income")),
        color=alt.Color("region", title="State"),
    )
    .mark_circle()
    .configure_axis(labelFontSize=18, titleFontSize=18)
    .configure_title(fontSize=20)
    .configure_legend(titleFontSize=18, labelFontSize=18)
)
chart

# %%
chart = (
    alt.Chart(df)
    .encode(
        alt.X("n_subway", axis=alt.Axis(title="Subway Count")),
        alt.Y("annual_income_$45_000_to_$49_999", axis=alt.Axis(title="45-49k Income")),
        color=alt.Color("region", title="State"),
    )
    .mark_circle()
    .configure_axis(labelFontSize=18, titleFontSize=18)
    .configure_title(fontSize=20)
    .configure_legend(titleFontSize=18, labelFontSize=18)
)
chart

# %%
chart = (
    alt.Chart(df)
    .encode(
        alt.X("n_mcdonalds", axis=alt.Axis(title="McDonald Count")),
        alt.Y("annual_income_$45_000_to_$49_999", axis=alt.Axis(title="45-49k Income")),
        color=alt.Color("region", title="State"),
    )
    .mark_circle()
    .configure_axis(labelFontSize=18, titleFontSize=18)
    .configure_title(fontSize=20)
    .configure_legend(titleFontSize=18, labelFontSize=18)
)
chart




# %%
chart = (
    alt.Chart(df)
    .encode(
        alt.X("n_lsRestaurants", axis=alt.Axis(title="Restaurant Count")),
        alt.Y("count_new_bus_past_year", axis=alt.Axis(title="New Bus")),
        color=alt.Color("region", title="State"),
    )
    .mark_circle()
    .configure_axis(labelFontSize=18, titleFontSize=18)
    .configure_title(fontSize=20)
    .configure_legend(titleFontSize=18, labelFontSize=18)
)
chart

# %%
chart = (
    alt.Chart(df)
    .encode(
        alt.X("n_subway", axis=alt.Axis(title="Subway Count")),
        alt.Y("count_new_bus_past_year", axis=alt.Axis(title="New Bus")),
        color=alt.Color("region", title="State"),
    )
    .mark_circle()
    .configure_axis(labelFontSize=18, titleFontSize=18)
    .configure_title(fontSize=20)
    .configure_legend(titleFontSize=18, labelFontSize=18)
)
chart

# %%
chart = (
    alt.Chart(df)
    .encode(
        alt.X("n_mcdonalds", axis=alt.Axis(title="McDonald Count")),
        alt.Y("count_new_bus_past_year", axis=alt.Axis(title="New Bus")),
        color=alt.Color("region", title="State"),
    )
    .mark_circle()
    .configure_axis(labelFontSize=18, titleFontSize=18)
    .configure_title(fontSize=20)
    .configure_legend(titleFontSize=18, labelFontSize=18)
)
chart

# %%
