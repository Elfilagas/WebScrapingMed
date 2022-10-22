import requests
import os
import csv
import json
from datetime import datetime


def collect_data():
    cur_date = datetime.now().strftime('%d_%m_%Y')

    response = requests.get(url='https://www.lifetime.plus/api/analysis2')

    with open(f'info_{cur_date}.json', 'w') as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)


def main():
    collect_data()


if __name__ == '__main__':
    main()
