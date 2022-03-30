#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('/Users/blakekrupa/Desktop/wiz_kids_development_app/data_v1.csv')



selection = df.loc[:,['region', 'n_lsRestaurants', 'n_subway', 'n_mcdonalds']]




selection['bins'] = pd.cut(x=selection['n_lsRestaurants'], bins=[0, 5, 10, 15, 20, 25, 30, 35, 40],
                    labels=['Under 5', '6 to 10', '11 to 15',
                            '16 to 20', '21 to 25', '26 to 30', '31 to 35', '36 to 40'])




meanz = selection.groupby("bins").agg(
    subway_avg=pd.NamedAgg(column="n_subway", aggfunc="mean"),
    mcdonalds=pd.NamedAgg(column="n_mcdonalds", aggfunc="mean")).reset_index()


meanz = meanz.drop([6, 7])
meanz


# %%
#break proportions into 4th
selection = df.loc[:,['region', 'tract','new_business_proportion', 'n_lsRestaurants', 'n_subway', 'n_mcdonalds']]


selection['business_growth'] = pd.qcut(selection.new_business_proportion, q=[0,0.25,0.50,
                    0.75,1], labels=['low growth', 'med-low growth','med-high growth' ,'high growth'])





#we specifically want locations without a subway or mcdonalds
selection1 = selection[(selection['n_subway']) ==0 ]
selection1 = selection1[(selection1['n_mcdonalds']) ==0 ]


#%%
#we only want areas with high growth since thats where alot of mcdonalds and subways tend to be
growth_graph = selection1[(selection1['business_growth'] =='high growth') ]
#only get top 3 for each region and group by business proportions
growth_graph = growth_graph.sort_values(by=['n_lsRestaurants'], ascending=False).groupby('region').head(3)
growth_graph = growth_graph.sort_values(by=['region','new_business_proportion' ], ascending=False).groupby('region').head(3)
growth_graph.loc[:,['region', 'tract', 'new_business_proportion','n_lsRestaurants', 'business_growth']]
# %%
import seaborn as sns
sns.set_theme(style="whitegrid")

ax = sns.barplot(x="n_subway", y="new_business_proportion", data=selection)
ax
# %%

ax = sns.barplot(x="n_mcdonalds", y="new_business_proportion", data=selection)
ax
# %%
sns.scatterplot(x="n_mcdonalds", y="new_business_proportion", data=selection,hue = 'region')
# %%
sns.scatterplot(x="n_subway", y="new_business_proportion", data=selection, hue = 'region')
# %%
