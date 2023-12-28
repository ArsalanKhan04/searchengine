#!/usr/bin/env python
# coding: utf-8

# In[1]:


#  taking word list from nltk
# first we import nltk library 
import nltk
# downloading words from nltk
nltk.download('words')  
# taking the english word from all list of words
word_list = nltk.corpus.words.words()
# check the lebgth of word list 
length_of_wordlist=len(word_list)


# In[8]:


# now the length of word list is [236736] stored in var length_of_wordlist
# by using function we assign unique wordId to word. 

def WordID(word):
    wordaddress=word_list.index(word) 
    return wordaddress
WordID("this")


# In[ ]:




