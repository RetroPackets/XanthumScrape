import re
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
from bs4 import BeautifulSoup
from colorama import Fore,Style

cyan = "\033[1;36;40m"
green = "\033[1;32;40m"
red = "\033[1;31;40m"
Y = '\033[1;33;40m'



print(f"""
{Fore.WHITE}
      _____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______________
      ______¶¶¶¶¶¶¶¶¶___________¶¶¶¶¶¶¶¶¶_______
      ____¶¶¶¶¶__________¶¶¶¶¶__________¶¶¶¶¶___
      ____¶¶___________¶¶¶¶¶¶¶¶¶____________¶¶__
      ____¶¶__________¶¶¶¶¶¶¶¶¶¶¶___________¶¶__
      ____¶¶______________¶¶¶¶¶¶____________¶¶__
      ____¶¶_____________¶¶¶¶¶¶¶____________¶¶__
      ____¶¶______¶¶___¶¶¶¶¶¶¶¶¶____________¶¶__
      ____¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶_¶_____¶¶__
      ____¶¶_____¶¶¶¶¶¶¶¶¶¶¶________¶¶______¶¶__
      ____¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶_______¶¶¶_____¶¶__
      ____¶¶____¶¶¶__¶¶¶¶¶¶¶¶¶¶¶_____¶¶_____¶¶__
      ____¶¶______¶¶____¶¶¶¶¶¶¶¶¶____¶¶_____¶¶__
      ____¶¶_______¶_____¶¶¶¶¶¶¶¶¶_¶¶¶______¶¶__
      ____¶¶_____________¶¶¶¶¶¶¶¶¶¶¶________¶¶__
      ____¶¶_____________¶¶¶¶¶¶¶_¶_________¶¶___
      _____¶¶_______¶¶___¶¶¶¶¶¶¶__________¶¶____
      ______¶¶______¶¶¶¶¶¶¶¶¶¶¶__________¶¶_____
      _______¶¶_____________¶¶¶_________¶¶______
      ________¶¶___________¶¶__________¶¶_______
      _________¶¶_________¶¶__________¶¶________
      __________¶¶______¶¶¶__________¶¶_________
      ___________¶¶¶_______________¶¶___________
      _____________¶¶____________¶¶¶____________
      _______________¶¶¶_______¶¶¶______________
      _________________¶¶¶__¶¶¶_________________
      ____________________¶¶____________________
                                             
{Fore.WHITE}▀▄▀ ▄▀█ █▄░█ ▀█▀ █░█ █░█ █▀▄▀█   █▀ █▀▀ █▀█ ▄▀█ █▀█ █▀▀
█░█{Fore.CYAN} █▀█ █░▀█ ░█░ █▀█ █▄█ █░▀░█   ▄█ █▄▄ █▀▄ █▀█ █▀▀{Fore.WHITE} ██▄
   {Fore.CYAN}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   |{Fore.WHITE}  CREATED BY : RetroPackets{Fore.CYAN}                    |
   |{Fore.WHITE}  INSTAGRAM : @retropacketz    {Fore.CYAN}                |
   |{Fore.WHITE}  GITHUB : https://github.com/RetroPackets{Fore.CYAN}     |
   {Fore.CYAN}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")





starting_url = input(f'{Fore.CYAN}TARGET URL{Fore.WHITE}:{Fore.MAGENTA} ')

unprocessed_urls = deque([starting_url])
processed_urls = set()
emails = set()


while len(unprocessed_urls):

    url = unprocessed_urls.popleft()
    processed_urls.add(url)

    parts = urlsplit(url)
    base_url = "{0.scheme}://{0.netloc}".format(parts)
    path = url[:url.rfind('/')+1] if '/' in parts.path else url

    print(f"{Fore.CYAN}[Xanthum]{Fore.YELLOW} is crawling :{Fore.GREEN} %s" % url)
    try:
        response = requests.get(url)
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        continue

    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
    emails.update(new_emails)
    print(f"{Fore.GREEN}[✔]{Fore.WHITE}", emails, """
""")
    soup = BeautifulSoup(response.text, 'lxml')


    for anchor in soup.find_all("a"):
        link = anchor.attrs["href"] if "href" in anchor.attrs else ''
        if link.startswith('/'):
            link = base_url + link
        elif not link.startswith('http'):
            link = path + link
        if link not in unprocessed_urls and link not in processed_urls:
            unprocessed_urls.append(link)
