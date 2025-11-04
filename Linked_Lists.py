# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 20:10:34 2025

@author: John
"""
'''node class produces a node with the a ppinter that will take the next node'''
class Node:
    #constructor for node intialisation
    def __init__(self, data):
        self.data=data #node data
        self.next=None #node pointer to the next node

'''linked list class takes a node as a head'''
class LinkedList:
    #Constructor for intialistaion
    def __init__(self):
        self.head=None #the head of the linked list
    
    
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head #setting the pointer of next to the start of th elinked list
        self.head = new_node #reassigning the head as teh new node
        
    
    def append(self, data):
        new_node = Node(data) #creating a new node
        if not self.head: #checking that head of the linked list ois occupied
            self.head=new_node
            return
        current=self.head #set current pointer to head of list
        while current.next:
            current=current.next #set current pointer the location of the new node
        current.next=new_node #set the current pointer to the new node
    
    
    def delete(self, data):
        if not self.head: #ensure we start at the head of the list
            return
        if self.head.data==data:
            self.head=self.head.next
            return 
        current = self.head
        while current.next and current.next.data!=data: #cycling throught he linked list and moving t epointer when data does not equal value
            current = current.next
        if current.next: 
            current.next = current.next.next #forcing the pointer to jump the entry that we dont want
            
    def swap(self,data1,data2):
        if not self.head:
            return
        current1 = self.head
        current2 = self.head
        while current1.data!=data1:
            current1=current1.next
        while current2.data!=data2:
            current2=current2.next
            swap_data=current1.data
        current1.data=current2.data
        current2.data=swap_data
    
        
    def reverse(self):
        if not self.head:
             return
        if not self.head.next:
             return
        current = self.head
        previous=None
        while current:
            next_node = current.next #saving the next node
            current.next = previous #making the pointer point to the node stored in previous
            previous = current #moving th e previous pointer to the current node ready for the next iteration
            current = next_node #moving the current node to the next node
        self.head=previous #making the head of the linkedlist at the new starting node
    
    
    def insert(self,position,data):
        if not self.head:
            return
        current = self.head
        new_node = Node(data)
        if position==0: #Handling thezeroth node and reassigng thehead of the linked list
            new_node.next=current
            self.head=new_node
        else:
            pos=1
            while current and pos!=position: #going through the linked list until the right position has been found
                if not current.data or current.next: #ensuring that the positon is in range
                    pos+=1
                    current=current.next
                else:
                    print('Insertion position out of range.')
                    return
            new_node.next=current.next
            current.next=new_node
        
    def display(self):
        if not self.head:
            return
        list_entries=[]
        current = self.head #pointer to current data
        while current: 
            list_entries.append(current.data)
            current=current.next #moving th epointer to the next list entry
        print('->'.join(map(str,list_entries)))
        
        
    def destroy(self):
        if not self.head:
            return
        current = self.head
        while current:
            LinkedList.delete(self,current.data)
            current = current.next
        
if __name__=='__main__':
    
    ll=LinkedList()
    
    for i in range(0,10):
        ll.append(i)
    
    # for i in range(1,10):
    #     ll.prepend(-1*i)
    #ll.swap(-9,9)
    ll.insert(1,99)
    ll.display()
    
    # for i in range(0,10):
    #     ll.delete(i)
    
    # for i in range(0,10):
    #     ll.delete(i)
   
    # ll.display()
    
    # ll.destroy()
    
    # ll.display()
    
    
    
    
        