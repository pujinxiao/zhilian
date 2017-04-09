# -*- coding:utf-8 -*-
def get_start_url():
    '''
    得到不同城市的起始链接
    return:是包含不同城市的起始url
    '''
    # 先主要爬主要城市，看不同需求，也可以爬全国，只要把智联的候选地点全部抓取下来即可

    place_name = ['北京','上海', '广州', '深圳', '天津', '武汉', '西安', '成都', '大连', '长春', '沈阳', '南京', '济南', '青岛',
                   '杭州', '苏州', '无锡', '宁波', '重庆', '郑州', '长沙', '福州', '厦门', '哈尔滨', '石家庄', '合肥', '惠州']
    job_name = ['数据分析', 'php', '大数据', 'java', 'UI', 'IOS', '安卓', 'C++', 'python', '前端', '.net', '测试', '产品经理', '网络营销',
                '嵌入式', '项目经理', 'VR', 'AR']

    total_urls = []
    for keyword in job_name:
        list_urls = []
        for i in place_name:
            url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=' + str(i) + '&kw=' + keyword
            list_urls.append(url)
        total_urls.append((keyword, list_urls))
    return total_urls