#!/usr/bin/env python
# coding: utf-8

# In[12]:


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service("C:\Drivers\chromedriver.exe"))


# In[ ]:





# In[ ]:





# In[13]:


driver.get("https://www.python.org")


# In[ ]:





# In[14]:


driver.title


# <input id="id-search-field" name="q" type="search" role="textbox" class="search_bar">

# ****click searchbar

# In[15]:


search_bar=driver.find_element(By.CLASS_NAME, "search-field")


# In[16]:


search_bar.clear()


# send keys to search bar

# In[17]:


search_bar.send_keys("update")

time.sleep(3)


# In[18]:


search_bar.send_keys(Keys.RETURN)


# PRINTS URL

# In[19]:


print(driver.current_url)


# In[20]:


driver.back()


# In[21]:


driver_2 = webdriver.Chrome(service=Service('C:\Drivers\chromedriver.exe'))


# TAB to new window

# In[22]:


driver.switch_to.new_window()


# In[23]:


print(driver.window_handles)


# In[ ]:





# In[24]:


webscrape=["https://www.python.org","https://youtube.com","https://www.twitter.com","https://www.wikipedia.com","https://www.google.com"]


# In[25]:


for i in range(4):
    driver_2.switch_to.new_window()
    driver_2.get(webscrape[i])
    print(webscrape[i])


# In[26]:


print(driver_2.window_handles)
driver_2.switch_to.window(driver_2.window_handles[2])


# In[27]:


search_bar2=driver_2.find_element(By.CLASS_NAME, "ytd-searchbox")


# In[ ]:





# In[28]:


dir(search_bar2)

search_bar2.click()
time.sleep(5)
print(search_bar2)


inputElem = driver_2.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")



inputElem.send_keys('election')


inputElem = driver_2.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button/yt-icon")
inputElem.click()
old=driver_2.current_url
print(old)
time.sleep(2)
inputElem = driver_2.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string")
inputElem.click()


# In[29]:


number2="/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[2]/div[1]/div/div[1]/div/h3/a/yt-formatted-string"
html(/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-shelf-renderer[1]/div[1]/div[2]/ytd-vertical-list-renderer/div[1]/ytd-video-renderer[2]/div[1]/div/div[1]/div/h3/a/yt-formatted-string")
results = number2.find('ytd-video-renderer[2]')

for number in range(2,10):
    driver_2.switch_to.new_window()
    driver_2.get(old)
    print(results)
    inputElem = driver_2.find_element_by_xpath(number2)
    number2=number2[:result+19]+str(number)+number2[result+20:]
    print(number2)
    
       
    time.sleep(2)
    inputElem.click()
    time.sleep(4)


# In[ ]:



number2[:result+19]+str(number)+number2[result+20:]


# In[ ]:


user_data = driver_2.find_elements_by_xpath('//*[@id="video-title"]')

links = []
title=[]
for i in user_data:
            links.append(i.get_attribute('href'))
            title.append(i.get_attribute('title'))


# In[ ]:


print(links)
print(title)


# In[ ]:


for number in links:
    driver_2.switch_to.new_window()
    driver_2.get(number)


# In[ ]:




