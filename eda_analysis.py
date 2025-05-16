import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def run_eda(input_path=r'C:/Users/NINJA/Documents/inflation_commodity_analysis/data/cleaned_data.csv'):
    """
    Analisis dan Visualisasi Tren Inflasi
    """
    # Load data bersih
    df = pd.read_csv(input_path)

    df['Periode'] = pd.to_datetime(df['Periode'], errors='coerce')


    import numpy as np
    plt.figure(figsize=(10,5))
    plt.plot(df['Periode'], df['Inflasi'], marker='o', linestyle='-')
    plt.title('Tren Inflasi Indonesia (2019–2024)')
    plt.xlabel('Periode')
    plt.ylabel('Inflasi (%)')


    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(bymonth=[1, 6]))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))


    plt.xticks(rotation=45, ha='right')

    plt.grid(True)
    plt.tight_layout()
    plt.show()


    # Tampilkan inflasi tertinggi dan terendah
    max_inflasi = df.loc[df['Inflasi'].idxmax()]
    min_inflasi = df.loc[df['Inflasi'].idxmin()]

    print(">> Inflasi Tertinggi:")
    print(max_inflasi)

    print("\n>> Inflasi Terendah:")
    print(min_inflasi)

if __name__ == "__main__":
    run_eda()
