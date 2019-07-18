import pandas as pd
%matplotlib inline

df = pd.read_excel("/home/Salohy_Mike_2018.xlsx")

df.head(10)

# Which sex participate most this year?
df['Geschlecht'].value_counts().plot.bar()

# Which route is the most chosen by all
df['Strecke'].value_counts().plot.bar()

# Which route is most chosen by women and men respectively
most_chosen_route_by_all = df.groupby(["Strecke", "Geschlecht"]).size()
print(most_chosen_route_by_all)
df.groupby(["Strecke", "Geschlecht"]).size().plot.bar(stacked=True)


# get top 3 women/men that participate for a specific route k/l and sort the performance
is_women = (df['Geschlecht'] == 'w') & (df['Strecke'] == 'k')
df[is_women].sort_values(by=['Zeit']).head(3)