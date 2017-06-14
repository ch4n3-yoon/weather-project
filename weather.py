# -*- coding : utf-8 -*-
import requests
from bs4 import BeautifulSoup

forcastUrl = 'http://www.kma.go.kr/weather/observation/currentweather.jsp?type=t99&mode=0&stn=0&auto_man=m&tm=2017.06.12.08:00&dtm=1'
r = requests.get(forcastUrl)
soup = BeautifulSoup(r.text, 'html.parser')
td = soup.find_all("td")


currentWeather = td[1].contents[0]
print("[*] 현재 날씨 : " + currentWeather)

currentTemper = td[5].contents[0]
print("[*] 현재 기온 : " + currentTemper + "℃")


discomfortIndex = int(td[7].contents[0])
print("[*] 현재 불쾌지수 : %d " % (discomfortIndex), end="")

if discomfortIndex > 80:
	print("(매우 높음)")
elif discomfortIndex > 75:
	print("(높음)")
elif discomfortIndex > 68:
	print("(보통)")
else:
	print("(낮음)")


humid = int(td[9].contents[0])
print("[*] 현재 습도 : %d%% " % (humid))
