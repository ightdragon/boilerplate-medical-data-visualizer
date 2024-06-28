import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')
#print(df.columns)
# 2

df['overweight'] = np.where(((df['weight'] / ((df['height'] * 0.01) ** 2)) > 25), 1, 0)

# 3

df['cholesterol'] = np.where(df['cholesterol'] == 1, 0 , 1)
df['gluc'] = np.where(df.gluc == 1, 0, 1)

#print(df.gluc)


# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars='cardio', value_vars = ['cholesterol','gluc','smoke','alco','active','overweight'])
    
    #print(df_cat)

    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    #print(df_cat)

    # 7
    # 8
    #'''
    fig = sns.catplot(df_cat, x='variable', y='total', kind='bar', hue='value', col='cardio').figure
    # fig is now a facetgrid
    #setting axes
    # 9
    #print(type(fig))
    fig.savefig('catplot.png')
    
    return fig
    

# 10

def draw_heat_map():
    # 11
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    #print(df_heat)
    # 12
    #df_heat = df_heat.drop(cont)

    
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr,dtype=bool))

    #print(mask)


    # 14
    fig, ax = plt.subplots()

    # 15
    sns.heatmap(
        corr,
        mask=mask,
        vmax=.3,
        annot=True,
        fmt='.1f',
        square='True',
        linewidth=.5,
        cbar_kws={"shrink": .5},
        ax=ax
    )



    # 16
    fig.savefig('heatmap.png')
    return fig
    