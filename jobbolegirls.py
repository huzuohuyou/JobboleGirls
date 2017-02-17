from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)




@app.route('/')
def intrest():
    import re
    import xiangqin as xq
    import jieba
    #jieba.load_userdict("userdict.txt")
    content=xq.getIntrest()

    l=re.split(r'(?:,|;|；|！|，|、|。|\s)\s*', content)
    l.remove('')
    dictIntrest={}
    print('len'+str(len(l)))
    for i in l :
        group=[]
        for j in l:
            samecount=0
            diffcount=0
            if len(i)<=2:
                for x in i:
                    if x in j :
                        samecount=samecount+1
                    if samecount==2:
                        if i not in dictIntrest.keys():
                            dictIntrest[i]=1
                        else:
                            dictIntrest[i]=int(dictIntrest[i])+1
                        l.remove(j)
                        group.append(j)
                        break
            elif len(i)>2:
                for x in i:
                    if x in j :
                        samecount=samecount+1
                    else:
                        diffcount=diffcount+1
                if samecount>diffcount:
                    if i not in dictIntrest.keys():
                        dictIntrest[i]=1
                    else:
                        dictIntrest[i]=int(dictIntrest[i])+1
                    l.remove(j)
                    group.append(j)
        print('*******group:'+str(group))
        # seg_list=jieba.cut(str(i), cut_all=False)
        # for word in seg_list:
        #     if word not in dictIntrest.keys():
        #         dictIntrest[word]=1
        #     else:
        #         dictIntrest[word]=int(dictIntrest[word])+1
    #print (len(dictIntrest.keys()))
    dictcopy={}
    for key in dictIntrest.keys():
        if int(dictIntrest[key])==1:
            pass
        else:
            dictcopy[key]=int(dictIntrest[key])*10
    return  render_template('echart.html',entries = dictcopy)

if __name__ == '__main__':
    app.run()
