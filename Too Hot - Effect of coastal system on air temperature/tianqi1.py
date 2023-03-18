#url: http://www.weather.com.cn/
#采用的库:request-html

from requests_html import HTMLSession

url= "http://www.weather.com.cn/"
#设置代理
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.36"}
#采用cookies
cookies = {"Cookie": "Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1647089595; userNewsPort0=1; f_city=%E6%88%90%E9%83%BD%7C101270101%7C; Hm_lvt_2d6746724599c946d9b4734941e9f90c=1647089611; Hm_lpvt_2d6746724599c946d9b4734941e9f90c=1647089611; defaultCty=101270101; defaultCtyName=%u6210%u90FD; zs=101270101%7C%7C%7Cyd-uv; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1647090441"}
def data_request(url):
    session = HTMLSession()
    reponse = session.request(get, url, headers=headers, cookies=cookies)
    if(reponse.status_code<200 or reponse.status_code>300):
        print("访问失败"+ reponse.status_code)
        
    reponse.encoding="utf-8"
    content_text = reponse.text#获取所有页面文本
    content_meda = reponse.content#获取所有媒体内容
    url_list_abs = reponse.html.absolute_links()#获取所有绝对链接
    url_list_xiang = reponse.html.links()#获取所有相对链接
    
    return content_text, content_meda, url_list_abs, url_list_xiang


def deal_urllist(url_list_xiang):
    url_list_part2 = list()
    root = "http://www.weather.com.cn/"
    for url in url_list_xiang:
        url= url +root
        url_list_part2.append(url)
    return url_list_part2

def deal_mian_content:
    
def deal_main_media:
    
def smell_links(url_list):
    root = "http://www.weather.com.cn/"
    for url in url_list:
        if root not in url:
            continue;
    data_request(url)
    
if __name__=="__main__":
        
    
    
