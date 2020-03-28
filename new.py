import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
music = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

i = 1
for rank in music:
    artist = music.select_one('a.title.ellipsis')
    title = music.select_one('a.artist.ellipsis')

    if artist is not None and title is not None:
        print (str(i) + "위 : " + artist.get_text() + title.get_text())
        i = i + 1

