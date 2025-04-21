def clean_netflix_data(input_path, output_path):
    df = pd.read_csv(input_path, encoding='ISO-8859-1')
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    df.drop_duplicates(inplace=True)
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    for col in ['type', 'rating', 'country']:
        df[col] = df[col].astype(str).str.strip().str.title()
    print(df.isnull().sum())
    df.to_csv(output_path, index=False)
