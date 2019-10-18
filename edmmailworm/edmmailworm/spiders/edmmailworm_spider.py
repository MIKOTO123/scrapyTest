from urllib.request import Request

import scrapy


def authentication_failed(response):
    # TODO: Check the contents of the response and return True if it failed
    # or False if it succeeded.
    if '","status":1,"' in response.text :
        return True
    else:
        return False




class EdmmailwormSpider(scrapy.spiders.Spider):
    name = "edm" #这个命令用于scrapy crawl edm 启动爬虫
    # allowed_domains = ["dmoz.org"]
    start_urls = [
        'https://www.bossedm.com/admin',
    ]
    edmpageno = 0;


    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
             formdata={'username': 'username', 'pwd': 'pwd'},
            callback=self.after_login
        )

    def after_login(self, response):
        if authentication_failed(response):
            self.logger.info("Login success")
            return self.runningwor(response)
        else:
            self.logger.info("Login failed")
            return

    def runningwor(self,response):
        smgui = response.url.split("/")
        sid = smgui[-1] #获取到sid
        self.logger.info("Login success");
        while self.edmpageno < 1000 :
            self.edmpageno= self.edmpageno + 1
            # self.logger.info(sid);
            # self.logger.info(str(self.edmpageno));
            yield  scrapy.Request(url="https://www.bossedm.com/Admin/Subscriber/groupMembers/list_id/19/pageno/"+ str(self.edmpageno) +"/sid/"+sid, callback=self.parseMailaddr)


    def parseMailaddr(self,response):
        mailboxs = response.xpath("//tr//td[2]/a/text()")
        for mailbox in mailboxs :
            # self.logger.info(response.body)
            # self.logger.info(mailbox.get())
            yield {"mailbox":mailbox.get()}





