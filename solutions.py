# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 19:29:11 2018

@author: Alberto Rosario
Udacity Technical Interview Practice solutions
"""


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

print "print question1(): " + str(question1(main_str, sub_str))
# Expected output: print question1(): False

print "print question1(): " + str(question1(main_str, ''))
# Expected output: print question1(): False 
# Input error. Please input a string type, and make sure it is smaller than or
# equal to in length as the main string.

print "print question1(): " + str(question1(main_str, None))
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
                k = len(a)-2 # start length of words to search for
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
print "print question2(): " + str(question2(test1))
# Expected output: print question2(): tacocat

test2 = "   "
print "print question2(): " + str(question2(test2))
# Expected output: print question2(): Input Error. Please make sure to enter
# a string atleast 2 letters long. Spaces are not counted.

test3 = None
print "print question2(): " + str(question2(test3))
# Expected output: print question2(): Input Error. Please make sure to enter
# a string atleast 2 letters long. Spaces are not counted.

test4 = "x taco cat z ada s"
print "print question2(): " + str(question2(test4))
# Expected output: print question2(): tacocat


### Helper functions for questions 3,4,5
import heapq

class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False
        self.predecessor = None

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to
        
    def __cmp__(self, otherEdge):
        return self.cmp(self.value, otherEdge.value)
        
    def __lt__(self, other):
        return self.value < other.value

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        
    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)
    
    def get_edge_list(self):
        edge_list = []
        for edge_object in self.edges:
            edge = (edge_object.value, edge_object.node_from.value, edge_object.node_to.value)
            edge_list.append(edge)
        return edge_list
        
    def get_node_list(self):
        node_list = []
        for node_object in self.nodes:
            node = (node_object.value, node_object.edges, node_object.visited, node_object.predecessor)
            node_list.append(node)
        return node_list
        
    def get_adjacency_list(self):
        max_index = self.find_max_index()
        adjacency_list = [None] * (max_index + 1)
        for edge_object in self.edges:
            if adjacency_list[edge_object.node_from.value]:
                adjacency_list[edge_object.node_from.value].append((edge_object.node_to.value, edge_object.value))
            else:
                adjacency_list[edge_object.node_from.value] = [(edge_object.node_to.value, edge_object.value)]
        return adjacency_list

    def get_adjacency_matrix(self):
        max_index = self.find_max_index()
        adjacency_matrix = [[0 for i in range(max_index + 1)] for j in range(max_index + 1)]
        for edge_object in self.edges:
            adjacency_matrix[edge_object.node_from.value][edge_object.node_to.value] = edge_object.value
        return adjacency_matrix
    
    def find_max_index(self):
        max_index = -1
        if len(self.nodes):
            for node in self.nodes:
                if node.value > max_index:
                    max_index = node.value
        return max_index

class PrimsAlgorithm(object):
    def __init__(self, unvisitedList):
        self.unvisistedList = unvisitedList
        self.spanningTree = []
        self.edgeHeap = []
        self.fullCost = 0
        
    def constructSpanningTree(self, node):
        self.unvisistedList.remove(node)
        while self.unvisistedList:
            for edge in node.edges:
                if edge.node_to in self.unvisistedList:
                    heapq.heappush(self.edgeHeap, edge)
            minEdge = heapq.heappop(self.edgeHeap)
            self.spanningTree.append(minEdge)
            print("Edge added to spanning tree %s : %s"%(minEdge.node_from.value, minEdge.node_to.value))
            self.fullCost += minEdge.value
            node = minEdge.node_to
            self.unvisistedList.remove(node)
                
    def getSpanningTree(self):
        return self.spanningTree
        
### End of helper functions
        
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
#    try:
    if type(G) != dict:
        return "Input type Error. Please input a dictionary."
    if len(G) < 2:
        return "Input length Error. Please input a dictionary with 2 or more edges"
    graph = Graph()
    graph_keys = sorted(G.keys())
    graph_sorted_items = sorted(G.items())
    for i in graph_sorted_items:
        graph.insert_node(graph_sorted_items.index(i))
        for e in i[1]:
            graph.insert_edge(e[1], graph_sorted_items.index(i),
                              graph_keys.index(e[0]))

    min_span_tree = PrimsAlgorithm(graph.nodes)
    min_span_tree.constructSpanningTree(graph.nodes[0])
    return "to_do_still"
#    except:
#        print "Input error. Please make sure graph is correctly formatted."
#        return

print "\n #3"
test1 = {
'A': [('B', 2), ('D', 1)],
'B': [('A', 2), ('C', 5)], 
'C': [('B', 5), ('D', 8)],
'D': [('C', 8), ('A', 1)]      }
print "print question3(test1):" 
print question3(test1)
# Expected output:
# print question3():
# {'A': [('D', 1)], 'B': [('A', 2)], 'C': [('B', 5)], 'D'[('A', 1)]}


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