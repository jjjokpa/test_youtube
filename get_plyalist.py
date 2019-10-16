# -*- coding: utf-8 -*- 
from selenium import webdriver 
import pandas as pd 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

import test_firebase

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver = webdriver.Chrome('chromedriver', chrome_options=options)

while(True):
    keywords = test_firebase.db.collection(u'keywords').where(u'flag', u'==', 0).stream()

    for keyword in keywords:

        dict_keyword = keyword.to_dict()
        id_keyword = keyword.id

        key = dict_keyword.get("keyword")

        key.replace(" ","+")

        driver.get("https://www.youtube.com/results?search_query="+key+"&sp=EgIQAQ%253D%253D")
        driver.implicitly_wait(3)

        user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
        links = []
        count = 0
        for i in user_data:
            add_flg = True      #When True add links
            link = i.get_attribute('href')

            saved = test_firebase.db.collection(u'links').where(u'link', u'==', link).stream()

            for sv in saved:
                if(len(sv.to_dict()) > 0):
                    add_flg = False     # already exists link

            if (add_flg):
                data = {
                            "keyword": key,
                            "link": link,
                            "flag": 0
                        }
                print(data)
                doc_ref = test_firebase.db.collection(u'links').add(data)
                count += 1
            
            if count == 2 :
                test_firebase.db.collection("keywords").document(id_keyword).update({"flag": 1})    #keyword flag 0 -> 1
                break

# print("Complete!!!")
# driver.quit()