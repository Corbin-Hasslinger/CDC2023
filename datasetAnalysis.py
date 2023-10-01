import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

with open('dataset.pkl', 'rb') as file:
    df = joblib.load(file)

state_counts= df["STATE"].value_counts()
top_10_state_counts = state_counts.head(10)

grouped_data = df.groupby(['STATE', 'FIRE_SIZE_CLASS']).size().reset_index(name='COUNT')
# Fill any missing values in the 'Count' column with 0
pivot_table = grouped_data.pivot_table(index='STATE', columns='FIRE_SIZE_CLASS', values='COUNT', fill_value=0).astype(int)

pivot_table['TotalCount'] = pivot_table.sum(axis=1)
print(pivot_table)
top_g_counts = pivot_table.sort_values(by = 'G', ascending = False).head(10)
print(top_g_counts)
fire_class_counts = pivot_table.sort_values(by='TotalCount', ascending=False).head(10)

# Create a new DataFrame to associate rankings with states and the corresponding counts
def total_state_count():
    x = top_10_state_counts.values
    y = top_10_state_counts.index.tolist()
    data = pd.DataFrame({'States': y, 'Counts': x})

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Counts", y="States", data=data, palette="Blues_d")
    plt.xlabel('Fire Count', fontsize=12)
    plt.ylabel('States', fontsize=12)
    plt.title('Top 10 Most Common State Locations of Fires', fontsize=14)

    plt.show()

def class_state_count():
    plt.figure(figsize=(10, 6))
    sns.set(style="whitegrid")

    state_order = fire_class_counts.index.values  # Use index to access state names
    excluded_fire_classes=['A','B','C','D','E','F']
    excluded_fire_classes2=['A','B','C','D','E','G']
    excluded_fire_classes3=['A','B','C','D','F','G']

    # Define the order of fire classes in reverse
    fire_class_order = list((fire_class_counts.columns))

    # Loop through fire classes and plot them with different colors
    for fire_class in fire_class_order:
        if fire_class != 'TotalCount' and fire_class not in excluded_fire_classes3:
            sns.barplot(x=fire_class, y=state_order, data=fire_class_counts, label='E', color='#8AC7DB')
    for fire_class in fire_class_order:
        if fire_class != 'TotalCount' and fire_class not in excluded_fire_classes2:
            sns.barplot(x=fire_class, y=state_order, data=fire_class_counts, label='F', color='#43A6C6')
    for fire_class in fire_class_order:
        if fire_class != 'TotalCount' and fire_class not in excluded_fire_classes:
            sns.barplot(x=fire_class, y=state_order, data=fire_class_counts, label='G', color="b")
    # Customize labels and title
    plt.xlabel('Count', fontsize=12)
    plt.ylabel('States', fontsize=12)
    plt.title('Top 10 States by Fire Class Count', fontsize=14)
    plt.legend(title='Fire Class')

    plt.show()

def g_state_counts():
    state_names = top_g_counts.index.tolist()
    g_counts = top_g_counts['G'].tolist()

    # Define the order of fire classes in reverse
    g_data = pd.DataFrame({'State': state_names, 'G_Count': g_counts})

    sns.barplot(x='G_Count', y='State', data=g_data, palette='Blues_d')
    # Customize labels and title
    plt.xlabel('G-Count', fontsize=12)
    plt.ylabel('States', fontsize=12)
    plt.title('Top 10 States by Fire Class Count', fontsize=14)
    plt.legend(title='Fire Class')

    plt.show()

total_state_count()
class_state_count()

g_state_counts()