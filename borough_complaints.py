import argparse
import pandas as pd
import sys

def main(): 
    parser = argparse.ArgumentParser(description="Count complaint types per borough in a given date range.")
    parser.add_argument("-i", "--input", required=True, help="Path to the input CSV file")
    parser.add_argument("-s", "--start", required=True, help="Start date in YYYY-MM-DD format")
    parser.add_argument("-e", "--end", required=True, help="End date in YYYY-MM-DD format")
    parser.add_argument("-o", "--output", help="Path to the output CSV file (optional)")
    args = parser.parse_args()

    try: 
        df = pd.read_csv(args.input, encoding='utf-8', low_memory=False)
    except Exception as e: 
        print(f"Error reading input file: {e}")
        sys.exit(1)

    if 'Created Date' not in df.columns:
        print("Error: 'Created Date' column not found in the input file.")
        sys.exit(1)

    df['Created Date'] = pd.to_datetime(df['Created Date'], format="%m/%d/%Y %I:%M:%S %p", errors='coerce')

    start_date = pd.to_datetime(args.start)
    end_date = pd.to_datetime(args.end)
    df_filtered = df[(df['Created Date'] >= start_date) & (df['Created Date'] <= end_date)]

    if 'Complaint Type' not in df_filtered.columns or 'Borough' not in df_filtered.columns:
        print("Error: Required columns ('Complaint Type', 'Borough') not found in the input file.")
        sys.exit(1)

    grouped = df_filtered.groupby(['Complaint Type', 'Borough']).size().reset_index(name='Count')
    grouped = grouped.sort_values(by=['Complaint Type', 'Borough'])

    if args.output:
        grouped.to_csv(args.output, index=False)
    else: 
        print("complaint type,borough,count")
        for _, row in grouped.iterrows():
            print(f"{row['Complaint Type']},{row['Borough']},{row['Count']}")

if __name__ == "__main__":
    main()