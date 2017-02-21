from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)

def cut(l):
    import jieba
    import  codecs
    #jieba.load_userdict("userdict.txt")
    fr = codecs.open ( 'words.txt', 'w', 'utf_8' )
    for item in l:
        seg_list=jieba.cut(str(item),cut_all=False)
        words =''
        for word in seg_list:
            words+= word+'\t'
        fr.write(words+'\n')
    fr.close()

def getGroups():
    from apriori import getRules
    rules=getRules()
    groups=[]
    for itemset in rules:
        tempset=[]
        for item in itemset[:-1]:
            #print(str for str in item)
            tempset.extend([str for str in item ])
        groups.append(tempset)
    return groups

@app.route('/')
def intrest():
    import xiangqin as xq
    import jieba

    groups = getGroups()
    dictIntrest={}
    l=xq.getIntrest()
    print(groups)
    log=[]
    for group in groups:
        one=[]
        for i in l :
            if not [False for value in group if value not in list(jieba.cut(i))] :
                one.append(i)
                if i not in dictIntrest.keys():
                    dictIntrest[i]=1
                else:
                    dictIntrest[i]=int(dictIntrest[i])+1
            else:
                pass
        log.append(one)
                #print('group:'+str(list(group))+'\t'+str(list(jieba.cut(i))))

    print(item for item in log)
    dictcopy={}
    for key in dictIntrest.keys():
        if int(dictIntrest[key])==1:
            pass
        else:
            dictcopy[key]=int(dictIntrest[key])*10
    return  render_template('echart.html',entries = dictcopy)

if __name__ == '__main__':
    app.run()
