import pandas as pd
def extract_xlsx(file_path):
    try:
        data = pd.read_excel(file_path)
        records = data.fillna("").to_dict(orient="records")
        return records
    except Exception as error:
        print("Error reading Excel file:", error)
        return []
