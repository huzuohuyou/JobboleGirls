__author__ = 'hailong'
'''
清除网易云音乐没有互粉的脚本
2017-02-26
wuhailong
'''
import urllib
import http.cookiejar
import ssl
import requests

def getNoMutal(params,enSecKey):
    print(params)
    print(enSecKey)
    data = {'params': str(params.strip()),
            'encSecKey':str(enSecKey.strip())}
    headers = {
    'POST http':'//music.163.com/weapi/user/getfollows/112272936?csrf_token=8c133a69f9cbf30a37e04ef55af6444f HTTP/1.1',
    'Host':'music.163.com',
    'Connection':' keep-alive',
    'Content-Length':' 512',
    'Originv http':'//music.163.com',
    'User-Agent':' Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',
    'Content-Type':' application/x-www-form-urlencoded',
    'Accept':' */*',
    'Referer':' http://music.163.com/user/follows?id=112272936',
    'Accept-Encoding':' gzip, deflate',
    'Accept-Language':' zh-CN,zh;q=0.8',
    'Cookie':' vjuids=48ee6d7e7.154708c8d48.0.e47a1ade127ee;' \
             ' _ntes_nnid=4e55d0db288b793b80c224f24edb7b40,1462177140046;' \
             ' _ntes_nuid=4e55d0db288b793b80c224f24edb7b40;' \
             ' __gads=ID=1360325d4099a926:' \
             'T=1462177139:' \
             'S=ALNI_MauUMT_xiutG499sdbI9AydEJT2Cg;' \
             ' NETEASE_WDA_UID=112272936#|#1450712246404; vjlast=1462177140.1483862690.21; ' \
             'vinfo_n_f_l_n3=769bcc6c42f59ff3.1.5.1462177140055.1470573193421.1483864116572; ' \
             'usertrack=c+5+hlie4kF0DnRnDIQzAg==; ' \
             'NTES_SESS=o_x36IW6dtLGoJJgfDcuC6PafzDOxT2kUYe3vCEBv0APxaw1xYbLveIipTTdOSYfgBMxa3jjmDaIM2vyLVlXMkuYVoqb' \
             'mraqXaoymEjmGLlknUjVkrY3SzoLnbZ9T61sFHdBCC8Fmeg8BgQj23Oy6XMOo0EnZXIFsHGlk0XW6t_zar.kqpN_oOQKL; S_INFO=1488083' \
             '416|0|2&90##|m13126506430; P_INFO=m13126506430@163.com|1488083416|0|other|00&99|bej&1488083396&mail_client#bej&n' \
             'ull#10#0#0|131430&1||13126506430@163.com; ANTICSRF=740c013b756c55e88df6123d564dac27; mail_psc_fingerprint=b1f9b6b3e6e' \
             'e9300a1f4b9c1c101bd8a; MUSIC_EMAIL_U=831b5c2232a641e00e7fed3e753184255053be85f4706fa6a830726bb445a259216e71553eda245df4' \
             '98575063635afb07242b041a0830c37955a739ab43dce1; BOX_DISABLE=true; JSESSIONID-WYYY=AMBqIKmDpB8GjnCUEfqUUp%2F8kHREoC2fY' \
             'oN%5Cpxl4jGGof%2Bf99w%2BK1XbhsMChuj5vKj%2BklJ7nbC2IP1C2laPVQZfp0PGSpnP9tc%5C9jYeki9IvE9pqJ%5C8Elydg0HiYmHmC%2Bg9O6D5' \
             'N%2FS2coRyf4tmHkysNUzuiK6Ap00OEss7kXASVhdxe%3A1488085221959; _iuqxldmzr_=32; playliststatus=visible; __remember_me=tru' \
             'e; MUSIC_U=f3a31190fec5ba90e00502f7ee1fa84b45a65483946f4a803f7e0bf5ec37bc9ff42796a14cec3362c44f363093f7adb38bafcdfe5ad2b' \
             '092; __csrf=8c133a69f9cbf30a37e04ef55af6444f; __utma=94650624.1809290275.1472952435.1479036584.1488084383.5; __utmb=' \
             '94650624.11.10.1488084383; __utmc=94650624; __utmz=94650624.1472952435.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic'}
    r = requests.post('http://music.163.com/weapi/user/getfollows/112272936?csrf_token=8c133a69f9cbf30a37e04ef55af6444f', data=data, headers=headers)
    print(r.text)
    import json
    data = json.loads(r.text)
    defollows=[]
    for follower in data['follow']:
        if follower['mutual']==False:
            defollows.append(follower['userId'])
    print('defollows:'+str(defollows))
    return defollows


def defollowed(defollows):
    data = {'params': 'c3S6p3BC4SU7idoGy4GpyJ/Az7LlSC0KmIcCfi9435TbeYMrSBtOqgFAqdIwoLecalp1RBLHOvfpuZ/RT3OfwSnJ/zs5TEW'
                       '+PqRWMrCHVcoqm4qFYK72Tm7aLSTCbATvINJ1JPBmDRFntv4TLRNaSA==',
            'encSecKey':'d577dd3f46d316483db1ea103e3e55d4d07cefb055135c4ae462c703c1d24061c6b0b67aa94c3eb10a52da65cc9321f6'
                        'd92b8e2b8635909ae4e0679e01f56a42dd4ff6f34375d0cfbd11cce355bdbfab385b3ea4834e777d17da4631a959b7e9f2'
                        'be23da3e908925bdb2500b5187a57dda16704b1fa9069cae85bdb02344d732'}
    header={
    #'POST http://music.163.com/weapi/user/delfollow/127028008?csrf_token=8c133a69f9cbf30a37e04ef55af6444f HTTP/1.1'
    'Host':' music.163.com',
    'Connection':' keep-alive',
    'Content-Length':' 438',
    'Origin':' http://music.163.com',
    'User-Agent':' Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',
    'Content-Type':' application/x-www-form-urlencoded',
    'Accept':' */*',
    'Referer':' http://music.163.com/user/home?id=127028008',
    'Accept-Encoding':' gzip, deflate',
    'Accept-Language':' zh-CN,zh;q=0.8',
    'Cookie':' vjuids=48ee6d7e7.154708c8d48.0.e47a1ade127ee; _ntes_nnid=4e55d0db288b793b80c224f24edb7b40,1462177140046; _ntes_nu'
            'id=4e55d0db288b793b80c224f24edb7b40; __gads=ID=1360325d4099a926:T=1462177139:S=ALNI_MauUMT_xiutG499sdbI9AydEJT2Cg; NETEASE'
            '_WDA_UID=112272936#|#1450712246404; vjlast=1462177140.1483862690.21; vinfo_n_f_l_n3=769bcc6c42f59ff3.1.5.1462177140055.147'
            '0573193421.1483864116572; usertrack=c+5+hlie4kF0DnRnDIQzAg==; NTES_SESS=o_x36IW6dtLGoJJgfDcuC6PafzDOxT2kUYe3vCEBv0APxaw1xYb'
            'LveIipTTdOSYfgBMxa3jjmDaIM2vyLVlXMkuYVoqbmraqXaoymEjmGLlknUjVkrY3SzoLnbZ9T61sFHdBCC8Fmeg8BgQj23Oy6XMOo0EnZXIFsHGlk0XW6t_zar'
            '.kqpN_oOQKL; S_INFO=1488083416|0|2&90##|m13126506430; P_INFO=m13126506430@163.com|1488083416|0|other|00&99|bej&1488083396&ma'
            'il_client#bej&null#10#0#0|131430&1||13126506430@163.com; ANTICSRF=740c013b756c55e88df6123d564dac27; mail_psc_fingerprint=b1f'
            '9b6b3e6ee9300a1f4b9c1c101bd8a; MUSIC_EMAIL_U=831b5c2232a641e00e7fed3e753184255053be85f4706fa6a830726bb445a259216e71553eda245'
            'df498575063635afb07242b041a0830c37955a739ab43dce1; BOX_DISABLE=true; playliststatus=visible; __remember_me=true; MUSIC_U=f3a'
            '31190fec5ba90e00502f7ee1fa84b45a65483946f4a803f7e0bf5ec37bc9ff42796a14cec3362c44f363093f7adb38bafcdfe5ad2b092; __csrf=8c133a'
            '69f9cbf30a37e04ef55af6444f; __utma=94650624.1809290275.1472952435.1479036584.1488084383.5; __utmb=94650624.13.10.1488084383;'
            ' __utmc=94650624; __utmz=94650624.1472952435.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; JSESSIONID-WYYY=tNIwJQl%2FDtm'
            'Oyn7rS0ZIu82eQA80%5CHsCXH5%2F%2F8K6R%5CBlNwvZQ1RITBNijrONoafWzflavuPO4Xe1PP6hGTdA%2Fs7aBmC3RwgNXVzh8Uexp2mVCZblsD%5Ci031fecV'
            'xX47CqIvWiRA8GSJwuMo%5CN2PutJCJidXuFVuJFUM39K9p52IEKPOh%3A1488086962026; _iuqxldmzr_=32'
    }
    for id in defollows:
        print('id:'+str(id))
        url='http://music.163.com/weapi/user/delfollow/{userid}?csrf_token=8c133a69f9cbf30a37e04ef55af6444f'.format(userid=str(id))
        print('url:'+url)
        r = requests.post(url,data=data,headers=header)
        print('defollow {userid} {result}'.format(userid=id,result=r.text))

def iphoneGetFollows():
    data = {
        'params': 'CB4023D1ACF58C9EE6B33349D681184E122C875ECD70224E982E718565F4404D70EA07CFDD15C819AD73921279CF784B44A443A4373C6B4F31FF99572206FE205CE4EE969AE34FE98D11C04E893164121B7'
                  '836A9FC45BE25F5636C71C1956A04AE3E16BD558512B41115E2B6C0EB00175D1C5C36DBB3D53BA9F50D4A636079086355354E27FC9AC8C394B3D9906A8AF9CCAEA1074983507BE352953D70FBBCE3FB084F'
                  '666271BC63DE164E3F7588A78E3B1FF65A13CB7540B4AF96C121887766A0D2CC40D6A7AF77D798A1BBD026A168838D9CE9FD921FDC60FC9A4465EAF1D86B2B9583DDCEA44F52F967CE35A7DACB8C3BCB246'
                  '5683B36E3F76A61C08202914C47E2259445135D7D7DCE8C1052D8FCB1CDC03883F413FC610D35F8DF86BFE6F0466A50F71BADA19E5E372DE67F780375FC58D539328D82E384F71D1A83D522C9426890C0234'
                  '5C6A14F2CC386FF99964967B0A1874E5B41E5C23316338EC6312AE359E8352EA786387CE1DB37ABE34502CEF97C7B8B7F7B5A62149988889BC762AEC0677701ECB361A9BD0F3AF77BB323769D5A78475CC69'
                  '59D82162ADAA503A7A7037B438EF645DAE467FD6B9EDF75FD5E19FD7BAF18F158787E0E3939D8FFC03D3CD9FBDA4AD93879B278FC6BA108023D64FF939298A109B29537EDB2C5E13B49BFEE3103D81B5DC3DC'
                  '504491906959F7359B2AFF8308A0E2C8C3AB9D015FE701BC107E415C35BAB94D7FCB7D42CCD0CA05E581B5EA4DC90FE876695ED366BC26E5AD8C85A7D5570D9028AA9E840E35D6A5AD0EE26A87449FA7BFE87'
                  '57B962D36B8175E189127135D4FA8712B1E7ABAC4D1FD617976E175B6462A15E4E2CC39D58E19584B8359B73F3BC45DCE3222'
           }
    headers = {
    'Host':' music.163.com',
    'Content-Type':'application/x-www-form-urlencoded',
    'Connection':'close',
    'Cookie':'MUSIC_U=f3a31190fec5ba90312fe67780e5f74988593b43d3514f0fcbc78e4b695628d26dc0e603cc30bbb16e9bb25d901b401431b299d667364ed3; os=iPhone OS; osver=10.2.1; appver=3.7.5; device'
             'Id=4c0a12f31bf22ffbeed5924b4bf7f597',
    'User-Agent':'网易云音乐 3.7.5 rv:694 (iPhone; iOS 10.2.1; zh_CN)',
    'Content-Length':' 1255',
    'Accept-Encoding':' gzip',
    'Connection':'close'
    }
    r = requests.post('http://music.163.com/eapi/user/getfollows/112272936', data=data, headers=headers)
    print(r.text.encode('utf-8').decode('gzip'))
    # rr=r.text.encode('utf-8')
   # bytes.decode(rr)


    # print(bytes.decode(rr))
    # import json
    # data = json.loads(r.text)
    # defollows=[]
    # for follower in data['follow']:
    #     if follower['mutual']==False:
    #         defollows.append(follower['userId'])
    # print('defollows:'+str(defollows))
    # return defollows

if __name__ == '__main__':
    defollows=[]#getNoMutal()

    file = open("params&key")
    index=0
    while 1:
        index=index+1
        line = file.readline()
        if not line:
            break
        else:
            params=line.split('#')[0]
            enSecKey=line.split('#')[1]
            defollows.extend(getNoMutal(params,enSecKey))
    defollowed(defollows)




   # iphoneGetFollows()