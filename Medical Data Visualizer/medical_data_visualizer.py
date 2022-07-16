import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = [1 if result > 25 else 0 for result in df['overweight']]

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol'
# or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = [0 if value <= 1 else 1 for value in df['cholesterol']]
df['gluc'] = [0 if value <= 1 else 1 for value in df['gluc']]

# Draw Categorical Plot
def draw_cat_plot():

    # Create DataFrame for cat plot using `pd.melt` using just the values from
    # 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'],
                     value_vars=sorted(['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']))

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature.
    # You will have to rename one of the columns for the catplot to work correctly.

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(data=df_cat, kind='count', x='variable',
                      hue='value', col='cardio').set(ylabel='total').fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():

    # Clean the data - it has to be at same time and to divided.
    df_heat = df.loc[df[(df['ap_lo'] <= df['ap_hi'])
                        & (df['height'] >= df['height'].quantile(.025))
                        & (df['height'] <= df['height'].quantile(.975))
                        & (df['weight'] >= df['weight'].quantile(.025))
                        & (df['weight'] <= df['weight'].quantile(.975))].index]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr))

    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, mask=mask, fmt='.1f')
    # Use the fmt='.1f' to round the numbers.

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
