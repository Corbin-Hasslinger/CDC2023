import pandas as pd
import joblib

main_file_name, cities_file_name = "NautralSciences_Dataset.xlsx", "uscities.xlsx"
main_sheet, cities_sheet = "Fires", "Sheet1"
mf = pd.read_excel(io=main_file_name, sheet_name=main_sheet, usecols="Y, AC, AD, AE, AF")
with open('dataset.pkl', 'wb') as file:
    joblib.dump(mf, file)
# cf = pd.read_excel(io = cities_file_name, sheet_name=cities_file_name, usecols="A, ")
print(mf.head(5))

