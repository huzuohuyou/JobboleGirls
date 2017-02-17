from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/intrest')
def intrest():
    import re
    import xiangqin as xq
    import jieba
    jieba.load_userdict("userdict.txt")
    content=xq.getIntrest()

    l=re.split(r'(?:,|;|；|！|，|、|。|\s)\s*', content)
    dictIntrest={}
    for i in l :
        seg_list=jieba.cut(str(i), cut_all=False)
        for word in seg_list:
            if word not in dictIntrest.keys():
                dictIntrest[word]=1
            else:
                dictIntrest[word]=int(dictIntrest[word])+1
    #print (len(dictIntrest.keys()))
    print (dictIntrest)
    return  render_template('echart.html',entries = dictIntrest)

if __name__ == '__main__':
    app.run()
