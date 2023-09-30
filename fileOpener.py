import pandas as pd
import joblib

main_file_name, cities_file_name = "NautralSciences_Dataset.xlsx"
main_sheet = "Fires"
mf = pd.read_excel(io=main_file_name, sheet_name=main_sheet, usecols="Y, AC, AD, AE, AF, AI")
with open('dataset.pkl', 'wb') as file:
    joblib.dump(mf, file)

