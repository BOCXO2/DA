from sqlalchemy import create_engine
from logger import logger
from config import DB_CONFIG

def get_db_engine():
    url = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    return create_engine(url)

def load_data(df, table_name="users"):
    if df.empty:
        logger.warning("Отсутствуют данные для загрузки")
        return
    
    engine = get_db_engine()
    try:
        df.to_sql(table_name, con=engine, if_exists='append', index=False)
        logger.info("Загруженные %d записи в таблицу '%s'.", len(df), table_name)
    except Exception as e:
        logger.error("Загрузка завершена с ошибкой: %s", e)