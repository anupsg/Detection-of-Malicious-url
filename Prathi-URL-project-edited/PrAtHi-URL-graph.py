#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


traindata = pd.read_csv('rnn.csv')


# In[17]:


#get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
plt.show(block=True)

# In[20]:


print(traindata.keys())


# In[21]:


# summarize history for accuracy
plt.plot(traindata['acc'])
plt.plot(traindata['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()


# In[22]:


# summarize history for loss
plt.plot(traindata['loss'])
plt.plot(traindata['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()


# In[ ]:




