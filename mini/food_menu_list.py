import requests
from bs4 import BeautifulSoup as bs
address = 'http://www.andong.ac.kr/main/module/foodMenu/view.do?manage_idx=21&memo5=2020-08-12'
res = requests.get(address)
soup = bs(res.text,'html.parser')

table = soup.select_one('dl:nth-child(2) dd')
print(table.get_text('\n'))