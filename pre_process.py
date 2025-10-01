import pandas as pd 

df = pd.read_csv("2024_short.csv", low_memory=False)

df['Created Date'] = pd.to_datetime(df['Created Date'], format="%m/%d/%Y %I:%M:%S %p", errors='coerce')
df['Closed Date'] = pd.to_datetime(df['Closed Date'], format="%m/%d/%Y %I:%M:%S %p", errors='coerce')
df['Duration'] = (df['Closed Date'] - df['Created Date']).dt.total_seconds() / 3600.0
df = df.dropna(subset=['Duration', 'Incident Zip'])
df['YearMonth'] = df['Created Date'].dt.to_period('M')

zip_codes = df['Incident Zip'].unique()
zips = []
for zip_code in zip_codes:
    zips.append(str(zip_code))
data_dict = {zip: [] for zip in zips}

grouped = df.groupby(['YearMonth', 'Incident Zip'])['Duration'].mean().reset_index()

for zip_code in zip_codes:
    zip_data = grouped[grouped['Incident Zip'] == zip_code].sort_values(by='YearMonth')
    data_dict[zip_code] = zip_data['Duration'].tolist()
