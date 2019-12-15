import requests as req
import re
import os
from datetime import datetime, timedelta
from pprint import pprint

yesterday = datetime.now() - timedelta(1)
print(yesterday.strftime("%Y/%m/%d"))
resp = req.get("https://radonezh.ru/radio/" + yesterday.strftime("%Y/%m/%d"))

links = re.findall(r"http://.*mp3\#00:00", resp.text)

links = list(set(links))

#pprint(links)

dir_name = yesterday.strftime("%Y-%m-%d")
os.mkdir(dir_name,0o777)
for i, link in enumerate(links):
    mp3 = req.get(link)
    with open(dir_name + '/' + str(i+1) + ".mp3", 'wb') as f:
        f.write(mp3.content)
    print("{} track of {} downloaded".format(i+1, len(links)))
print("Complete!")

