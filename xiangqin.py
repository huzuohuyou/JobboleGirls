__author__ = 'wuhailong 2016-12-16'
import requests
from bs4 import BeautifulSoup
import re
import codecs
def getGils(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    start_html=requests.get(url,headers = headers)
    Soup=BeautifulSoup(start_html.text,'lxml')
    gilslist=Soup.find_all(class_='p-tit')
    content=''
    for item in gilslist:
        hrefitem = BeautifulSoup(str(item),'lxml')
        if "【" in hrefitem.a.get_text():
            continue
        else:
            content +=hrefitem.a['href']+'\t'+hrefitem.a.get_text()+'\n'
        #print(hrefitem.a['href']+'\t'+hrefitem.a.get_text())
    return content

def getValue(content):

    #'出生年月','身高','所在城市','籍贯','职业','父母情况','是否是独生子女','收入描述','兴趣爱好','是否接受异地恋','打算几年内结婚','要几个小孩','最低要求是','特殊要求是','一句话'
    if '出生年月' in content \
    or '身高' in content \
    or '所在城市' in content \
    or '所在地' in content \
    or '籍贯' in content \
    or '职业' in content \
    or '父母情况' in content \
    or '是否是独生子女' in content \
    or '收入描述' in content \
    or '兴趣爱好' in content \
    or '是否接受异地恋' in content \
    or '打算几年内结婚' in content \
    or '要几个小孩' in content \
    or '最低要求是' in content \
    or '特殊要求是' in content \
    or '一句话' in content:
        if "：" in content:
            return str(content).split('：')[1].replace(' ','')
        elif ":" in content:
            return str(content).split(':')[1].replace(' ','')
    else:
        print(content)
        return None

def getDetail(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    start_html=requests.get(url,headers = headers)
    soup=BeautifulSoup(start_html.text,'lxml')
    detail=soup.find_all(class_='p-entry')
    soupdetail=BeautifulSoup(str(detail),'lxml')
    soupdetail.find_all('p')
    row=[]
    for item  in soupdetail.get_text().split('\n'):
        if None!=getValue(item):
            row.append(getValue(item))
    #print(row)
    #print(len(row))
    return row

def write_csv_file(path, head, data):
    import csv
    try:
        with open(path, 'w',newline='') as csv_file:
            #csv_file.write(codecs.BOM_UTF8)
            writer = csv.writer(csv_file, dialect='excel')
            if head is not None:
                print('head'+head)
                writer.writerow(head)
            for row in data:
                #print('row'+row)
                try:
                    writer.writerow(row)
                except:
                    continue
            print("Write a CSV file to path %s Successful." % path)
    except Exception as e:
        print("Write an CSV file to path: %s, Case: %s" % (path, e))

def getIntrest():
    import  csv
    csv_reader = csv.reader(open('details.csv'))
    content=''
    for row in csv_reader:
        content+=str(row[-2])+','+str(row[-3])
        #print(str(row[-2])+str(row[-3]))
    l=re.split(r'(?:,|;|；|！|，|、|。|（|）|\)|\(|\s)\s*', content)
    ret =  [str for str in l if str not in ['', ' ', None]]
    #l=l.remove('')
    #print(ret)
    fr = codecs.open ( 'items.txt', 'w', 'utf_8' )
    for item in ret:
        fr.write(item +'\n')
    fr.close()
    return ret

def fixValue(value):
    maininfo=['170','175','爱心','不抽烟','上进心']
    for item in maininfo:
        if item in maininfo:
            print('key'+item)
            return item
    return value

def getContent():
    i=1
    content=''
    while(i<=15):
        url="http://date.jobbole.com/page/{page}/".format(page=str(i))
        print(url)
        content+=getGils(url)
        i=i+1
    fr = codecs.open ( 'content.txt', 'w', 'utf_8' )
    fr.write(content)

def getDetails():
    fr = codecs.open ( 'content.txt', 'r' , 'utf-8')
    rows=[]
    index=0
    while 1:
        line = fr.readline()
        if not line:
            break
        print(line)
        row=getDetail(line.split('\t')[0])
        if len(row)==15:
            index=index+1
            print(index)
            rows.append(row)

    path='details.csv'
    header=['出生年与','身高','所在城市','籍贯','职业','父母情况','是否是独生子女','收入描述','兴趣爱好','是否接受异地恋','打算几年内结婚','要几个小孩','最低要求是','特殊要求是','一句话']
    write_csv_file(path,None,rows)

if __name__ == '__main__':
    #getContent()
    #getDetails()
    l= getIntrest()
    dictIntrest={}
    for i in l :
        #i=fixValue(i)
        if i not in dictIntrest.keys() and i!='':
            dictIntrest[i]=l.count(i)
    print (len(dictIntrest.keys()))
    print (dictIntrest)
