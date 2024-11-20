from BS_Tree1 import *

class Bs_tree(BinarySearchTreeNode):

    def add_child(self, data):
        if data == self.data:
            return  # node already exists
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = Bs_tree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Bs_tree(data)

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)

        return elements
    
    def find_max(self):
        if not self.right :
            return self.data
        
        return self.right.find_max()
    
    def find_min(self):
        if not self.left:
            return self.data
        return self.left.find_min()
    
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    
def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = Bs_tree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("in order traversal gives this sorted list:",numbers_tree.in_order_traversal())
    print("post order traversal gives this sorted list:",numbers_tree.post_order_traversal())
    print("pre order traversal gives this sorted list:",numbers_tree.pre_order_traversal())
    print('max number:', numbers_tree.find_max())
    print('min number:', numbers_tree.find_min())
    print('sum of elements:', sum(numbers_tree.in_order_traversal()))