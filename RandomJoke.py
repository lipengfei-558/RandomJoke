#-*- coding:utf-8 -*-
#代码详解：http://www.lookfor404.com/简易python爬虫-爬取冷笑话/
__author__ = '李鹏飞'
import urllib2
import re
 
class randomJoke:
 
    #初始化方法
    def __init__(self):
        self.url = 'http://lengxiaohua.com/random'
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        #初始化headers
        self.headers = { 'User-Agent' : self.user_agent }
        #笑话内容
        self.content = []
 
    #获取网页源代码
    def getSourceCode(self):
        try:
            request = urllib2.Request(url = self.url, headers=self.headers)
            response = urllib2.urlopen(request)
            sourceCode = response.read().decode('utf-8')
            return sourceCode
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"网络错误...",e.reason
                return None
 
    #获取笑话
    def setContent(self):
        sourceCode = self.getSourceCode()
        if not sourceCode:
            print('获取网页内容失败~！')
            quit()
        pattern = re.compile(' <pre.*?js="joke_summary".*?"first_char">(.*?)</span>(.*?)</pre>.*?class="user_info">.*?<a.*?>(.*?)</a>.*?(.*?)',re.S)
        items = re.findall(pattern,sourceCode)
        self.content = items
        print u"已经爬取源代码...正在解析源代码..."
 
    #返回笑话
    def getContent(self):
        return self.content
 
    #打印一则笑话
    def printAJoke(self,number):
        joke = self.content[number]
        print u"作者:%s" %(joke[2])
        print u'发表于:'+ joke[3]
        #item[0]和item[1]组成完整的内容
        print joke[0]+joke[1]
 
randomJoke = randomJoke()
notQuit = True
print u"你好，这里是随机笑话！"
print u"---------------------"
randomJoke.setContent()
print u"...."
print u"笑话池已经装满，20/20"
print u"输入1到20看笑话~~，输入quit退出,输入new重新爬取新笑话"
while notQuit:
    input = raw_input()
    if input == "quit" :
        print u"bye！"
        notQuit = False
    elif input == "new":
        randomJoke.setContent()  #重新抓取笑话内容
        print u"...."
        print u"笑话池已经装满，20/20"
        print u"输入1到20看笑话~~，输入quit退出,输入new重新爬取新笑话"
    else:
        input = int(input)
        randomJoke.printAJoke(input-1)
        print u"--------------------------------------------------"
        print u"输入1到20看笑话~~，输入quit退出,输入new重新爬取新笑话"
print u"您已经成功退出！"
quit()
