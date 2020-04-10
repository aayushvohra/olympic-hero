# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)
data.rename(columns={"Total":"Total_Medals"},inplace=True)
data.head(10)





# --------------
data[['Total_Summer', 'Total_Winter']]



data["Better_Event"]=np.where(data["Total_Summer"]>data["Total_Winter"],"Summer",(np.where(data["Total_Summer"]<data["Total_Winter"],"Winter","Both")))
print(data)
better_event = data["Better_Event"].value_counts().idxmax()
print(better_event)



# --------------
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries = top_countries[0:-1]
def top_ten(top_countries,column):
    country_list = []
    top10 = top_countries.nlargest(10, column)
    country_list = list(top10["Country_Name"])
    return country_list
top_10_summer = top_ten(top_countries,"Total_Summer")
print(top_10_summer)
top_10_winter = top_ten(top_countries,"Total_Winter")
print(top_10_winter)
top_10 = top_ten(top_countries,column="Total_Medals")
print(top_10)
common = list(set(top_10_summer).intersection(top_10_winter,top_10))
print(common)


# --------------
summer_df = data[data["Country_Name"].isin(top_10_summer)]
winter_df = data[data["Country_Name"].isin(top_10_winter)]
top_df = data[data["Country_Name"].isin(top_10)]
#summer_df["Country_Name"].(["Total_Summer"]).plot(kind="bar")
plt.bar(summer_df["Country_Name"], summer_df["Total_Summer"], color="blue")
plt.bar(winter_df["Country_Name"], winter_df["Total_Summer"], color="green")
plt.bar(top_df["Country_Name"], top_df["Total_Summer"], color="red")


# --------------
summer_df["Golden_Ratio"]=summer_df["Gold_Summer"]/summer_df["Total_Summer"]
summer_max_ratio = max(summer_df["Golden_Ratio"])
summer_country_gold = summer_df.loc[summer_df["Golden_Ratio"].idxmax(),"Country_Name"]
print(summer_country_gold)

winter_df["Golden_Ratio"]=winter_df["Gold_Winter"]/winter_df["Total_Winter"]
winter_max_ratio = max(winter_df["Golden_Ratio"])
winter_country_gold = winter_df.loc[winter_df["Golden_Ratio"].idxmax(),"Country_Name"]
print(winter_country_gold)

top_df["Golden_Ratio"]=top_df["Gold_Total"]/top_df["Total_Medals"]
top_max_ratio = max(top_df["Golden_Ratio"])
top_country_gold = top_df.loc[top_df["Golden_Ratio"].idxmax(),"Country_Name"]
print(top_country_gold)


# --------------
#Code starts here
data_1 = data[0:-1]
data_1["Total_Points"]=(data_1["Gold_Total"]*3)+(data_1["Silver_Total"]*2)+(data_1["Bronze_Total"]*1)
most_points = data_1["Total_Points"].max()
print(most_points)
best_country = data_1.loc[data_1["Total_Points"].idxmax(),"Country_Name"]
print(best_country)


# --------------
#Code starts here
best = data[data["Country_Name"]==best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
print(best)
best.groupby(['Gold_Total','Silver_Total','Bronze_Total']).size().unstack()
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.show()


