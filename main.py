import random
import socket

from queue import LifoQueue

from graphviz import Digraph

from Node import Node


def all_explored():
    for node in nodes:
        if node.get_value() == "Z":
            if node.get_explored_count() < 1:
                return False
        else:
            if node.get_explored_count() < 3:
                return False

    return True


def get_node(node_value):
    for node in nodes:
        if node.get_value() == node_value:
            return node

    return None


digraph = Digraph('State machine')
nodes = []
for node_value in [chr(i) for i in range(65, 91)]:
    nodes.append(Node(node_value))
    digraph.node(node_value, node_value)

digraph.edge('Z', 'A', label='1')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("20.28.230.252", 65432))
start_node_value = s.recv(1024).decode('utf-8')[0]
current_node = get_node(start_node_value)


while not all_explored():
    print(current_node.get_value())
    if current_node.get_explored_count() < 3:
        s.send((str(current_node.get_explored_count() + 1) + "\n").encode('utf-8'))
        next_node_value = s.recv(1024).decode('utf-8')[0]
        current_node.set_explored_count(current_node.get_explored_count() + 1)
        digraph.edge(current_node.get_value(), next_node_value, label=str(current_node.get_explored_count()))

        if next_node_value == "Z":
            current_node = get_node('A')

            if get_node('Z').get_explored_count() < 1:
                get_node('Z').set_explored_count(1)

        else:
            current_node = get_node(next_node_value)

    else:
        s.send(random.choice(["1\n", "2\n", "3\n"]).encode('utf-8'))
        next_node_value = s.recv(1024).decode('utf-8')[0]

        if next_node_value == "Z":
            current_node = get_node('A')
        else:
            current_node = get_node(next_node_value)

digraph.view()
