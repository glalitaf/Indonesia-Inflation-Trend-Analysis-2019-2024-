import pandas as pd

def clean_data(input_path=r'C:/Users/NINJA/Documents/inflation_commodity_analysis/data/raw_data.xlsx',
               output_path=r'C:/Users/NINJA/Documents/inflation_commodity_analysis/data/cleaned_data.csv'):
    """
    Bersihkan data inflasi yang sudah diunduh dari BI.
    """
    # Load data dan skip baris header yang salah
    df = pd.read_excel(input_path, skiprows=4)

    # Rename kolom agar rapi
    df.columns = ['No', 'Periode', 'Inflasi','Kosong']

    # Ambil column yang dibutuhkan saja

    df=df[['No', 'Periode', 'Inflasi']]

    # Buang baris yang kosong semua (biasanya di akhir file)
    df = df.dropna(how='all')

    # Buang baris yang 'Periode' kosong
    df = df.dropna(subset=['Periode'])

    # Bersihkan tanda % di kolom Inflasi dan ubah ke float
    df['Inflasi'] = df['Inflasi'].str.replace('%', '').str.strip()
    df['Inflasi'] = pd.to_numeric(df['Inflasi'], errors='coerce')


    # Mapping Bulan Indo ke English
    bulan_mapping = {
    'Januari': 'January',
    'Februari': 'February',
    'Maret': 'March',
    'April': 'April',
    'Mei': 'May',
    'Juni': 'June',
    'Juli': 'July',
    'Agustus': 'August',
    'September': 'September',
    'Oktober': 'October',
    'November': 'November',
    'Desember': 'December'
    }

    for indo, eng in bulan_mapping.items():
     df['Periode'] = df['Periode'].str.replace(indo, eng)

   # Tambahkan tanggal 1
    df['Periode'] = '1 ' + df['Periode']

    # Ubah ke datetime dan cek mana yang gagal (NaT)
    df['Periode'] = pd.to_datetime(df['Periode'], format='%d %B %Y', errors='coerce')

    # # Tampilkan yang gagal
    # print("Yang gagal diparse:")
    # print(df[df['Periode_Datetime'].isna()]['Periode_Temp'])

    # Sort berdasarkan Periode
    df = df.sort_values('Periode')


    # Simpan hasil bersih ke CSV
    df.to_csv(output_path, index=False)

    print(f">> Cleaned data berhasil disimpan ke {output_path}")
    print("5 Baris Pertama Data Bersih:")
    print(df.head())

    return df

if __name__ == "__main__":
    clean_data()
