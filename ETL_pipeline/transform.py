import pandas as pd
from logger import logger
from extract import extract_data

def transform_data(data):
    if not data:
        logger.warning("Нет данных для преобразования")
        return pd.DataFrame()
    
    try:
        df = pd.DataFrame(data)

        df.drop_duplicates(subset=['email'], inplace=True)

        df['name'] = df['name'].str.title()

        df['gender'] = df['gender'].str.capitalize()

        logger.info("Трансформация %d закончена.", len(df))
        return df
    except Exception as e:
        logger.error("Трансформация завершилась с ошибкой: %s", e)
        return pd.DataFrame()
    
if __name__ == ("__main__"):
    raw_data = extract_data(10)
    df = transform_data(raw_data)
    print(df.head())