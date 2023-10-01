import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

with open('dataset.pkl', 'rb') as file:
    df = joblib.load(file)

class_counts= df["FIRE_SIZE_CLASS"].value_counts()

total_fire_sizes = {fire_class: 0 for fire_class in df['FIRE_SIZE_CLASS'].unique()}

for i in range(len(df['FIRE_SIZE'])):
    fire_size = df.at[i, 'FIRE_SIZE']
    fire_class = df.at[i, 'FIRE_SIZE_CLASS']
    
    # Add the fire size to the total for the corresponding class
    total_fire_sizes[fire_class] += fire_size
# Display the total fire sizes for each class

myKeys = list(total_fire_sizes.keys())
myKeys.sort()
sorted_dict = {i: total_fire_sizes[i] for i in myKeys}

for fire_class, total_size in total_fire_sizes.items():
    print(f"Total Fire Size for Class {fire_class}: {total_size} acres")

print(total_fire_sizes)
print(total_fire_sizes.values)
print(total_fire_sizes.keys)

def total_damage_count():
    x = list(sorted_dict.values())
    y = list(sorted_dict.keys())
    data = pd.DataFrame({'Classes': y, 'Damage': x})

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Damage", y="Classes", data=data, palette="Blues_d")
    plt.xlabel('Total Damage Acreage', fontsize=12)
    plt.ylabel('Classes', fontsize=12)
    plt.title('Most Damaging Classes of Fire', fontsize=14)
    
    sns.set_style("dark")
    plt.show()



total_damage_count()