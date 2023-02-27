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
        self.parent = list(map(int, input().split(' ')))

    def parse_input_file(self, file_name):
        file = open(file_name, "r", -1, "utf-8")
        self.n = int(file.readline())
        self.parent = list(map(int, file.readline().split(' ')))

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
    key = sys.stdin.readline(1)
    if (key.upper() == "I"):
        tree_instance.parse_input_user()
        mex_height = tree_instance.compute_height()
        print(mex_height)
    elif (key.upper() == "F"):
        file_name = input("Enter filepath:")
        if (file_name.lower() == "a"):
            print("Bad file name!")
            return

        tree_instance.parse_input_file(file_name)
        mex_height = tree_instance.compute_height()
        print(mex_height)

    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))