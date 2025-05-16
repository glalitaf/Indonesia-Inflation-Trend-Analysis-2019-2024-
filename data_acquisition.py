import pandas as pd

def load_local_data(file_path=r'C:/Users/NINJA/Documents/inflation_commodity_analysis/data/raw_data.xlsx'):
    df = pd.read_excel(file_path)
    print(">> Data berhasil dimuat dari:", file_path)
    print(">> Preview 5 baris pertama:")
    print(df.head())
    return df

# PENTING! Ini WAJIB ADA untuk eksekusi langsung
if __name__ == "__main__":
    load_local_data()
