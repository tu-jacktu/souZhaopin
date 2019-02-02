# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SouzhaopinItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    SOU_POSITION_ID = scrapy.Field()
    sou_city_id = scrapy.Field()
    page_index = scrapy.Field()
    detail = scrapy.Field()
    updateDate = scrapy.Field()
    city_display = scrapy.Field()
    endDate = scrapy.Field()
    positionURL = scrapy.Field()
    salary = scrapy.Field()
    number = scrapy.Field()
    vipLevel = scrapy.Field()
    workingExp_name = scrapy.Field()
    company_name = scrapy.Field()
    company_type_name = scrapy.Field()
    company_url = scrapy.Field()
    createDate = scrapy.Field()
    jobName = scrapy.Field()
    eduLevel_name = scrapy.Field()
    eduLevel_code = scrapy.Field()
    emplType = scrapy.Field()
    jobTag_searchTag = scrapy.Field()
    timeState = scrapy.Field()
    pass
