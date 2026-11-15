from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def extract_image(file_path):
    try:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)

        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        if not lines:
            return ""

        rows = []
        for line in lines:
            columns = line.split("  ")
            columns = [
                column.strip()
                for column in columns
                if column.strip()
            ]
            rows.append(columns)

        return rows

    except Exception as error:
        print("Error reading image:", error)
        return ""