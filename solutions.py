# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 19:29:11 2018

@author: Alberto Rosario
Udacity Technical Interview Practice solutions
"""
from math import factorial
from itertools import permutations

### Helper functions

# Removes all spaces from string and creates a list of each character
def str_to_char_list(in_str):
    return list(''.join(in_str.split()))

"""
Question 1
Given two strings s and t, determine whether some anagram of t is a substring 
of s. For example: if s = "udacity" and t = "ad", 
then the function returns True. Your function definition should look like: 
question1(s, t) and return a boolean True or False.
"""
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
                                return True
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