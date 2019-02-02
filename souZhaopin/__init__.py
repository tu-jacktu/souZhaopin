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
        "&kw=JAVA"  # 搜索关键字
        "&kt=3"  # 未知,一般为3
        "&_v=0.66116581"  #未知,搜索可不带
        "&x-zp-page-request-id=fde9e51fa1184df196980acf843495df-1545741531977-479528"
        # 未知,搜索可不带"
    ][0]
print(initUrl.replace("{cityId}","658"))