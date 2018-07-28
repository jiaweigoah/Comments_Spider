import requests
import json
import time
import random

danmu_html = "https://mfm.video.qq.com/danmu?otype=json&timestamp={}&target_id={}&count=800"
target_id = '2722492267'

times = 0
'''
while True:
    html = danmu_html.format(times, target_id)
    times += 30
    time.sleep(6)
    if times >= 300:
        break
    print(times)
    print(html)
    '''
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)'
]
user_agent = random.choice(user_agents)
headers = {
        'user-agent': user_agent
    }

html = danmu_html.format(30000, target_id)
wb_data = requests.get(html, headers=headers, proxies = None).text
#print(wb_data)
js_dict = json.loads(wb_data)
#print(js_dict)
a = 5

b = js_dict['comments']
if b == []:
    raise NameError
for i in b:
    comment = i['content']
    upcount = i["upcount"]
    usr_name = i['opername']
    lists = [comment, upcount, usr_name]
    print('lists')
    if lists == []:
        print('false')