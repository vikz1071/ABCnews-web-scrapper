#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 22:19:48 2021

@author: vigneshwar
"""


   

import requests
from bs4 import BeautifulSoup

class ABCnews:
    
    BASE_URL = 'https://www.abc.net.au/news/2021-06-04/sa-icac-issues-public-statement/100192136'
    
    def get_html(url):
        
        ABCnews = requests.get(url)
        html = BeautifulSoup(ABCnews.text,'html.parser')
        
        return html
    
    
    def article_content_lis(html):
        
        if html:
            content = html.find('div', id = 'body')
            content_p  = content.find_all('div')[1]
            print(content_p)
            return content_p.find_all('p')
        return None
    
    """
        
    def article_content(html):
        para = ABCnews.article_content_lis(html) 
        nav = para.find('p',class_='1HzXw')
        print(nav)
        
   """     
"""
        lis = DailyNation.get_topics_lis()
        topics = []
        for li in lis:
            topics.append(li.find('a').text.lower())
        return topics
        """
"""
    def get_text():
        lis  = ABCnews.article_title()
        title = []
        for h1 in lis:
            title.append(h1.text.lower())
        return title
        
"""
       
"""  
    def get_topics_lis():
        html = Washingtonpost.get_html(Washingtonpost.baseurl)
        if html:
            nav = html.find('div',class_="relative side-nav")           
            topics_ul = nav.find_all('div', class_="dib flex font--subhead white hover-bg-black relative bold")
            return topics_ul.find_all('li')
        return none
"""   
   
if __name__ == '__main__':
    
    url = input('Enter ABC news URL:')
    ABCnews_html = ABCnews.get_html(url)
    lis = ABCnews.article_content_lis(ABCnews_html)
    c = ABCnews.article_content(ABCnews_html)
    print(c)
   ## ABCnews_title_html = ABCnews.article_title(ABCnews_html)
    
  
    
    
   ## ABCnews_title = ABCnews.get_text()

