__author__ = 'jishu12'
#coding:utf-8
import urllib
import http.cookiejar
import ssl
import requests
from bs4 import BeautifulSoup
import re
import codecs
'''
作者：吴海龙
OSC乱弹抢沙发
1.使用fiddler进行数据抓包获取header及cookie信息
2.使用python urllib https进行发送数据
'''

def qiangshafa(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    #url = "https://my.oschina.net/action/blog/add_comment?blog=797134"
    postdata =urllib.parse.urlencode({
    "content":"抢沙发大作战开始！"
    }).encode('utf-8')
    header = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Origin": "https://my.oschina.net",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer":"https://my.oschina.net/xxiaobian/blog/844061?p=3&temp=1487827633938",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
    "Cookie": "_user_behavior_=c3e70246-ed88-41bf-9ab2-b3201f4dab89; Hm_lvt_f0bcd6b2e12cfb80bab5d6f851cd41ad=1477208617,1477208642,1477272219,1477357544; bdshare_firstime=1482837433584; oscid=x7LWUaBbNqLsKSvRMKPgsAZXGtPXHWWnjmAiwk9XuenLSmi5rfyTZTKKpAX8c7gPIjtylJcPGXlLICY80fws18XIHMXrHE284UEO363Q8YL4q2%2B%2BXKKbwf8IvHMKDOtNwzUlwQxCxep9VGxPcaB%2Fl2wfT58Y4thGfG7SixLLmvM%3D; Hm_lvt_a411c4d1664dd70048ee98afe7b28f0b=1487574213,1487642093,1487758057,1487821660; Hm_lpvt_a411c4d1664dd70048ee98afe7b28f0b=1487822430"
    }
    req = urllib.request.Request(url,postdata,header)
    print(urllib.request.urlopen(req).read().decode('utf-8'))
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    r = opener.open(req)
    print(r.read().decode('utf-8'))

flag=False
def hasnews(preid):
    try:
        global flag
        ssl._create_default_https_context = ssl._create_unverified_context
        import http.client,datetime
        conn = http.client.HTTPSConnection('my.oschina.net')
        conn.request("GET", "/xxiaobian/blog")
        sourp=BeautifulSoup(conn.getresponse().read(),'lxml')
        gilslist=sourp.find_all(class_='time')
        import time
        id=str(sourp.find_all(class_='blog-title',limit=1)[0]['href']).split('/')[-1]
        if preid==None:
            return id
        if id!=str(preid):
            return str(sourp.find_all(class_='blog-title',limit=1)[0]['href'])
        else:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+str(gilslist[0].get_text().strip().replace('发布','').strip()))
            if flag:
                print('sleep 2 second ...')
                time.sleep(2)
            else :
                flag=True
                date_str=datetime.datetime.now().strftime("%Y-%m-%d 23:40:50")
                endtime=datetime.datetime.strptime(date_str,"%Y-%m-%d %H:%M:%S")
                now=datetime.datetime.now()
                print('endtime:{end} now:{now}'.format(end=endtime,now=now))
                interval=(endtime-now)
                sec = interval.days*24*3600 + interval.seconds
                print('need sleep {second} second ...'.format(second=abs(sec)))
                time.sleep(sec)
            return None
            # hasnews()
            # print(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))
    except ValueError as e:
        sendEmail('发生异常了！'+str(e))
        fr=open('log.txt')
        fr.write(str(e))
        fr.close()
       # sourp.find_all(class_='blog-title',limit=1)['href']



def sendEmail(message):
    from email.mime.text import MIMEText
    msg = MIMEText(message, 'plain', 'utf-8')
    from_addr = '13126506430@163.com'
    password = 'whl05043016'
    # 输入收件人地址:
    to_addr = '13126506430@163.com'
    # 输入SMTP服务器地址:
    smtp_server = 'smtp.163.com'

    import smtplib
    server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

class log():
    def __init__(self,id):
        self.id=id
id=None
if __name__ == '__main__':
    global id
    import http.client,datetime, pickle,os
    if os.path.exists('dump.txt'):
        f = open('dump.txt', 'rb')
        logid = pickle.load(f)
        preid=logid.id
        f.close()
        print('preid is '+str(preid))
    else:
        preid=None
    while id==None:
        id = hasnews(preid)
    f = open('dump.txt', 'wb')
    pickle.dump(log(id), f)
    f.close()
    url="https://my.oschina.net/action/blog/add_comment?blog={id}".format(id=id)
    #https://my.oschina.net/action/blog/add_comment?blog=797134"
    #https://my.oschina.net/xxiaobian/blog/844061
    qiangshafa(url)
    sendEmail('over \t'+url+'\t'+str(datetime.datetime.now()))