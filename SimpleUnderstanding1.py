#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
countries = ['France', 'Germany', 'Brazil']
for country in countries:
    ts = editor.template('{male} {last} is from {city}',
                male=editor.lexicons.male_from[country],
                last=editor.lexicons.last_from[country],
                city=editor.lexicons.country_city[country],
               )
    print('Country: %s' % country)
    print('\n'.join(np.random.choice(ts.data, 3)))
    print()


# In[11]:


import re
import checklist
from checklist.perturb import Perturb
def replace_john_with_others(x, *args, **kwargs):
    # Returns empty (if John is not present) or list of strings with John replaced by Luke and Mark
    if not re.search(r'\bJohn\b', x):
        return None
    return [re.sub(r'\bJohn\b', n, x) for n in ['Luke', 'Mark']]

dataset = ['John is a man', 'Mary is a woman', 'John is an apostle']
ret = Perturb.perturb(dataset, replace_john_with_others)
ret.data


# In[12]:


import checklist
from checklist.editor import Editor
from checklist.perturb import Perturb
from checklist.test_types import MFT, INV, DIR
editor = Editor()

t = editor.template('This is {a:adj} {mask}.',  
                      adj=['good', 'great', 'excellent', 'awesome'])
test1 = MFT(t.data, labels=1, name='Simple positives',
           capability='Vocabulary', description='')


# In[ ]:




