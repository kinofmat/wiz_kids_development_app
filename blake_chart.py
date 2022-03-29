#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('/Users/blakekrupa/Desktop/wiz_kids_development_app/data_v1.csv')



selection = df.loc[:,['region', 'n_lsRestaurants', 'n_subway', 'n_mcdonalds']]




selection['sbins'] = pd.cut(x=selection['n_lsRestaurants'], bins=[0, 5, 10, 15, 20, 25, 30, 35, 40],
                    labels=['Under 5', '6 to 10', '11 to 15',
                            '16 to 20', '21 to 25', '26 to 30', '31 to 35', '36 to 40'])


selection1 = selection[(selection['n_lsRestaurants'] <35 ) ]
selection1


meanz = selection1.groupby("bins").agg(
    subway_avg=pd.NamedAgg(column="n_subway", aggfunc="mean"),
    mcdonlads_avg=pd.NamedAgg(column="n_mcdonalds", aggfunc="mean")).reset_index()


meanz = meanz.drop([6, 7])
meanz


# %%
selection = df.loc[:,['new_business_proportion', 'n_lsRestaurants', 'n_subway', 'n_mcdonalds']]
selection
# %%
import seaborn as sns
sns.set_theme(style="whitegrid")

ax = sns.barplot(x="n_subway", y="new_business_proportion", data=selection)
ax
# %%

ax = sns.barplot(x="n_mcdonalds", y="new_business_proportion", data=selection)
ax
# %%
selection = df.loc[:,['annual_income_less_than_$10_000','annual_income_$10_000_to_$14_999','annual_income_$15_000_to_$19_999','annual_income_$20_000_to_$24_999','annual_income_$25_000_to_$29_999','annual_income_$30_000_to_$34_999','annual_income_$35_000_to_$39_999','annual_income_$40_000_to_$44_999','annual_income_$45_000_to_$49_999','annual_income_$50_000_to_$59_999','annual_income_$60_000_to_$74_999','annual_income_$75_000_to_$99_999','annual_income_$100_000_to_$124_999','annual_income_$125_000_to_$149_999','annual_income_$150_000_to_$199_999','annual_income_$200_000_or_more' 'n_subway', 'n_mcdonalds']]
selection
# %%
