#%% Program to create Linked List data structure
import numpy as np
def print_matrix(x,y,G,attrib):
    for row in range(x):
        for col in range(y):
            print (G.nodes[(row,col)][attrib], end =" ")
        print()
    print()

def print_values():
    print ("matrix 1 : values")
    print_matrix(x,y,G,"valueA")
    print ("matrix 2 : values")
    print_matrix(x,y,G,"valueB")

def print_nvalues():
    print ("matrix 1 : nvalues")
    print_matrix(x,y,G,"nvalueA")
    print ("matrix 2 : nvalues")
    print_matrix(x,y,G,"nvalueB")

# %% Linked list
# Node class 
class Node: 
  
    # Function to initialise the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
  
# Linked List class contains a Node object 
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # This function prints contents of linked list 
    # starting from head 
    def printList(self): 
        temp = self.head 
        while (temp): 
            print (temp.data) 
            temp = temp.next
