import pandas as pd

def clean_marketing_data(input_file: str, output_file: str):
    data = pd.read_csv(input_file, sep="\t")

    if 'Income' in data.columns:
        data['Income'].fillna(data['Income'].median(), inplace=True)

    data.drop_duplicates(inplace=True)

    if 'Education' in data.columns:
        data['Education'] = data['Education'].str.lower().str.strip()
    if 'Marital_Status' in data.columns:
        data['Marital_Status'] = data['Marital_Status'].str.lower().str.strip()

    if 'Dt_Customer' in data.columns:
        data['Dt_Customer'] = pd.to_datetime(data['Dt_Customer'], dayfirst=True, errors='coerce')

    data.columns = [col.lower().replace(" ", "_") for col in data.columns]

    if 'year_birth' in data.columns:
        data['year_birth'] = pd.to_numeric(data['year_birth'], errors='coerce').astype('Int64')
    if 'income' in data.columns:
        data['income'] = pd.to_numeric(data['income'], errors='coerce')

    data.to_csv(output_file, index=False)

    print(f"✅ Cleaned dataset saved as '{output_file}'")

clean_marketing_data("marketing_campaign.csv", "marketing_campaign_cleaned.csv")
