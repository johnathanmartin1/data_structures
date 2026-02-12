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

'''__________________________________________________________________________
_____________________BINARY TREE CLASS USING THE NODE CLASS__________________
_____________________________________________________________________________'''

class BinaryTree:
    '''Binary tree constrtuctor'''
    def __init(self):
        self.root=None
        self.tree_type=None #assinging a tree type so that methods can be filtered 
    
    
    '''_______________________________________________________________________
    ________________________BUILD TREE METHODS_______________________________
    _________________________________________________________________________'''
    
    
    '''********************************************************************'''
    '''recursive method called by build_breadth_tree function to build a
    tree filling all layers from left to right'''
    @classmethod 
    def build_breadth(cls,data,index=0):
        if index>=len(data) or data[index] is None: #checking the data exists
            return None
        node = Node(data[index]) #assining the first element as a new node
        node.left = cls.build_breadth(data,2*index+1) #splitting the data in to left and rigth sub trees
        node.right = cls.build_breadth(data, 2*index+2)
        return node
    
    '''user callable method to build a breadth first tree from a list filling
    the layers left to right'''
    def build_breadth_tree(self,data):
        self.tree_type='binary tree'
        self.root =  self.build_breadth(data)
           
    '''******************************************************************'''
   
    
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
    
    '''user callable method to build binary search tree from a list
    sorted or not'''
    def build_binary_search_tree(self,data):
        self.tree_type='binary search tree'
        self.root = self.build_binary_search(data)    
    '''*******************************************************************'''
    
    
    '''_______________________________________________________________________
    __________________TREE ALTERATION METHODS_________________________________
    __________________________________________________________________________'''
    
    
    '''********************************************************************'''
    '''inversion recuresive function called by invert method'''
    @classmethod
    def invert_recursive(cls,node):
        if node is None:
            return
        temp = node.right
        node.right = cls.invert_recursive(node.left)
        node.left = cls.invert_recursive(temp)
        return node
    
    '''user callable function to invert a binary tree'''
    def invert(self):
        current = self.root
        self.invert_recursive(current)
    '''*********************************************************************'''
    
    '''converts a binary tree into a binary search tree'''        
    def convert_to_binary_search(self):
        if self.tree_type == 'binary search tree':
            return
        tree = sorted([element for element in self.get_tree() if element is not None])
        self.root = self.build_binary_search(tree)
        self.tree_type = 'binary search tree'
        
        
    '''_______________________________________________________________________
    _______________________TREE SEARCH METHODS________________________________________
    __________________________________________________________________________'''
    
    
    '''********************************************************************'''
    '''depth first search pre order method access to binary tree'''
    @classmethod
    def depth_first_search_pre_order(cls,node,list_nodes):
        if node is None:
            list_nodes.append(None)
        else:
            list_nodes.append(node.data)
            cls.depth_first_search_pre_order(node.left,list_nodes)
            cls.depth_first_search_pre_order(node.right,list_nodes) 
    
    '''depth first search post order method access to binary tree'''
    @classmethod
    def depth_first_search_post_order(cls,node,list_nodes):
        if node is None:
            list_nodes.append(None)
        else:
            cls.depth_first_search_post_order(node.left,list_nodes)
            cls.depth_first_search_post_order(node.right,list_nodes) 
            list_nodes.append(node.data)
            
    '''depth first search in order method access to binary tree'''
    @classmethod
    def depth_first_search_in_order(cls,node,list_nodes):
        if node is None:
            list_nodes.append(None)
        else:
            cls.depth_first_search_in_order(node.left,list_nodes)
            list_nodes.append(node.data)
            cls.depth_first_search_in_order(node.right,list_nodes) 
    
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
            
            
    '''method to get the binary tree with search type option in a list'''
    def get_tree(self,search_type='dfspre'):
        nodes=[]
        current=self.root
        if search_type == 'dfspre':
            self.depth_first_search_pre_order(current,nodes)
        if search_type == 'dfspost':
            self.depth_first_search_post_order(current, nodes)
        if search_type == 'dfsin':
            self.depth_first_search_in_order(current, nodes)
        if search_type == 'bfs':
            self.breadth_first_search(current,nodes)
        return nodes
    '''******************************************************************'''
    
'''_________________________________________________________________________
________________END OF BINARY TREE CLASS____________________________________
__________________________________________________________________________'''
if __name__=='__main__':
    
    bt=BinaryTree()
  
    practice = [1,2,3,4,5,6,7]
    
    #bt.build_binary_search_tree(practice)
    
    bt.build_breadth_tree(practice)
    print(bt.tree_type)
    print(bt.get_tree('bfs'))
    
    
    
    bt.convert_to_binary_search()
  
    
    #bt.invert()
    
    
    print(bt.tree_type)
    print(bt.get_tree('bfs'))
    
    
        
