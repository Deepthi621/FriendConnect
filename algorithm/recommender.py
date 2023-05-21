from classtype.Graph import Graph
from classtype.People import People
from algorithm.sna import *
import heapq

def recommendFriends(graph: Graph, person: People):
    return getNLevelFriend(graph, person, 2)

