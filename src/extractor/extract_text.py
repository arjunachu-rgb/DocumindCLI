def extract_text(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        return text

    except Exception as error:
        print("Error reading text file:", error)
        return ""
