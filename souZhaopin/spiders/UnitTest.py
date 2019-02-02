# -*- coding : utf-8 -*-
testStr = ["abc"
          "bcd"
          "def"][0]
print(testStr)

testStr = """
"applyType":"1","updateDate":"2018-12-04 11:45:31","refreshMulscore":"0.0","g_sort":"sort-ps-score-pqks-ranking",
"city":{"display":"杭州-拱墅区","items":[{"code":"653","name":"杭州"},{"code":"2236","name":"拱墅区"}]},"endDate":"2019-01-04 11:56:38","saleType":0,"showLicence":0,"positionURL":"https://jobs.zhaopin.com/265788688250004.htm","g_weight":0,"industry":"200300","salary":"8K-10K","welfare":["五险一金","绩效奖金","餐补","定期体检"],"SOU_POSITION_ID":"CC265788688J90250004000","geo":{"lon":"","lat":""},"duplicated":0,"score":100,"number":"CC265788688J90250004000","vipLevel":1002,"recruitCount":3,
"workingExp":{"code":"103","name":"1-3年"},"tagIntHighend":0,"companyScore":0,"company":{"number":"CZ265788680","size":{"code":"2","name":"20-99人"},"name":"杭州政智经济信息咨询有限公司","type":{"code":"5","name":"民营"},"url":"https://company.zhaopin.com/CZ265788680.htm"},"jobType":{"display":"软件/互联网开发/系统集成,软件工程师","items":[{"code":"160000","name":"软件/互联网开发/系统集成"},{"code":"45","name":"软件工程师"}]},"seo":"0","g_query":"query-ps-score-3","createDate":"2018-11-06 11:56:38","resumeCount":0,"jobName":"软件开发人员","manualScore":"0.0","eduLevel":{"code":"-1","name":"不限"},
"companyLogo":"http://company.zhaopin.com/CompanyLogo/20170924/B0C9792B85044D2AA511634623A03343.jpg","futureJob":false,"emplType":"全职","g_source":"source-solr-position","recentAndTotal":{"applyTotal":"0","exposureTotal":"0","clickTotal":"0","exposureRecent":"0","clickRecent":"0","applyRecent":"0"},"tags":[],"positionLabel":"{\"qualifications\":null,\"chatWindow\":0,\"role\":null,\"companyTag\":null,\"level\":null,\"refreshLevel\":0,\"skill\":null,\"joblight\":[\"五险一金\",\"绩效奖金\",\"餐补\",\"定期体检\"]}","expandCount":0,"jobTag":{"searchTag":"五险一金,绩效奖金,餐补,定期体检"},"feedbackRation":0,"interview":0,"selected":false,"applied":false,"collected":false,"isShow":false,"timeState":"招聘中","rate":""},

"""
print(len(testStr))