import chardet

def fix_csv_encoding(input_file, output_file):
    # Detect file encoding
    with open(input_file, 'rb') as file:
        result = chardet.detect(file.read())
        encoding = result['encoding']
        print(f"Detected encoding: {encoding}")

    # Read and re-save file with UTF-8 encoding
    try:
        with open(input_file, 'r', encoding=encoding) as infile:
            data = infile.read()

        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(data)

        print(f"File successfully re-encoded to UTF-8: {output_file}")
    except Exception as e:
        print(f"Error while processing file: {e}")

if __name__ == "__main__":
    input_file = "../data/mission_launches.csv"
    output_file = "../data/space_missions_fixed.csv"
    fix_csv_encoding(input_file, output_file)