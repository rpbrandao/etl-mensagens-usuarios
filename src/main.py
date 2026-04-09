from extract import extract_data
from transform import transform_data
from load import load_data

def main():
    input_path = '../data/input.csv'
    output_path = '../data/output.csv'

    df = extract_data(input_path)
    df = transform_data(df)
    load_data(df, output_path)

if __name__ == "__main__":
    main()
