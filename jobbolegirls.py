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
    content=xq.getIntrest()

    l=re.split(r'(?:,|;|；|！|，|、|。|\s)\s*', content)
    dictIntrest={}
    for i in l :
        #i=fixValue(i)
        if i not in dictIntrest.keys() and i!='':
            dictIntrest[i]=l.count(i)
    #print (len(dictIntrest.keys()))
    print (dictIntrest)
    return  render_template('echart.html',entries = dictIntrest)

if __name__ == '__main__':
    app.run()
