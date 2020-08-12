from selenium import webdriver
from bs4 import BeautifulSoup


#取的網頁source code
url = 'https://www.cwb.gov.tw/V8/C/W/County/index.html'
browser = webdriver.Chrome()
browser.get(url)
browser.find_element_by_xpath('//*[@title="明日白天"]').click()
source = browser.page_source
soup = BeautifulSoup(source, 'html.parser')
browser.close()


#從HTML找到要爬那些資料
city = soup.find('div', attrs={'class': 'col-md-8'}).find_all('p', attrs={'class': 'city'})
temperature = soup.find('div', attrs={'class': 'col-md-8'}).find_all('span', attrs={'class': 'tem-C is-active'})
rain = soup.find('div', attrs={'class': 'col-md-4'}).find_all('span', attrs={'class': 'rain'})

#將資料放進陣列
data = []
temperaturedata = []
raindata = []

for x in city:
    setcitydata = {'縣市':x.text}
    data.append(dict(setcitydata))
    
for y in temperature:
    settemperaturedata = {'氣溫':y.text}
    temperaturedata.append(dict(settemperaturedata))
    
for g in rain:
    setraindata = {'降雨機率':g.text}
    raindata.append(dict(setraindata))
    
for z in range(len(data)):
    data[z].update(temperaturedata[z])
    data[z].update(raindata[z])
    


# interface
while True:
    str = input("請輸入縣市: ")
    if str == 'exit':
        break
    elif str == 'all':
        for x in range(len(data)):
            print('縣市: {:s}  氣溫: {:s}  降雨機率: {:s}'.format(data[x]['縣市'], data[x]['氣溫'],data[x]['降雨機率']))
        break
    else:
        index = next((i for i, item in enumerate(data) if item["縣市"] == str), None)
        if index in range(0,len(data)):
            print('縣市: {:s}  氣溫: {:s}  降雨機率: {:s}'.format(data[index]['縣市'], data[index]['氣溫'],data[index]['降雨機率']))
        else:
            print('請輸入正確的縣市名稱')
