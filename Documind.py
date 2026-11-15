import os
from src.parser import create_parser, parse_file
from src.display import display_table
from src.convert.convert_csv import convert_csv
from src.summarizer import summarize_data
from src.convert.convert_json import convert_json
def main():
    parser = create_parser()
    args = parser.parse_args()
    input_file = args.input
    output_format = args.format

    if not os.path.isfile(input_file):
        print("Error: Input file does not exist.")
        return

    try:
        data = parse_file(input_file)
        display_table(data)
        summary = summarize_data(data)

        print("\n----- Document Summary -----")
        print(summary)
        print("----------------------------")

        output_folder = "Result"
        os.makedirs(output_folder, exist_ok=True)

        file_name = os.path.splitext(
            os.path.basename(input_file)
        )[0]

    
        if output_format == "csv":
            output_file = os.path.join(
                output_folder, file_name + ".csv"
            )

            if isinstance(data, str):
                data = [{"text": data}]

            convert_csv(data, output_file)

        elif output_format == "json":
            output_file = os.path.join(
                output_folder, file_name + ".json"
            )

            if isinstance(data, str):
                data = {"text": data}

            convert_json(data, output_file)

    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
