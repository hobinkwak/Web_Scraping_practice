import requests
import json
from bs4 import BeautifulSoup

def send_msg(msg,
             WEBHOOK_URL = "https://hooks.slack.com/services/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"):
    payload = {
        #'channel' : '@곽호빈',
        'username' : '날씨를 알려주는 호빈',
        'text' : msg,
    }
    requests.post(WEBHOOK_URL, data=json.dumps(payload))
    
#def forecast(lat, lng, TOKEN='52b4cd56c007d2863acc0cla9c8de16c'):
#    url = 'https://api.darksky.net/forecast/{}/{}/{}'.format(TOKEN, lat, lng)
#    response = requests.get(url)
#    json_obj = response.json()
    
#    return json_obj['currently']['summary']
    
    
#lat, lng = 37.5665, 126.9780
#msg = forecast(lat, lng)
#send_msg(msg)

def today_weather(city='서울'):
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={} 날씨'.format(city)
    res = requests.get(url)
    doc = BeautifulSoup(res.text, 'lxml')
    today_weather_summary = doc.select('#main_pack > section.sc_new.cs_weather._weather > div > div.api_cs_wrap > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.main_info > div > ul > li:nth-child(1) > p')[0].get_text()
    today_weather = doc.select('#main_pack > section.sc_new.cs_weather._weather > div > div.api_cs_wrap > div.weather_box > div.weather_area._mainArea > div.table_info.weekly._weeklyWeather > ul:nth-child(2) > li:nth-child(1) > dl > dd')[0].get_text()
    return today_weather +' ' + today_weather_summary

msg = today_weather()
send_msg(msg)