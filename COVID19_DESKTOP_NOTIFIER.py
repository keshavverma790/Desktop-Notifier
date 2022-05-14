#!/usr/bin/env python
# coding: utf-8

# In[42]:


pip install win10toast


# In[43]:


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier


# In[44]:


header = {"User-Agent" : "Brave"}
req = Request("https://www.worldometers.info/coronavirus/country/india/", headers = header)
html = urlopen(req)


# In[45]:


html.status


# In[46]:


obj = bs(html)


# In[47]:


new_cases = obj.find("li", {"class" : "news_li"}).strong.text.split()[0]


# In[48]:


new_deaths = list(obj.find("li", {"class" : "news_li"}).strong.next_siblings)[1].text.split()[0]


# In[49]:


notifier = ToastNotifier()


# In[50]:


message = "New cases - " + new_cases + "n" + "New Deaths - " + new_deaths


# In[51]:


message


# In[52]:


notifier.show_toast(title = "COVID UPDATE", msg = message, duration = 5)


# In[ ]:




