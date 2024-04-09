from bs4 import BeautifulSoup
import requests
import urllib3


def parse():
    urllib3.disable_warnings()
    url = 'https://omgtu.ru/general_information/the-structure/the-department-of-university.php'
    page = requests.get(url, verify=False)
    print(page.status_code)  # ответ от страницы
    soup = BeautifulSoup(page.text, "html.parser")
    block = soup.findAll('div', id="pagecontent")
    description = ''
    for data in block:
        if data.find('a'):
            descriptiontest = data.text
            description = descriptiontest.replace('\n\n', '') + '\n'
    description.strip() #убираем верхние и нижние сносы строк
    return(description)


def file(department):
    f = open('department.txt', 'w')
    f.write(department)
    f.close()