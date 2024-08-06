from settings import config
from bs4 import BeautifulSoup

import pandas as pd

import requests


def get_html(url):
    response = requests.get(url)
    return response.text


def parse_headers(table):
    headers = table.find_all('tr')[1].find_all('td')
    return [header.text for header in headers]


def parse_table(url):
    page = get_html(url)
    soap = BeautifulSoup(page, "lxml")
    abitu_table = soap.find('table', id='t_common')

    headers = parse_headers(abitu_table)

    table_rows = abitu_table.find_all('tr')[2:]

    table = []
    for row in table_rows:
        row_data = []
        for td in row.find_all('td'):
            row_data.append(td.text.strip())
        table.append(row_data)
    df = pd.DataFrame(table, columns=headers)
    return df


def main():
    url = config.URL_IB
    table = parse_table(url)
    table.to_csv('table.csv', index=False)


if __name__ == "__main__":
    main()
