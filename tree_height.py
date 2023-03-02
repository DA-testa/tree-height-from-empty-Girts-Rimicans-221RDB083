# python3

import sys
import threading
import numpy

class Tree:
    def __init__(self) -> None:
        self.n = None
        self.parent = None
        self.tree_nodes = None
        self.tree_root = None
        self.height = 1

    def parse_input_user(self):
        self.n = int(input())
        # print(self.n)
        self.parent = list(map(int, input().strip().split(' ')))
        # print(self.parent)

    def parse_input_file(self, file_name):
        file = open(file_name, "r", -1, "utf-8")
        self.n = int(file.readline().strip())
        # print(self.n)
        self.parent = list(map(int, file.readline().strip().split(' ')))
        # print(self.parent)

    def create_tree_nodes(self):
        self.tree_nodes = [ [] for i in range(self.n) ]
        for inner_index in range(self.n):
            index_parent = self.parent[inner_index]
            if index_parent == -1:
                self.tree_root = inner_index
            else:
                self.tree_nodes[index_parent].append(inner_index)

    def get_tree_depth(self, index, height):
        if not self.tree_nodes[index]:
            return height
        tree_depth = 0
        for node_index in self.tree_nodes[index]:
            tree_depth = max(tree_depth, self.get_tree_depth(node_index, height + 1))
        return tree_depth

    def compute_height(self):
        self.create_tree_nodes()
        return self.get_tree_depth(self.tree_root, self.height)

def main():
    tree_instance = Tree()
    try:
        key = input().strip()
        # print(key)
        if (key.upper() == "I"):
            tree_instance.parse_input_user()
            mex_height = tree_instance.compute_height()
            print(mex_height)
        elif (key.upper() == "F"):
            file_name = input().strip()
            if (file_name.lower() == "a"):
                pass

            tree_instance.parse_input_file("test/" + file_name)
            mex_height = tree_instance.compute_height()
            print(mex_height)
    except:
        pass

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
