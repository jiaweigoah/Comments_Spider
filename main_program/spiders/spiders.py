import requests
import simplejson
import re
from bs4 import BeautifulSoup
import time

class all_spider(object):

    def __init___(self):
        pass

    #获取腾讯视频弹幕的爬虫
    def tencent_danmu(self, url, headers, proxies = None):
        wb_data = requests.get(url, headers = headers, proxies=proxies).text
        js_dict = simplejson.loads(wb_data, strict=False)
        data = js_dict['comments']
        if data == []:
            raise NameError
        all_comments = []
        for i in data:
            # content是弹幕内容， upcount是指赞的人数，opername是指用户名, headurl是指头像网址,timepoint是发表的相对时间
            dicts = {}
            timepoint = i['timepoint']
            comment = i['content']
            upcount = i["upcount"]
            usr_name = i['opername']
            headurl = i['headurl']
            lists = [comment, upcount, usr_name, headurl, timepoint]
            all_comments.append(lists)
        return all_comments

    #获取评论的爬虫
    def get_comments(self):
        pass

    def WYMusic_list(self, url, headers, proxies = None):
        lists = []
        wb_data = requests.get(url, headers = headers, proxies=proxies).text
        soup = BeautifulSoup(wb_data, "lxml")
        datas = soup.find('textarea').text
        js_dict = simplejson.loads(datas, strict = False)
        for i in js_dict:
            lists.append(i["id"])
        return lists

    def WYMusic_comments(self, url, headers, proxies = None):
        lists = []
        offset = 0
        while True:
            time.sleep(1.3)
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
        
    def WYMusic_user(self, url, headers, proxies = None):
        html = 'music.163.com/user/home?id={}'.format(url)
        wb_data = requests.get(html, headers = headers, proxies = proxies).text
        region = re.search(r'所在地区：[\u4e00-\u9fa5]* - [\u4e00-\u9fa5]*', wb_data).group()
        des = re.search(r'"description": "[\u4e00-\u9fa5|\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b]*。', wb_data).group()
        return [region, des]
