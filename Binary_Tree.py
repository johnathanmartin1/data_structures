# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 04:11:37 2025

@author: John
"""
from collections import deque


'''node for binary tree'''
class Node:
    #constrictor for a binary tree node 
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    
class BinaryTree:
    #constructor for the binary tree
    def __init(self):
        self.root=None
    
    '''recursive method called by build_breadth_tree function'''
    @classmethod 
    def build_breadth(cls,data,index=0):
        if index>=len(data) or data[index] is None: #checking the data exists
            return None
        node = Node(data[index]) #assining the first element as a new node
        node.left = cls.build_breadth(data,2*index+1) #splitting the data in to left and rigth sub trees
        node.right = cls.build_breadth(data, 2*index+2)
        return node
    
    '''user callable method to build a breadth first tree'''
    def build_breadth_tree(self,data):
        self.root =  self.build_breadth(data)
    
    '''recursive method to build a binary search tree called 
    by build_binary_search_tree function'''
    @classmethod
    def build_binary_search(cls,data):
        if len(data)==0: #checking that the list contains data
            return 
        data = sorted(data) #sorting the dtat into correct order
        root_index = len(data)//2 #finding the center of the array
        node = Node(data[root_index]) #assigning the centre of the aray as the new node
        node.left = cls.build_binary_search(data[:root_index]) #splitting the reming area in two sub arrays left and right of the middle element
        node.right = cls.build_binary_search(data[root_index+1:]) 
        return node
    
    '''user callable method to build binary search tree'''
    def build_binary_search_tree(self,data):
        self.root = self.build_binary_search(data)    
    
    '''depth first search method access to binary tree'''
    @classmethod
    def depth_first_search(cls,node,list_nodes):
        if node is None:
            list_nodes.append(None)
        else:
            list_nodes.append(node.data)
            cls.depth_first_search(node.left,list_nodes)
            cls.depth_first_search(node.right,list_nodes) 
    
    '''breadth first search method to access binary tree'''
    @classmethod
    def breadth_first_search(cls,node,list_nodes):
        if not node:
            return
        queue = deque([node])
        while queue:
            current_level=[]
            for _ in range(len(queue)):
                current = queue.popleft()
                if current:
                    current_level.append(current.data)
                    queue.append(current.left)
                    queue.append(current.right)
                else:
                    current_level.append(None)
            list_nodes.append(current_level)
            
            
    '''method to print out the binary tree with search type option'''
    def display(self,search_type='dfs'):
        nodes=[]
        current=self.root
        if search_type=='dfs':
            self.depth_first_search(current,nodes) 
        if search_type == 'bfs':
            self.breadth_first_search(current,nodes)
        print(nodes)

if __name__=='__main__':
    
    bt=BinaryTree()
  
    practice = [1,10,15,6,3,134,9]
    
    bt.build_binary_search_tree(practice)
    
    #bt.build_breadth_tree(practice)
    
    bt.display('bfs')
    
        
