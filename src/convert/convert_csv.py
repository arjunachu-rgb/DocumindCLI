import pandas as pd
def convert_csv(data, output_file):
    try:
        df = pd.DataFrame(data)
        df.to_csv(output_file, index=False, encoding="utf-8")

        print("CSV file created successfully:", output_file)

    except Exception as error:
        print("Error creating CSV file:", error)
