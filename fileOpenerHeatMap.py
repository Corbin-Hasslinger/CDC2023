import pandas as pd

main_file_name, cities_file_name = "NautralSciences_Dataset.xlsx", "uscities.xlsx"
main_sheet, cities_sheet = "Fires", "Sheet1"
df = pd.read_excel(io=main_file_name, sheet_name=main_sheet, usecols="Y, AC, AE, AF",nrows = 50)


