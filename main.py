import requests as req
import re
import os
from datetime import datetime, timedelta
from sys import stderr
from pprint import pprint


def fetch_mp3_files(date):
    resp = req.get("https://radonezh.ru/radio/" + date.strftime("%Y/%m/%d"))
    links = re.findall(r"http://.*mp3#00:00", resp.text)

    links = list(set(links))
    # pprint(links)
    dir_name = date.strftime("%Y-%m-%d")
    try:
        os.mkdir(dir_name, 0o777)
    except Exception as e:
        print(stderr, "Cant create folder with name {} : {}".format(dir_name, str(e)))
        return
    print("Start downloading, date: ", dir_name)
    for i, link in enumerate(links):
        mp3 = req.get(link)
        with open(dir_name + '/' + str(i + 1) + ".mp3", 'wb') as f:
            f.write(mp3.content)
        print("{} track of {} downloaded".format(i + 1, len(links)))
    print("Complete!")


def main():
    yesterday = datetime.now() - timedelta(1)
    fetch_mp3_files(yesterday)


if __name__ == "__main__":
    main()
