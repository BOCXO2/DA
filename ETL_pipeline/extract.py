import requests
from logger import logger

API_URL = "https://randomuser.me/api/"

def extract_data(records=10):
    users = []
    try:
        for _ in range(records):
            response = requests.get(API_URL)
            response.raise_for_status()
            data = response.json()['results'][0]
            users.append({
                "name": f"{data['name']['first']} {data['name']['last']}",
                "email": data['email'],
                "gender": data['gender'],
                "country": data['location']['country']
            })
            logger.info("Извлеченные пользователи: %s", users[-1]["name"])
        return users
    except requests.exceptions.RequestException as e:
        logger.error("Извлечение завершено с ошибкой: %s", e)
        return {}
    
if __name__ == "__main__":
    data = extract_data(5)
    print(data)