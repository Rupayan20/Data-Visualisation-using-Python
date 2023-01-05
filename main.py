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

# For nominal-type data, one common operation is to sort the data in terms of frequency. With our data in a pandas DataFrame, we can use various DataFrame methods to compute and extract an ordering, then set that ordering on the "order" parameter:
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
