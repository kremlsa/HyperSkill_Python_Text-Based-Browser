import collections
import sys
import os
import requests as requests
from bs4 import BeautifulSoup
from colorama import Fore

# write your code here
history = collections.deque()
dir_name = sys.argv[1]
if not os.access(dir_name , os.F_OK):
    os.mkdir(dir_name)
os.chdir(dir_name)
while True:
    _url = input()
    if _url == "exit":
        break
    elif _url == "back":
        if len(history) > 0:
            history.pop()
            print(history.pop())
    if "." in _url:
        if not _url.startswith("https://"):
            _url = "https://" + _url
        try:
            r = requests.get(_url)
            soup = BeautifulSoup(r.text , 'html.parser')
            # print(soup.get_text())
            for tag in soup.findAll():
                if tag.name == "a":
                    print(Fore.BLUE + tag.text)
                else:
                    print(tag.text)
            with open(_url[_url.index("/") + 2: _url.index(".")] , 'w') as f:
                f.write(soup.get_text())
        except ConnectionError:
            print("Incorrect URL")
    elif _url == "back":
        if len(history) > 0:
            history.pop()
            print(history.pop())
    else:
        if os.access(_url , os.F_OK):
            with open(_url , 'r') as f:
                temp = f.read()
                print(temp)
                history.append(temp)
        else:
            print("Error: Incorrect URL")
