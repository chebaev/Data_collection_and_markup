import requests
from config import Configs

config = Configs()

def send_request(city:str) -> dict:
    params = {
        "near": city,
        "query": "restaurant"
    }
    headers = {
        "Accept": "application/json",
        "Authorization": config.api_key.get_secret_value()
    }
    response = requests.get(url=config.url, params=params, headers=headers)
    if response.status_code == 200:
        result = response.json()
    else:
        print(f"Запрос API завершился неудачей с кодом состояния: {response.status_code}")
        result = {}
    return result

def data_processing(data: dict, categoty: str, city:str):
    data = data["results"]
    for venue in data:
        for cat in venue['categories']:
            if categoty in cat['name']:
                print(f"Название: {cat["name"]}\nАдрес: {venue['location']['address']}\n")


def main():
    flag = True
    city = input("Введите название города: ")
    data = send_request(city)
    print('Выберите из списка категорию, что Вас интересует\n')
    while flag:
        print(f'1.Ресторан\n'
              f'2.Еда и напитки\n'
              f'3.Кафе\n'
              f'4.Стейк-хаус\n')
        number = input('Введите число 1 до 4: ')
        if number.isnumeric():
            if 1 <= int(number) <= 4:
                result = ''
                match int(number):
                    case 1:
                        result ='Restaurant'
                    case 2:
                        result ='Dining and Drinking'
                    case 3:
                        result = 'Café'
                    case 4:
                        result = 'Steakhouse'
                data_processing(data=data, categoty=result, city=city)
                flag = False
            else:
                print("Вы ошиблись!!! Введите правильное число")

        else:
            print("Вы ошиблись!!!")


if __name__ == '__main__':
    main()