 Data Cleaning Task – Marketing Campaign Dataset

 Dataset Used

"marketing_campaign.csv" — A marketing dataset containing demographic and transactional data of customers.

Cleaning Steps Performed

1. Missing Values:
   - Filled 24 missing values in the `Income` column using the "median".

2. Duplicates:
   - Checked and found no duplicate rows, so none were removed.

3. Text Standardization:
   - Standardized text fields like `Education` and `Marital_Status` by converting to lowercase and stripping spaces.

4. Date Formatting:
   - Converted `Dt_Customer` to a proper `datetime` format using `pd.to_datetime()`.

5. Column Renaming:
   - Renamed all columns to lowercase with underscores for consistency and readability.

6. Data Type Fixes:
   - Ensured correct types: `year_birth` as `int`, `income` as `float`, and `Dt_Customer` as `datetime`.

Tools:
- Python
- Pandas library

