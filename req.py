import requests
from pprint import pprint

class Menu:
    def __init__(self) -> None:
        self.URL = "https://apps.bcccatering.com.tr/bccdeyizapi/api/webmenu/GetMenuOfProject"
        self.PAYLOAD = "{\n  \"ProjectName\": \"\",\n  \"Project\": \"aGZ1c3piNGRpYUwzNS8xT3Vnemx3WEJWWFAwSWFRR0tUK2pMUXZzSXNYTDdmZmpsbGFMcnEvU2lrVmtyRGZMdkFlVVNWT1FmdC9DMWdkdXllL1BOV0w1Q2pNWS9abVRzVitwbWU5T3FBdlNwekpFYUNQaUpRSjV6WWNzQXc2RmRtK1hiZTdhbDdYc1RXOTl2WjFHWHp3PT0\"\n}"
        self.HEADERS = {
        'authority': 'apps.bcccatering.com.tr',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,tr-TR;q=0.8,tr;q=0.7',
        'authorization': 'spack JOrqwWLuZFgbpvT5a+Z7+V66QFdEXJC+53Jp3Zn81HbJCMtu0jfzfOcFAFks8dr1gH+m1iOpR2sblLksXgvwlPI+ZEGX7ZUBUhR2ZngUNcWZxyv5Iv2xh0DABl0heBWn',
        'cache-control': 'no-cache,no-store',
        'content-type': 'application/json; charset=UTF-8',
        'if-modified-since': 'Mon, 26 Jul 1997 05:00:00 GMT',
        'lang': 'tr',
        'origin': 'https://mobile.bcccatering.com.tr',
        'qrcode': 'aGZ1c3piNGRpYUwzNS8xT3Vnemx3WEJWWFAwSWFRR0tUK2pMUXZzSXNYTDdmZmpsbGFMcnEvU2lrVmtyRGZMdkFlVVNWT1FmdC9DMWdkdXllL1BOV0w1Q2pNWS9abVRzVitwbWU5T3FBdlNwekpFYUNQaUpRSjV6WWNzQXc2RmRtK1hiZTdhbDdYc1RXOTl2WjFHWHp3PT0',
        'referer': 'https://mobile.bcccatering.com.tr/',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'userid': '2'
        }
    def get_menu(self) -> list:
        response = requests.request("POST", self.URL, headers=self.HEADERS, data=self.PAYLOAD)
        menu = response.json()["dailymenu"]["meals"][0]["menuMembers"]
        return [f"{meal['name'] : <40} {meal['calorivalue'] : >7} cal." for meal in menu]

if __name__ == '__main__':
    menu = Menu()
    pprint(menu.get_menu())