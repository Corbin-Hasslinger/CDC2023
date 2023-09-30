import pandas as pd

file_name = "NautralSciences_Dataset.xlsx"
sheet = "Fires"
df = pd.read_excel(io=file_name, sheet_name=sheet)
print(df.head(5))
