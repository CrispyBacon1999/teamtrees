import requests
import time
import os
from sys import argv
from art import text2art
from colorama import Fore
from bs4 import BeautifulSoup


def load(last, lastTime, trees=True, topDonations=False, recentDonations=False):
    req = requests.get("https://teamtrees.org/")
    soup = BeautifulSoup(req.text, features="html.parser")
    count = int(soup.find("div", {"id": "totalTrees"}).attrs['data-count'])
    trees_per_second = -1
    curr_time = time.time()
    if last != -1:
        time_diff = curr_time - lastTime
        tree_diff = count - last
        trees_per_second = tree_diff / time_diff
    t = text2art(str(count), font="char1")
    os.system('cls')
    print(Fore.GREEN + t)
    print(Fore.CYAN +
          f"Last Updated: {time.strftime('%m-%d-%Y at %I:%M:%S %p')}{Fore.MAGENTA + '  ' + str(trees_per_second) + ' tps' if trees_per_second != -1 else ''}")
    return (count, curr_time)


delay = float(argv[1]) if len(argv) > 1 else 10.0

os.system('mode 72,11')
os.system(f'title Team Trees Live Count ({delay}s)')
last = load(-1, -1)
while True:

    try:
        load(*last)
    except:
        pass
    time.sleep(delay)
