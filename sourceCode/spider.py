from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from lxml import etree
import pandas as pd

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)

try:
    browser.get('http://sou.chinanews.com.cn/search.do')
    input = browser.find_element_by_id('q')  # 查找节点--通过id
    input.send_keys('电信诈骗')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 5)  # 等5s待网页加载完成
    browser.find_element_by_xpath(
        '/html/body/table/tbody/tr/td[2]/table/tbody/tr/td[4]/div/p[1]/font/a').click()  # 按相关度排序
    browser.find_element_by_xpath(
        '/html/body/table/tbody/tr/td[2]/table/tbody/tr/td[4]/div/p[2]/font/a[6]').click()  # 获取最近一年的新闻
    record = []

    for pageCount in range(0, 50):
        content = etree.HTML(browser.page_source)

        links = content.xpath('//*[@class="news_title"]/a/@href')

        for path in links:
            browser.get(path)
            temp = etree.HTML(browser.page_source).xpath('//*[@class="left_zw"]/p/text()')

            news = ""
            for msg in temp:
                news += msg
            else:
                print(news)
                record.append(news)  # 将该新闻记录，返回父界面
                browser.back()
        else:
            browser.find_element_by_xpath('//*[@id="pagediv"]/a[9]').click()  # 翻页

finally:
    browser.close()

result = pd.DataFrame(data=record)
result.to_csv('诈骗新闻.csv')
