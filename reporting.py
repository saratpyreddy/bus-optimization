import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def summary_report(results_df):
    print(results_df.groupby(['route', 'day'])[['buses_allocated','paid_seats','free_seats','revenue']].sum())
    print("\nPeak slots by route:")
    print(results_df.groupby(['route', 'slot'])[['paid_seats','free_seats']].sum())

def plot_occupancy(results_df):
    sns.set(style="whitegrid")
    for route in results_df['route'].unique():
        plt.figure(figsize=(10,6))
        subset = results_df[results_df['route']==route]
        sns.barplot(x='slot', y='buses_allocated', hue='day', data=subset)
        plt.title(f'Buses Allocated per Slot - {route}')
        plt.show()
