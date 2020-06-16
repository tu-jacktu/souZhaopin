# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class SouzhaopinPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',  # 数据库地址
            port=3306,  # 数据库端口
            db='py_db1',  # 数据库名
            user='root',  # 数据库用户名
            passwd='xxxx',  # 数据库密码
            charset='utf8',  # 编码方式
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        for data in item['detail']:  #遍历其中页面的多条职位
            insert_sql = """
                insert into job_info(
                sou_city_id,
                page_index,
                detail,
                updateDate,
                city_display,
                endDate,
                positionURL,
                salary,
                number,
                vipLevel,
                workingExp_name,
                company_name,
                company_type_name,
                company_url,
                createDate,
                jobName,
                eduLevel_name,
                eduLevel_code,
                emplType,
                timeState
                )value (%s,%s,%s,
                %s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s,%s,%s)
            """
            self.cursor.execute(insert_sql,
                (
                item['sou_city_id'],
                item['page_index'],
                str(data),
                data['updateDate'],
                data['city']['display'],
                data['endDate'],
                data['positionURL'],
                data['salary'],
                data['number'],
                data['vipLevel'],
                data['workingExp']['name'],
                data['company']['name'],
                data['company']['type']['name'],
                data['company']['url'],
                data['createDate'],
                data['jobName'],
                data['eduLevel']['name'],
                data['eduLevel']['code'],
                data['emplType'],
                data['timeState']
                ))
            # 提交sql语句
            self.connect.commit()
        return item  # 必须实现返回
