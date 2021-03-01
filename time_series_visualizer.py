import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df=df.set_index('date')


# Clean data
df = df[(df['value']>=df['value'].quantile(0.025)) & (df['value']<=df['value'].quantile(0.975))]

def draw_line_plot():
  fig, axs = plt.subplots(1, 1)
  fig.set_figwidth(15)
  fig.set_figheight(5)
  plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  plt.xlabel('Date')
  plt.ylabel('Page Views')
  plt.plot(df.index, df['value'], color='r')




    # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.index=pd.to_datetime(df_bar.index)
    df_bar["month"]= df_bar.index.month
    df_bar["year"]= df_bar.index.year
    df_bar=df_bar.groupby(["year","month"])["value"].mean().unstack()

    

    # Draw bar plot
    axs = df_bar.plot.bar(figsize=(14,5))
    axs.set_xlabel("Years")
    axs.set_ylabel("Average Page Views")
    axs.legend(fontsize = 10, labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

    fig = axs.get_figure()


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.index = pd.to_datetime(df_box.index)
    df_box['Year'] = [d.year for d in df_box.index.date]
    df_box['Month'] = [d.strftime('%b') for d in df_box.index.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(18, 10))
    sns.boxplot(ax=axes[0], data=df_box, x='Year', y='value')
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_ylabel("Page Views")
    sns.boxplot(ax=axes[1], data=df_box, x='Month', y='value', order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig