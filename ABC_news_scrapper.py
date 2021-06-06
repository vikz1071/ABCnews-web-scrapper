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
    
    
    def summary(html):
        
        if html:
            content = html.find('div', class_="YDnEu OK4xB")
            for p in content.find_all('p', class_="_1HzXw"):
                summary = content.p.string
            print ('\n Overview - First paragraph in this article:', summary)
            
    def get_title(html):
        if html:
            title_content = html.find('div', class_="_3ANn5")
            for h1 in title_content:
                title = title_content.h1.string
                print('\nThe title of this article is:',title)
                break
        
    def get_author_name(html):
        if html:
            author_name = html.find('span',class_="W-g-R _14nkQ _3BwtN _2eB4R _3qdyT")
            for a in author_name.find_all('a',class_="_2msBb vOtE5 _1wNLk _3i4V4 _1tAZ1"):
                author = author_name.a.text
                print('\nAuthored by:',author)
                break
            
 

if __name__ == '__main__':
    
    url = input('Enter ABC news URL:')
    ABCnews_html = ABCnews.get_html(url)
    ABCnews.get_title(ABCnews_html)
    ABCnews.summary(ABCnews_html)
    ABCnews.get_author_name(ABCnews_html)
    
