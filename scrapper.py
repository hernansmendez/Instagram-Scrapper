import requests
from bs4 import BeautifulSoup
import time


def scrap():
    print("\n" * 1)
    user = input("Ingrese un nombre de usuario: ")
    time.sleep(0.1)  # Wait for 0.1 seconds

    url = f"https://www.instagram.com/{user}/"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    meta_data = soup.find_all('meta', attrs={'property': 'og:description'})
    followers = meta_data[0].get('content').split()[0]
    following = meta_data[0].get('content').split()[2]
    posts = meta_data[0].get('content').split()[4]

    print("\n" * 1)
    print('Followers:', followers)
    print('Following:', following)
    print('Posts:', posts)
    print(url)
    print("\n" * 1)

    while True:
        user_input = input('Presione Enter para ingresar otro usuario o escriba "salir" para terminar: ')
        if user_input.lower() == 'salir':
            print("\n" * 1)
            print("Python Tool developed by Hernán Mendez. All rights reserved.")
            print("\n" * 1)
            break
        elif user_input == '':
            print("\n" * 1)  # Add some blank lines to clear the output
            scrap()
            break

scrap()
