# import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# import data
df = pd.read_csv('final/subscribers.csv')

# --- correlation matrix ---
# preprocess data
corr_df = df.drop(columns=['Unnamed: 0', 'subid',
                           'account_creation_date', 'trial_end_date',
                           'last_payment', 'next_payment', 'cancel_date'])
corr_df = pd.get_dummies(corr_df)
corr_df['current_sub_TF_True'] = df['current_sub_TF'].map(
    lambda x: 1 if x == True else 0)
corr_df['current_sub_TF_False'] = df['current_sub_TF'].map(
    lambda x: 1 if x == False else 0)
print('data preprocessed...')

# calculate correlation matrix
full_corr_matrix = corr_df.corr()[corr_df.columns]
print('correlation matrix calculated...')

# plot heatmap
f, ax = plt.subplots(figsize=(80, 80))
heatmap = sns.heatmap(full_corr_matrix,
                      square=True,
                      linewidths=.5,
                      cmap='coolwarm',
                      cbar_kws={'shrink': .4,
                                'ticks': [-1, -.5, 0, 0.5, 1]},
                      vmin=-1,
                      vmax=1,
                      annot=True,
                      annot_kws={'size': 12})
# add the column names as labels
ax.set_yticklabels(corr_df.columns, rotation=0)
ax.set_xticklabels(corr_df.columns)
sns.set_style({'xtick.bottom': True}, {'ytick.left': True})
sns.set(font_scale=2)
# plt.show()
# plt.savefig('final/full_corr_matrix.png')
