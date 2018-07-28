import random
import requests
import json
# 腾讯视频弹幕网页
# 其中timestamp是指时间节点，从0开始，以30为一个单位，target_id是指该视频号码
danmu_html = "https://mfm.video.qq.com/danmu?otype=json&timestamp={}&target_id={}&count=800"


# 要分析的成员的代号以及所有可能出现的名字及昵称
dict = {
    'mmq':["孟美岐", "mmq", "Meng Mei Qi", "美支", "美皮", "毛毛球", "MMQ", "山支大哥", "美岐"],
    'ycy':["杨超越", "超越", "小越越", "村花", "ycy", "cy", "甲醇", "全村的希望"],
    'wxy':["吴宣仪", "Xuan Yi", "XY", "WXY", "wxy", "오선의", "五选一", "二仪", "宣仪", "海南富婆", "海南小仙女"],
    'yamy':["Yamy", "yamy", "亚米酱"],
    'daj':["段奥娟", "大娟", "胖娟", "娟妹", "娟", "daj"],
    'lzt':["李紫婷", "米米粒", "泰妹", "lzt", "LZT"],
    'zn':["张紫宁", "紫宁", "zn", "winnie"],
    'sunnee':["可米Sunnee", "sunnee", "可米"]
}

# headers
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

headers = {
        'User-Agent': random.choice(user_agents),
        'Cookie':'vjuids=cd894bfc.16376faa00f.0.88fbd85462712; _ntes_nnid=c2cbce8a3916c5c491ae038bcb3c7ad9,1526709526558; _ntes_nuid=c2cbce8a3916c5c491ae038bcb3c7ad9; __utma=94650624.301866754.1526783683.1526783683.1526783683.1; __utmz=94650624.1526783683.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; WM_TID=FW7j6LY3QKnDAD99R1BBuav%2FRj2Ypi7P; __f_=1526885804881; usertrack=ezq0plsFfOSDh8/zD0kPAg==; Path=/; __remember_me=true; Expires=Sun, 14-Jan-2018 13:07:08 GMT; _iuqxldmzr_=32; vjlast=1526709527.1528376065.11; vinfo_n_f_l_n3=3767cfeeff39be45.1.1.1528282565822.1528282806015.1528376353016; JSESSIONID-WYYY=wBOXldPr99ZFH%2BqGGfFW4MD0uo31mXNi4EC4IqQDKuabB6Y5VHZaYFGpQEB9D9TAWUDvv%2F%2B1kWnhlKiupgM6JbO%2B%2FJmwb2mfFCSYYDc9%2FcBb%2BDgjjgc84pHY8ePN5x7ERndOFu5xuHIivoHcZpiETptYy3R5uOpl269j%5Cxs%2FNxd%2BEQl%2B%3A1528623658863; MUSIC_U=fba52d7fed2592ea336ed5cbe7a51d0d57b0eb03c4691fdf67d1fe2178fc4638ba2965ae8b3c58210f0b8c648fc701e8af9e62a8590fd08a; __csrf=77e833df4fbd02980d937848a763d4c8',  
        'Host':'music.163.com',  
        'Referer':'http://music.163.com/',  
        'Upgrade-Insecure-Requests':'1',  
        #'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'  
    }

def get_proxy():
    r = requests.get('http://127.0.0.1:8000/?types=0&count=10&country=国内')
    i = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    num = random.choice(i)
    ip_ports = json.loads(r.text)
    ip = ip_ports[num][0]
    port = ip_ports[num][1]
    proxies={
        'http':'http://{}:{}'.format(ip,port),
        'https':'http://{}:{}'.format(ip,port)
    }
    #r = requests.get('http://ip.chinaz.com/',proxies=proxies)
    #r.encoding='utf-8'
    return proxies
print(get_proxy())

print(headers)

singer = {
    'BooM':"http://music.163.com/artist?id=12065096",
    'AfterJourney':"http://music.163.com/artist?id=12127564",
    'Bridge':"http://music.163.com/artist?id=12493701",
}
