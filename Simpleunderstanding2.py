#!/usr/bin/env python
# coding: utf-8

# In[1]:


import checklist
from checklist.editor import Editor
from checklist.perturb import Perturb


# In[2]:


editor = Editor(language='chinese')


# In[6]:


ret = editor.template('这是一个{adj}电影', adj=['好看的', '不好看的', '垃圾的', '无与伦比的','新奇的','优美的'])
ret.data


# In[15]:


ret = editor.template('{male}是小米人吗', remove_duplicates=True)
ret.data[0:10]


# In[17]:


editor.add_lexicon('adj', ['good', 'bad', 'great', 'terrible'])


# In[18]:


ret = editor.template('{adj} is not the same as {adj2}', remove_duplicates=True)
ret.data[:4]


# In[29]:


editor.visual_suggest('这是一个{mask}的西瓜.')


# In[ ]:




