#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

def postfix_byJ(text_input):
    # text_input = text_input.split()
    stack_j = Stack()
    for str in text_input:
        if str in "0123456789" :
            stack_j.push(int(str))
        else:
            str1 = stack_j.pop()
            str2 = stack_j.pop()

            math_j = do_math_J(str,str2,str1)
            stack_j.push(math_j)
    return  stack_j.pop()
def do_math_J(op,n1,n2) :
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1-n2
    elif op == "*":
        return n1 * n2
    else :
        return n1 / n2


print(postfix_byJ("22*45*+"))

