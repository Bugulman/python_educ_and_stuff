import urllib.request
from bs4 import BeautifulSoup

get = urllib.request.urlopen("https://dist.cpk-tatneft.ru/mod/quiz/review.php?attempt=372598&cmid=7128")
html = get.read()

soup = BeautifulSoup(html, 'lxml')

answers = soup.find('form').get('action')
print(answers)
