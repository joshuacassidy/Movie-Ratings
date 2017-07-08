import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

movies = pd.read_csv('Movie-Ratings-Data.csv')
movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating','BudgetMillions','Year']

movies.Film = movies.Film.astype('category')
movies.Genre = movies.Genre.astype('category')
movies.Year = movies.Year.astype('category')

audienceDistribution = sns.distplot(movies.AudienceRating, bins=15)
criticDistribution = sns.distplot(movies.CriticRating, bins=15)
plt.show()

f, axes = plt.subplots(2,2, figsize=(12,8))
#plot [0,0]

kdeAudienceBudget = sns.kdeplot(movies.BudgetMillions , movies.AudienceRating, ax=axes[0,0])

#plot [0,1]
kdeCriticBudget = sns.kdeplot(movies.BudgetMillions , movies.CriticRating, ax=axes[0,1])

#plot [1,0]
violinYearBudget = sns.violinplot(data=movies, x = 'Year', y='BudgetMillions', ax=axes[1,0])

#plot [1,1]
kdeCriticAudience = sns.kdeplot(movies.CriticRating,movies.AudienceRating,ax=axes[1,1])

plt.show()

list1 = list()
mylabels = list()
for gen in movies.Genre.cat.categories:
    list1.append(movies[movies.Genre == gen].BudgetMillions)
    
fig,ax = plt.subplots()
h = plt.hist(list1,bins=30, stacked=True,rwidth=1, label=mylabels)
plt.legend(prop={'size':12})
plt.show()