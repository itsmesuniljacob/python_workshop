import lxml
import requests
import time

while True:
    page=requests.get('https://sports.ndtv.com/cricket/live-scorecard/australia-vs-west-indies-match-10-nottingham-auwi06062019186686')
    print(page)
    # tree=html.fromstring(page.text)
    # print(tree)
    # score=(tree.xpath('//div[@class="ckt-scr"]/text()')[0].lstrip()).rstrip()
    # sendscore(score)
    # print("%s sent at:%s "%(score,time.ctime()))
    # time.sleep(180)
