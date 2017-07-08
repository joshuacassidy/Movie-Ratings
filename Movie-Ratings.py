import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

movies = pd.read_csv('Movie-Ratings-Data.csv')
movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating','BudgetMillions','Year']

movies.Film = movies.Film.astype('category')
movies.Genre = movies.Genre.astype('category')
movies.Year = movies.Year.astype('category')

distribution = [movies.AudienceRating,movies.CriticRating]
sns.set_style("white")

def showGraph():    
    plt.show()

def Hist(i):
    fullDistribution = sns.distplot(i, bins=15)
    plt.yticks(fullDistribution.get_yticks(), fullDistribution.get_yticks() * 1000)
    plt.ylabel('Distribution [%]', fontsize=16)
    plt.xlabel('Audience and Critic Rating [%]', fontsize=16)
    plt.gcf().canvas.set_window_title('Distribution of Audience and Critic Ratings')

def AudienceAndCriticRating():
    [Hist(i)  for i in distribution]
    showGraph()

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

AudienceAndCriticRating()