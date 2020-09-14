# BeautifulSoup 모듈로 날씨 가져오기
"""from urllib import request
from bs4 import BeautifulSoup

import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

target = request.urlopen("https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

soup = BeautifulSoup(target, "html.parser")


for location in soup.select("location"):
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)
    print()"""



# Flask 모듈 사용하기
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello World!<h1>"

