#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, items):
        self.items.insert(0,items)

    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def show(self):
        return self.items

def menu() :
    print("\n\nchoose: 1 >> counter 1 to get customer. \tchoose: 2 >> counter 2 to get customer\t3. >> custorme waiting,and 4 > quit\n\n\n")
queue_j = Queue()

while True :
    menu()
    fn_input = int(input("Waiting for customer :  "))
    customer_waiting = queue_j.size()
    if fn_input == 1 :
        if customer_waiting > 0 :
            dequeue = queue_j.dequeue()
            print("Customer ({}) com to counter 1  : ".format(dequeue))
            customer_waiting -= 1
            print("Number of waiting customer : {}".format(customer_waiting))
            print("Waiting customer >>>  ",queue_j.show())
        else:
            print("Number of waiting customer : {}".format(customer_waiting))
            print("No one waiting")
    elif fn_input == 2 :
        if customer_waiting > 0 :
            dequeue = queue_j.dequeue()
            print("Customer ({}) com to counter 2  : ".format(dequeue))
            customer_waiting -= 1
            print("Number of waiting customer : {}".format(customer_waiting))
            print("Waiting customer >>>  ",queue_j.show())
        else:
            print("Number of waiting customer : {}".format(customer_waiting))
            print("No one waiting")
    elif fn_input == 3 :
            queue_input = input("Enter customer name >>>").strip()
            queue_j.enqueue(queue_input)
            print("Number of waiting customer : {}".format(customer_waiting))
            print("Waiting customer >>>  ",queue_j.show())
    else :
        break
    
    


# In[ ]:




