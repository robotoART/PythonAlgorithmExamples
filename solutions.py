# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 19:29:11 2018

@author: Alberto Rosario
Udacity Technical Interview Practice solutions
"""
import sys

"""
Question 1
Given two strings s and t, determine whether some anagram of t is a substring 
of s. For example: if s = "udacity" and t = "ad", 
then the function returns True. Your function definition should look like: 
question1(s, t) and return a boolean True or False.
"""
from itertools import permutations

def question1(s,t):
    try:
        if len(t) <= len(s) and len(t) > 0:
            perm = list(map("".join, permutations(t)))
            i = 1
            while i <= len(perm):
                if s.find(perm[i-1]) != -1:
                    return True
                else:
                    i += 1
            else:
                return False
        else:
            return False
    except:
        print ("Input error. Please input a string type, and make sure it is " 
        "smaller than or equal to in length as the main string.")
        return False

print "\n #1"
main_str = "fastest"
sub_str = "rtakljkljklj"

print "print question1(test1): " + str(question1(main_str, sub_str))
# Expected output: print question1(): False

print "print question1(test2): " + str(question1(main_str, ''))
# Expected output: print question1(): False 
# Input error. Please input a string type, and make sure it is smaller than or
# equal to in length as the main string.

print "print question1(test3): " + str(question1(main_str, None))
# Expected output: print question1(): False


"""
Question 2
Given a string a, find the longest palindromic substring contained in a. 
Your function definition should look like question2(a), and return a string.
"""
def question2(a):
    in_err = ("Input Error. Please make sure to enter a string atleast 2 "
    "letters long. Spaces are not counted.")
    try:
        no_palindrome = "Sorry, no palindromes found in given string."
        if type(a) is str and len(a.split()) > 0:
            a = "".join(a.split()).lower()
            if a.find(a[::-1]) == 0:
                return a[::-1]
            else:
                k = len(a)-2 # start with longest length of words to search for
                while k >= 3: # shortest word lengths to search for 
                    s1 = 0
                    e1 = s1+k
                    while e1 <= len(a):
                        b = a[s1:e1]
                        if a[s1:e1] == b[::-1]:
                            return b
                        else:
                            s1 += 1
                            e1 += 1
                    else:
                        k -= 1
                else:
                    return no_palindrome
        else:
            return in_err
    except:
        return in_err

print "\n #2"
test1 = "Taco Cat"
print "print question2(test1): " + str(question2(test1))
# Expected output: print question2(): tacocat

test2 = "   "
print "print question2(test2): " + str(question2(test2))
# Expected output: print question2(): Input Error. Please make sure to enter
# a string atleast 2 letters long. Spaces are not counted.

test3 = None
print "print question2(test3): " + str(question2(test3))
# Expected output: print question2(): Input Error. Please make sure to enter
# a string atleast 2 letters long. Spaces are not counted.

test4 = "x taco cat z ada s"
print "print question2(test4): " + str(question2(test4))
# Expected output: print question2(): tacocat

        
"""
Question 3
Given an undirected graph G, find the minimum spanning tree within G. 
A minimum spanning tree connects all vertices in a graph with the smallest 
possible total weight of edges. Your function should take in and return an 
adjacency list structured like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}
Vertices are represented as unique strings. 
The function definition should be question3(G)
"""
def question3(G):
    if type(G) != dict:
        return "Input type Error. Please input a dictionary."
    if len(G) < 2:
        return "Input length Error. Please input a dictionary with 2 or more edges"
    # queing the nodes setup
    nodes_Que_list = sorted(G.keys()) # list has [str of each node name]
    # initialize tree_nodes_Q
    tree_nodes_Q = {} # is Q
    for n in G.keys(): # must be each node in GRAPH
        tree_nodes_Q[n] = [sys.maxint, None] # [name]:[weight,from_node]
    tree_nodes_Q['A'] = [0, None] # set MST root node    
    ### begin finding MST edges
    mst_list = []
    while len(nodes_Que_list) != 0:
        indx_sm_node_w = [x[1][0] for x in tree_nodes_Q.items()].index(min([x[1][0] for x in tree_nodes_Q.items()]))
        tru_sm_tree_nod = tree_nodes_Q.items()[indx_sm_node_w][0]
        adj_edges_dict = dict(G.get(tru_sm_tree_nod)) # adjacent edges of smallest tree node
        # if small tree node parent not None ... todo
        if tree_nodes_Q.get(tru_sm_tree_nod)[1] != None:
            mst_list.append((tree_nodes_Q.get(tru_sm_tree_nod)[1], (tru_sm_tree_nod, tree_nodes_Q.get(tru_sm_tree_nod)[0])))
            mst_list.append((tru_sm_tree_nod, (tree_nodes_Q.get(tru_sm_tree_nod)[1], tree_nodes_Q.get(tru_sm_tree_nod)[0])))
        for n in adj_edges_dict.items(): # n is (str_name, int_weight)
            if tree_nodes_Q.has_key(n[0]) and n[1] < int(tree_nodes_Q.get(n[0])[0]):
                tree_nodes_Q[n[0]] = [n[1], tru_sm_tree_nod]
        # remove current visited tree node from Que list
        nodes_Que_list.remove(tru_sm_tree_nod)
        tree_nodes_Q.pop(tru_sm_tree_nod)
    return sorted(mst_list)

print "\n #3"
test1 = {
'A': [('B', 2), ('D', 1)],
'B': [('A', 2), ('C', 5)], 
'C': [('B', 5), ('D', 8)],
'D': [('C', 8), ('A', 1)]}
print "print question3(test1):" 
print question3(test1)
# Expected output:
# print question3():
# {'A': [('B', 2)], 'B': [('C', 5)], 'C': [('B', 5)], 'D'[('A', 1)]}

test2 = {
'A': [('B', 2), ('D', 1)],
'B': [('A', 2), ('C', 5)], 
'C': [('B', 5), ('D', 8)],
'D': [('C', 8), ('A', 1)],
'F': [('A', 9), ('B', 2), ('D', 4)],
'G': [('C', 3), ('F', 1)]}
print "print question3(test2):" 
print question3(test2)
# Expected output:
# print question3():
# {'A': [('B', 2)], 'B': [('C', 5)], 'C': [('B', 5)], 'D'[('A', 1)]}

test3 = ""
print "print question3(test3):" 
print question3(test3)
# Expected output:
# print question3():
# Input type Error. Please input a dictionary.

test4 = {}
print "print question3(test4):" 
print question3(test4)
# Expected output:
# print question3():
# Input length Error. Please input a dictionary with 2 or more edges


"""
Question 4
Find the least common ancestor between two nodes on a binary search tree. 
The least common ancestor is the farthest node from the root that is an 
ancestor of both nodes. For example, the root is a common ancestor of all 
nodes on the tree, but if both nodes are descendents of the root's left child, 
then that left child might be the lowest common ancestor. You can assume that 
both nodes are in the tree, and the tree itself adheres to all BST properties. 
The function definition should look like question4(T, r, n1, n2), where T is 
the tree represented as a matrix, where the index of the list is equal to the 
integer stored in that node and a 1 represents a child node, r is a 
non-negative integer representing the root, and n1 and n2 are non-negative 
integers representing the two nodes in no particular order. For example, one 
test case might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
and the answer would be 3.
"""
### Question 4 Helpers
class BST_Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Build_BST(object):
    def __init__(self, root):
        self.root = BST_Node(root)
        
    def insert(self,new_val):
        self.insert_helper(self.root, new_val)
        
    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = BST_Node(new_val)
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = BST_Node(new_val)
                
    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)
        return False

def get_LCA(bst_root, n1, n2):
#    print "Check current bst_root"
#    print bst_root.value
    if bst_root is None:
        return None
    # Look in left of bst if n1 and n2 are smaller than root
    if(bst_root.value > n1 and bst_root.value > n2):
        return get_LCA(bst_root.left, n1, n2)

   # Look in right of bst if n1 and n2 are larger than root 
    if(bst_root.value < n1 and bst_root.value < n2):
        return get_LCA(bst_root.right, n1, n2)
        
    return bst_root.value
    
### End of Q4 Helpers

def question4(T, r, n1, n2):
#    print "step uno, prep BST with Root"
    bst = Build_BST(r)
#    print bst.root.value
#    print "step dos, Insert children in as given"
    current_child = 0
    for child in T[r]:
        if child == 1:
            bst.insert(current_child)
            current_child += 1
        current_child += 1
    
    rollcall = 0 # current child node number to properly feed BST
#    print "ROLLCALL!"
    while rollcall <= len(T)-1:
#        print rollcall
#        print "len(T)-1"
#        print len(T)-1
        node_val = 0
        for node in T:
            if rollcall != r:
                if node[rollcall] == 1:
                    bst.insert(node_val)
                node_val += 1
        rollcall += 1
    # "Now, what's the LCA in the BST?"
    this_LCA = get_LCA(bst.root, n1, n2)
#    print "Take a closer look at the BST node 3"
#    print bst.root.left.right.value
#    print bst.search(3)
    return this_LCA

print "\n #4"
print "question4(test1): The LCA of 1 and 4 is,..."
# Test 1:         0  1  2  3  4
print question4([[0, 1, 0, 0, 0], # 0
                 [0, 0, 0, 0, 0], # 1
                 [0, 0, 0, 0, 0], # 2
                 [1, 0, 0, 0, 1], # 3
                 [0, 0, 0, 0, 0]], # 4 
                 3, 1, 4)
# the answer should be 3.

print "question4(test2): The LCA of 2 and 4 is,..."
# Test 2:         0  1  2  3  4  5  6
print question4([[0, 0, 0, 0, 0, 0, 0], # 0
                 [1, 0, 0, 1, 0, 0, 0], # 1
                 [0, 0, 0, 0, 0, 0, 0], # 2
                 [0, 0, 1, 0, 1, 0, 0], # 3
                 [0, 0, 0, 0, 0, 0, 0], # 4
                 [0, 1, 0, 0, 0, 0, 1], # 5
                 [0, 0, 0, 0, 0, 0, 0]], # 6 
                 5, 2, 4)
# the answer should be 3.

print "question4(test3): The LCA of 1 and 4 is,..."
# Test 3:         0  1  2  3  4  5  6
print question4([[0, 0, 0, 0, 0, 0, 0], # 0
                 [1, 0, 0, 1, 0, 0, 0], # 1
                 [0, 0, 0, 0, 0, 0, 0], # 2
                 [0, 0, 1, 0, 1, 0, 0], # 3
                 [0, 0, 0, 0, 0, 0, 0], # 4
                 [0, 1, 0, 0, 0, 0, 1], # 5
                 [0, 0, 0, 0, 0, 0, 0]], # 6 
                 5, 4, 1)
# the answer should be 1.

print "question4(test4): The LCA of 2 and 6 is,..."
# Test 4:         0  1  2  3  4  5  6
print question4([[0, 0, 0, 0, 0, 0, 0], # 0
                 [1, 0, 0, 1, 0, 0, 0], # 1
                 [0, 0, 0, 0, 0, 0, 0], # 2
                 [0, 0, 1, 0, 1, 0, 0], # 3
                 [0, 0, 0, 0, 0, 0, 0], # 4
                 [0, 1, 0, 0, 0, 0, 1], # 5
                 [0, 0, 0, 0, 0, 0, 0]], # 6 
                 5, 2, 6)
# the answer should be 5.

"""
Question 5
Find the element in a singly linked list that's m elements from the end. 
For example, if a linked list has 5 elements, the 3rd element from the end is
the 3rd element. The function definition should look like question5(ll, m), 
where ll is the first node of a linked list and m is the "mth number from the 
end". You should copy/paste the Node class below to use as a representation 
of a node in the linked list. Return the value of the node at that position.

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
"""
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
    
def question5(ll, m):
    return
    