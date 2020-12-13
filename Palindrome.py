#!/usr/bin/env python
# coding: utf-8

# In[13]:


class Qeque_byJ :
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def add_rear(self,item):
        self.items.append(item)
    def add_front(self,item):
        self.items.insert(0,item)
    def remove_rear(self):
        return self.items.pop()
    def remove_front(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def show(self):
        return self.items

def Palindrome(text):
    
    Palindrome = Qeque_byJ()
    for string in text :
        Palindrome.add_rear(string)
    
    status = True
    
    while Palindrome.size() > 1 and status :
        front = Palindrome.remove_front()
        end = Palindrome.remove_rear()
        
        if front != end :
            status = False
    return status


print(Palindrome("abcdefg"))
print(Palindrome("radar"))


# In[ ]:




