from bs4 import BeautifulSoup
import requests
import urllib3


def parse():
    urllib3.disable_warnings()  # отключаем варнинги чтобы пустило на сайт
    url = 'https://omgtu.ru/general_information/the-structure/the-department-of-university.php'
    page = requests.get(url, verify=False)
    print(page.status_code)  # ответ от страницы
    soup = BeautifulSoup(page.text, "html.parser")
    block = soup.findAll('div', id="pagecontent")  #находим тег "ul", где нужные нам данные
    description = ''
    for data in block:
        if data.find('a'):
            descriptiontest = data.text
            description = descriptiontest.replace('\n\n', '') + '\n'  # записываем с него текст
    description.strip() #убираем при выводе в файл верхние и нижние сносы строк
    return(description)


def file(department):
    f = open('department.txt', 'w')
    f.write(department)
    f.close()