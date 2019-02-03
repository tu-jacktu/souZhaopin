# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy import cmdline

from souZhaopin.items import SouzhaopinItem

class ZhaopinSpider(scrapy.Spider):
    name = "souZhaopin"
    allowed_domains = ['https://sou.zhaopin.com/']
    #各个城市职位下标
    cityIndex = {
                 "530":0,
                 "538":0,
                 "763":0,
                 "765":0,
                 "653":0,
                 "691":0
                }
    initUrl = [         #初试url
        "https://fe-api.zhaopin.com/c/i/sou?"
        "start=0"  # 起始下标,第一页为0,第二页为90,类推
        "&pageSize=90"  # 页容量,默认90,最大100
        "&cityId={cityId}"  # 城市
        "&workExperience=-1"  # 工作经验
        "&education=-1"  # 学历
        "&companyType=-1"  # 公司类别
        "&employmentType=-1"  # 职业类别
        "&jobWelfareTag=-1"  # 工作福利标签
        "&kw=JAVA "  # 搜索关键字
        "&kt=3"  # 未知,一般为3
        "&_v=0.66116581"  #未知,搜索可不带
        "&x-zp-page-request-id=fde9e51fa1184df196980acf843495df-1545741531977-479528"
        # 未知,搜索可不带"
    ][0]
    def start_requests(self):
        cityArr = [#此处有问题
                   # 并不会一个城市执行完,在执行下个城市
                   #startIndex 得控制,不然会导致数据混乱!
                    "530",  #北京
                    "538",  #上海
                    # "763",  #广州
                    # "765",  #深圳
                    # "653",  #杭州
                    # "691"   #南昌
                   ]
        # 逐个城市抓取
        for cityID in cityArr:
            # 此处会一次性跑完,赋值操作只有最后一次有效 !
            # 抓取多个城市
            request = scrapy.FormRequest(url=self.initUrl.replace("{cityId}",cityID),callback=self.parse,meta={'sou_city_id':cityID})
            yield request

    def parse(self, response):

        sou_city_id = response.meta['sou_city_id']

        print("城市代码:"+sou_city_id,"起始下标:"+str(self.cityIndex[str(sou_city_id)]))

        jobBytes = response.body
        jobJson = json.loads(jobBytes)
        sumCount = jobJson['data']['numFound']
        if len(jobJson['data']['results']) > 0 :
            cityCode = int(sou_city_id)
        else:
            cityCode = 0

        item = SouzhaopinItem()
        #此处在控制台打印大量json
        print("sumCount:"+str(sumCount),"startIndex:"+ str(self.cityIndex[str(cityCode)]))
        if sumCount <= (self.cityIndex[str(cityCode)]):
            item['detail'] = jobJson['data']['results']
        else:
            item['detail'] = jobJson['data']['results'][0:(sumCount-(self.cityIndex[str(cityCode)]))]
        print('尝试打印详情:',item['detail'])

        item['sou_city_id'] = cityCode
        # cityCode 为 0,会在此处停止
        item['page_index'] = self.cityIndex[str(cityCode)]//90 +1

        print('响应总数:',sumCount)
        print('当前页数:',item['page_index'])
        #把数据交给 pipline处理,进行保存
        yield item

        #进行翻页,抓取下一页数据
        if self.cityIndex[str(cityCode)] <= sumCount:
            self.cityIndex[str(cityCode)] += 90    #下一页起始下标
            next_page = self.initUrl.replace("start=0","start="+str(self.cityIndex[str(cityCode)]))
            next_page = next_page.replace("{cityId}",sou_city_id)
            meta= {'sou_city_id':sou_city_id}
            yield scrapy.Request(next_page,callback=self.parse,dont_filter=True,meta=meta)
        else:
            print("超出sumCount,页条数:",len(jobJson['data']['results']))

cmdline.execute("scrapy crawl souZhaopin".split())




