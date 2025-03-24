from extract import extract_data
from transform import transform_data
from load import load_data

def run_etl():
    # 1. Извлечение данных
    raw_data = extract_data(10)

    # 2. Преобразование данных
    df = transform_data(raw_data)

    # 3. Загрузка данных
    load_data(df)

if __name__ == ("__main__"):
    run_etl() 