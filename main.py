from main_program.spiders.spiders import all_spider
from main_program import data_op, conf
import pandas
import time
# 使用类的时候必须要先实例化
initize = all_spider()
spider_list = initize.WYMusic_list
spider_comments = initize.WYMusic_comments
spider_usr = initize.WYMusic_user
target_id = '2722492267'
times = 0 
lists = []

names = ['BooM', 'AfterJourney', 'Bridge']
singer = conf.singer
print(singer.values())

BooM = [523251474, 480994369, 511920317, 452592005, 554244546, 470775529, 477933820, 526904664, 452603679, 546281866, 523248470, 470774677, 470776167, 460889779, 526468223, 528270074, 452593605, 470775762, 470774886, 452593201, 452593556, 470776062, 452603876, 471006836, 452592797, 452576361, 452592962, 452575844, 452592692, 547012777, 547743893, 499793093, 497745124, 497755144, 502925959, 501467097, 509704100, 499793098, 502925962, 494645234, 501467091, 516358552]
BooM_comments = []
for id in BooM:
    time.sleep(10)
    print('正在抓取ID为{}的歌曲。'.format(id))
    lists = spider_comments(id, headers=conf.headers, proxies=conf.get_proxy())
    BooM_comments.extend(lists)
'''
while True:
    htmls = conf.danmu_html.format(times, target_id)
    #time.sleep(5)
    try: 
        a = spider(url = htmls, headers = conf.headers)
        print('{} has been crawled'.format(times))
        lists.extend(a)
    except NameError:
        break
    times += 30
'''
'''
    a = spider(url = htmls, headers = conf.headers)

    htmls = conf.danmu_html.format(times, target_id)
    a = spider(url = htmls, headers = conf.headers)
    lists.extend(a)
'''
data = pandas.DataFrame(BooM_comments, columns=['usr', 'usrID', 'comment'])
data.to_csv('BooM_comments.csv', index=False, encoding="utf-8")
