#'黄旭':"http://music.163.com/#/artist?id=12065096"
#'艾福杰尼':"http://music.163.com/#/artist?id=12127564"
#'布瑞吉':"http://music.163.com/#/artist?id=12493701"

#"http://music.163.com/api/v1/resource/comments/R_SO_4_516997458?limit=20&offset=40"
"""
//*[@id="5232514741528613761469"]
//*[@id="auto-id-kPMUocXHrZpiqxeK"]/table/tbody
//*[@id="5232514741528613761469"]/td[4]/div/a
"""
import requests
from bs4 import BeautifulSoup
import json
import simplejson

headers = {  
    'Cookie':'vjuids=cd894bfc.16376faa00f.0.88fbd85462712; _ntes_nnid=c2cbce8a3916c5c491ae038bcb3c7ad9,1526709526558; _ntes_nuid=c2cbce8a3916c5c491ae038bcb3c7ad9; __utma=94650624.301866754.1526783683.1526783683.1526783683.1; __utmz=94650624.1526783683.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; WM_TID=FW7j6LY3QKnDAD99R1BBuav%2FRj2Ypi7P; __f_=1526885804881; usertrack=ezq0plsFfOSDh8/zD0kPAg==; Path=/; __remember_me=true; Expires=Sun, 14-Jan-2018 13:07:08 GMT; _iuqxldmzr_=32; vjlast=1526709527.1528376065.11; vinfo_n_f_l_n3=3767cfeeff39be45.1.1.1528282565822.1528282806015.1528376353016; JSESSIONID-WYYY=wBOXldPr99ZFH%2BqGGfFW4MD0uo31mXNi4EC4IqQDKuabB6Y5VHZaYFGpQEB9D9TAWUDvv%2F%2B1kWnhlKiupgM6JbO%2B%2FJmwb2mfFCSYYDc9%2FcBb%2BDgjjgc84pHY8ePN5x7ERndOFu5xuHIivoHcZpiETptYy3R5uOpl269j%5Cxs%2FNxd%2BEQl%2B%3A1528623658863; MUSIC_U=fba52d7fed2592ea336ed5cbe7a51d0d57b0eb03c4691fdf67d1fe2178fc4638ba2965ae8b3c58210f0b8c648fc701e8af9e62a8590fd08a; __csrf=77e833df4fbd02980d937848a763d4c8',  
    'Host':'music.163.com',  
    'Referer':'http://music.163.com/',  
    'Upgrade-Insecure-Requests':'1',  
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'  
}
'''
wb_data = requests.get("http://music.163.com/artist?id=12127564", headers=headers).text
soup = BeautifulSoup(wb_data, "lxml")
datas = soup.find('textarea').text
lists = json.loads(datas)
print("id:{}".format(lists[0]["id"]))
print(datas)
'''

def WYMusic_list(url, headers, proxies = None):
    lists = []
    wb_data = requests.get(url, headers = headers, proxies=proxies).text
    soup = BeautifulSoup(wb_data, "lxml")
    datas = soup.find('textarea').text
    print(datas)
    js_dict = json.loads(datas)
    for i in js_dict:
        lists.append(i["id"])
    return lists

#print(WYMusic_list('http://music.163.com/#/artist?id=12065096', headers = headers))

def WYMusic_comments(url, headers, proxies = None):
    lists = []
    offset = 0
    while True:
        html = "http://music.163.com/api/v1/resource/comments/R_SO_4_{}?limit=20&offset={}".format(str(url), offset)
        try:
            wb_data = requests.get(html, headers = headers, proxies = proxies).text
            js_dict = simplejson.loads(wb_data)
            #print(js_dict)
            a = js_dict['comments'][0]['user']['nickname']
            print(a)
                #break
            for i in js_dict['comments']:
                usr = i['user']['nickname']
                usrID  = i['user']['userId']
                comment = i['content']
                lists.append([usr, usrID, comment])
            offset += 20
            print('前{}个已经爬取'.format(offset))
        except IndexError:
            break
        #print(wb_data)

    return lists

print(WYMusic_comments(452576361, headers=headers))