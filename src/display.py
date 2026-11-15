from tabulate import tabulate

def display_table(data):
    if isinstance(data, str):
        print("\nExtracted Text:\n")
        print(data)
    elif isinstance(data, dict):
        print(tabulate([data], headers="keys", tablefmt="grid"))
    elif isinstance(data, list):
        if data and isinstance(data[0], dict):
            print(tabulate(data, headers="keys", tablefmt="grid"))
        else:
            print(data)
    elif hasattr(data, "to_dict"):
        print(tabulate(data.to_dict("records"), headers="keys", tablefmt="grid"))
    else:
        print(data)
