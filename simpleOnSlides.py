#!/usr/bin/env python
# coding: utf-8

# In[1]:


import checklist
from checklist.editor import Editor
from checklist.perturb import Perturb


# In[4]:


#VOCAB+POS--MFT
editor = Editor(language='chinese')
con = '店家服务是{adj}的'
ret = editor.template(con,adj=['非常好', '不错', '垃圾的', '无与伦比的', '差劲', '优美的', '鸟语花香', '百花齐放', '繁花似锦', '桃红柳绿', '春色满园',
                               '春意盎然','喜上眉梢','兴高采烈','眉飞色舞','喜笑颜开','欣喜若狂','心花怒放','相当好',])
ret.data


# In[11]:


#VOCAB+POS--INV
editor = Editor(language='chinese')
con = '这次又买了一个{adj}'
ret = editor.template(con,adj=['小米10', '小天鹅', '华为mate40', '苹果12', '锤子', '魅族', '三星', '奔驰', '宝马', 
                               '劳力士', '酷派','菲仕乐','WMF','康宁','苏泊尔','健力宝','可口可乐','滴滴','回力','LV'])
ret.data


# In[ ]:


#VOCAB+POS--DIR
editor = Editor(language='chinese')
con = '这次又买了一个{adj}'
ret = editor.template(con,adj=['小米10', '小天鹅', '华为mate40', '苹果12', '锤子', '魅族', '三星', '奔驰', '宝马', 
                               '劳力士', '酷派','菲仕乐','WMF','康宁','苏泊尔','健力宝','可口可乐','滴滴','回力','LV'])
ret.data

