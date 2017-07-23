#coding=utf-8
from BaseTools import *
class Spinder:
    opener = '0'
    cookie = '0'
    handler = '0'
    dictListURL = "https://test.yitalicai.com/system/PreListDict.jsp"
    loginURL = 'https://test.yitalicai.com/Login.do'
    loginName = ''
    loginPSW = base64.b64encode("");
    def __init__(self):
        self.cookie = cookielib.CookieJar();
        self.handler = urllib2.HTTPCookieProcessor(self.cookie)
        self.opener =urllib2.build_opener(self.handler)

    def login(self):
        self.opener.addheaders=[
            ("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"),\
            ("Accept-Encoding","gzip, deflate, br"),\
            ("Accept-Language","zh-CN,zh;q=0.8"),\
            ("Connection","keep-alive"),\
            ("Content-Type","application/x-www-form-urlencoded"),\
            ("Host","test.yitalicai.com"),\
            ("Origin","https://test.yitalicai.com"),\
            ("Referer","https://test.yitalicai.com/Login.do"),\
            ("Upgrade-Insecure-Requests","1"),\
            ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 ")]
        data = "usercode="+ self.loginName +"&password="+ self.loginPSW +"&RetURL=&isMacAddress=0&MACAddr=&domain=&powersys="
        content = self.opener.open(self.loginURL, urllib.quote(data)).read()
        compressedstream = StringIO.StringIO(content)
        print(content)
        gzipper = gzip.GzipFile(fileobj=compressedstream)
        content = gzipper.read()
        print(content)

    def dictList(self):
        self.opener.addheaders=[
            ("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"),\
            ("Accept-Encoding","gzip, deflate, sdch, br"),\
            ("Accept-Language","zh-CN,zh;q=0.8"),\
            ("Connection","keep-alive"),\
            ("Host","test.yitalicai.com"),\
            ("Referer","https://test.yitalicai.com/system/ListDictionary.jsp?HeadHidden=1&FooterHidden=1&LeftHidden=1"),\
            ("Upgrade-Insecure-Requests","1"),\
            ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")]
        content = self.opener.open(self.dictListURL).read()
        compressedstream = StringIO.StringIO(content)
        print(content)
        gzipper = gzip.GzipFile(fileobj=compressedstream)
        content = gzipper.read()
        print(content)
