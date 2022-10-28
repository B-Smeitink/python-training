"""
APIs
"""

import requests
import pandas as pd


def main():
    url = "https://opendata.rdw.nl/resource/m9d7-ebf2.json"
    my_filter = {'$limit': '50200'}
    r = requests.get(url, params=my_filter).json()
    # for car in r:
    #     print(car["kenteken"])
    print(len(r))


if __name__ == '__main__':
    main()
