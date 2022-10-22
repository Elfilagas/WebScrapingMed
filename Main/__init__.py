import requests
import os
import csv
import json
from datetime import datetime


def collect_data():
    cur_date = datetime.now().strftime('%d_%m_%Y')

    response = requests.get(url='https://www.lifetime.plus/api/analysis2')

    # with open(f'info_{cur_date}.json', 'w') as file:
    #     json.dump(response.json(), file, indent=4, ensure_ascii=False)

    categories = response.json()['categories']
    result = []
    for c in categories:
        c_name = c.get('name').strip()
        c_items = c.get('items')

        for item in c_items:
            item_name = item.get('name').strip()
            item_price = item.get('price')
            #item_desc = item.get('description').strip()
            item_waittime = item.get('days')
            item_bio = item.get('biomaterial')

            result.append(
                [c_name, item_name, item_bio, item_price, item_waittime]
            )

    with open(f'result_{cur_date}.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                'Категория',
                'Анализ',
                'Биоматериал',
                'Стоимость',
                'Готовность в днях'
            )
        )

        writer.writerows(result)


def main():
    collect_data()


if __name__ == '__main__':
    main()
