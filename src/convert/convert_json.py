import json
def convert_json(data, output_file):
    try:
        with open(output_file, "w", encoding="utf-8") as file:json.dump(data, file, indent=4, ensure_ascii=False)
        print("JSON file created successfully:", output_file)
    except Exception as error:
        print("Error creating JSON file:", error)
