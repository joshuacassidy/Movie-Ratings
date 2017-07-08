import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

movies = pd.read_csv('Movie-Ratings-Data.csv')
movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating','BudgetMillions','Year']
movies.Genre = movies.Genre.astype('category')
distribution = [movies.AudienceRating,movies.CriticRating]
listOfMovies = list()
mylabels = list()

def showGraph():    
    plt.show()

def Hist(i):
    fullDistribution = sns.distplot(i, bins=15)
    plt.yticks(fullDistribution.get_yticks(), fullDistribution.get_yticks() * 1000)
    plt.ylabel('Distribution [%]', fontsize=16)
    plt.xlabel('Audience and Critic Rating [%]', fontsize=16)
    plt.gcf().canvas.set_window_title('Distribution of Audience and Critic Ratings')

def AudienceAndCriticRating():
    sns.set_style("white")
    [Hist(i)  for i in distribution]
    showGraph()


def FacetGrid():
    sns.set_style("dark",{"axes.facecolor":"black"})
    f, axes = plt.subplots(2,2, figsize=(12,8))
    [Kde(i,axes)  for i in range(0,2)]
    sns.violinplot(data=movies, x = 'Year', y='BudgetMillions', ax=axes[1,0],palette="YlOrRd")
    sns.kdeplot(movies.CriticRating,movies.AudienceRating,shade=True,shade_lowest=False,cmap='Blues_r',ax=axes[1,1])
    sns.kdeplot(movies.CriticRating,movies.AudienceRating,cmap='gist_gray_r', ax=axes[1,1])
    plt.gcf().canvas.set_window_title('Facet Grid')
    showGraph()

def Kde(i,axes):
    sns.kdeplot(movies.BudgetMillions , distribution[i], ax=axes[0,i],shade=True, shade_lowest=True,cmap='inferno')
    sns.kdeplot(movies.BudgetMillions , distribution[i],ax=axes[0,i],cmap='cool')


def budget(gen):
    listOfMovies.append(movies[movies.Genre == gen].BudgetMillions)
    mylabels.append(gen)

def MovieBudgetDistribution():
    sns.set_style("whitegrid",{"axes.facecolor":"white"})
    [budget(gen) for gen in movies.Genre.cat.categories]
    fig,ax = plt.subplots()
    plt.hist(listOfMovies,bins=30, stacked=True,rwidth=1, label=mylabels)
    plt.title("Movie Budget Distribution", fontsize=25,color="Gray",fontname="Impact")
    plt.legend(prop={'size':12},frameon=True,fancybox=True,shadow=True, framealpha=1)
    plt.show()

AudienceAndCriticRating()
FacetGrid()
MovieBudgetDistribution()