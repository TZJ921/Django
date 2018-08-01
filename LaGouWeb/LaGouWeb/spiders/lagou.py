# -*- coding: utf-8 -*-
import json
from scrapy import FormRequest,Request
from LaGouWeb.items import LagouwebItem
from scrapy.spider import CrawlSpider


class LagouSpider(CrawlSpider):
    name = 'lagouSpider'
    url = "https://www.lagou.com"
    page = 1
    start_urls = ['https://www.lagou.com/jobs/list_python']
    headers = {
        "Referer":"https://www.lagou.com/jobs/list_python?px=default&city=%E5%8C%97%E4%BA%AC",
        "Cookie":' _ga=GA1.2.2084562135.1532247319;'
                 ' _gid=GA1.2.822511747.1532247319;'
                 ' user_trace_token=20180722161518-5ebca763-8d87-11e8-a2a0-525400f775ce;'
                 ' LGUID=20180722161518-5ebca9e7-8d87-11e8-a2a0-525400f775ce;'
                 ' showExpriedIndex=1; showExpriedCompanyHome=1; '
                 'showExpriedMyPublish=1; hasDeliver=0;'
                 ' JSESSIONID=ABAAABAABEEAAJACD0B0F3C11961C9C396343F85A4152D7;'
                 ' Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532247319,1532344132,1532413333;'
                 ' _putrc=9A1DB13E3EB3CEFA123F89F2B170EADC; login=true;'
                 ' unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B74216;'
                 ' gate_login_token=29c9e7559201c4eb6637b184609f9afad64f406ae7e93575a2ff3d90f944ba6b;'
                 ' TG-TRACK-CODE=search_code; _gat=1;'
                 ' LGSID=20180724165540-577cc50b-8f1f-11e8-9ee6-5254005c3644;'
                 ' PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_python;'
                 ' PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_python%3Fpx%3Ddefault%26city%3D%25E5%258C%2597%25E4%25BA%25AC;'
                 ' LGRID=20180724165540-577cc67d-8f1f-11e8-9ee6-5254005c3644; '
                 'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532422540;'
                 ' index_location_city=%E5%8C%97%E4%BA%AC; SEARCH_ID=9382655db22b4bc58b6b7290ddb72b03'
    }

    def parse(self, response):
        with open('lagou.html','w') as f:
            f.write(response.text)
        print(response.headers.getlist('Set-Cookie'))
        formdata = {"kd": 'python',"pn":'1',"first":'true'}
        url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
        yield FormRequest(url,callback=self.parse_lagou,formdata=formdata,headers=self.headers)

    def parse_lagou(self,response):
        print(response.text)
        text = json.loads(response.text)
        res = []
        try:
            res = text["content"]["positionResult"]["result"]
        except:
            pass
        if len(res) > 0:
            for position in res:
                item = LagouwebItem()
                try:
                    item['title'] = position['positionName']
                    item['education'] = position['education']
                    item['company'] = position['companyFullName']
                    item['experience'] = position['workYear']
                    item['location'] = position['city']
                    item['salary'] = position['salary']
                except:
                    pass
                yield item

            self.page += 1
            url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
            formdata = {"kd":'python',"pn":str(self.page),"first":'false'}
            print('formdata: ',formdata)
            yield FormRequest(url,callback=self.parse_lagou,formdata=formdata,headers=self.headers)
        else:
            print("爬虫结束了！")

