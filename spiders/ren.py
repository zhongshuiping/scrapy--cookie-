import scrapy

class RenrenSpider(scrapy.Spider):

    name = 'renren'
    domain = ['renren.com']
    start_urls = [
         "http://www.renren.com/PLogin.do"
    ]

    def parse(self,response):

        yield scrapy.FormRequest.from_response(
             response,
             formdata = {"email" : "mr_mao_hacker@163.com", "password" : "alarmchime"},
             callback = self.parse_page
        )

    def parse_page(self,response):
        print ("=========1===" + response.url)
        #with open("mao.html", "w") as filename:
        #    filename.write(response.body)
        url = "http://www.renren.com/422167102/profile"
        yield scrapy.Request(url, callback = self.parse_newpage)

    def parse_newpage(self,response):
        print ("===========2====" + response.url)
        with open("xiao.html", "wb") as filename:
            filename.write(response.body)
