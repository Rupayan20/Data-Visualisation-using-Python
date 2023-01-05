# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
%matplotlib inline

# access the csv file (we have to download this file, link: https://docs.google.com/spreadsheets/d/1BQCIwjAaot-Stb93LaHFBB_g0pgDb5p2v115JB2K6Bs/edit?usp=sharing)
pokemon = pd.read_csv('/content/Copy of pokemon - pokemon.csv')
print(pokemon.shape)
pokemon.head()


# Bar Chart:
sb.countplot(data = pokemon, x = 'generation_id');

  # plotting all bars in the same color, here I choose color of 3rd gen whoose indexing is 2
base_color = sb.color_palette()[2]

  # for nominal-type data, one common operation is to sort the data in terms of frequency. With our data in a pandas DataFrame, we can use various DataFrame methods to compute and extract an ordering, then set that ordering on the "order" parameter:
sb.countplot(data = pokemon, x = 'generation_id', color = base_color)
base_color = sb.color_palette()[2]
gen_order = pokemon['generation_id'].value_counts().index
sb.countplot(data = pokemon, x = 'generation_id', color = base_color, order = gen_order)

  # we have a lot of category levels, or the category names are long, then we might end up with overcrowding of the tick labels. So, one way to deal with it is that, you can use matplotlib's xticks function and its "rotation" parameter to change the orientation in which the labels will be depicted.
base_color = sb.color_palette()[2]
sb.countplot(data = pokemon, x = 'type_1', color = base_color)
plt.xticks(rotation=90);

  # we can set the variable to be plotted on the parameter "y":
base_color = sb.color_palette()[2]
sb.countplot(data = pokemon, y = 'type_1', color = base_color)

  # Count Missing Data:
    # one interesting way we can apply bar charts is through the visualization of missing data. We can use pandas functions to create a table with the number of missing values in each column.
pokemon.isna().sum()

    # we could treat the variable names as levels of a categorical variable, and create a resulting bar plot.
na_counts = pokemon.isna().sum()
base_color = sb.color_palette()[2]
sb.barplot(na_counts.index.values, na_counts, color = base_color)
plt.xticks(rotation=90);


# Pie Charts
  # code for the pie chart seen above
sorted_counts = df['generation_id'].value_counts()
plt.pie(sorted_counts, labels = sorted_counts.index, startangle = 90,
        counterclock = False);
plt.axis('square');

  # Additional Variation:
    # To create a donut plot, we can add a "wedgeprops" argument to the pie function call. By default, the radius of the pie (circle) is 1; setting the wedges' width property to less than 1 removes coloring from the center of the circle.
sorted_counts = df['generation_id'].value_counts()
plt.pie(sorted_counts, labels = sorted_counts.index, startangle = 90,
        counterclock = False, wedgeprops = {'width' : 0.4});
plt.axis('square');


# Histograms:
  # a histogram is used to plot the distribution of a numeric variable. It's the quantitative version of the bar chart.
plt.hist(data = df, x = 'speed')

  # the hist function divides the data into 20 bins, based on the range of values taken.
plt.hist(data = df, x = 'speed', bins = 20)

  # the first argument to arange is the leftmost bin edge, the second argument the upper limit, and the third argument the bin width. Note that even though I've specified the "max" value in the second argument, I've added a "+1" (the bin width). That is because arange will only return values that are strictly less than the upper limit. Adding in "+1" is a safety measure to ensure that the rightmost bin edge is at least the maximum data value, so that all of the data points are plotted. The leftmost bin is set as a hardcoded value to get a nice, interpretable value, though you could use functions like numpy's around if you wanted to approach that end programmatically.
bins = np.arange(0, df['speed'].max()+1, 5)
plt.hist(data = df, x = 'speed', bins = bins)

  # this example puts two plots side by side through use of the subplot function, whose arguments specify the number of rows, columns, and index of the active subplot (in that order). The figure() function is called with the "figsize" parameter so that we can have a larger figure to support having multiple subplots
plt.figure(figsize = [10, 5]) # larger figure size for subplots

    # histogram on left, example of too-large bin size
plt.subplot(1, 2, 1) # 1 row, 2 cols, subplot 1
bin_edges = np.arange(0, df['speed'].max()+1, +5)
plt.hist(data = df, x = 'speed', bins = bin_edges);

    # histogram on right, example of too-small bin size
plt.subplot(1, 2, 2) # 1 row, 2 cols, subplot 2
bin_edges = np.arange(0, df['speed'].max()++1, 1)
plt.hist(data = df, x = 'speed', bins = bin_edges);

# Alternative Approach
  # when we specify the data to be plotted, note that the first argument must be the Series or array with the points to be plotted. This is in contrast to our ability to specify a data source and column as separate arguments, like we've seen with and countplot and hist.
  sb.distplot(df['speed']);
  
  # the distplot function has built-in rules for specifying histogram bins, and by default plots a curve depicting the kernel density estimate (KDE) on top of the data. The vertical axis is based on the KDE, rather than the histogram: you shouldn't expect the total heights of the bars to equal 1, but the area under the curve should equal 1.
 sb.distplot(df['speed'], kde=False);
 
  # despite the fact that the default bin-selection formula used by distplot might be better than the choice of ten bins that .hist uses, you'll still want to do some tweaking to align the bins to 'round' values. You can use other parameter settings to plot just the histogram and specify the bins like before:
bin_edges = np.arange(0, df['speed'].max()+1, 5)
sb.distplot(df['speed'], bins = bin_edges, kde = False,
            hist_kws = {'alpha' : 1});
