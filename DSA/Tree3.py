from Tree1 import *

class TreeNode(TreeNode):
    def __init__(self, data, level):
        super().__init__(data)
        self.level = level

    def print_tree(self, type):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if self.level <= type :
            print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(type)

def build_location_tree():
    root = TreeNode('Global', 0)

    cty1 = TreeNode('India', 1)
    st1 = TreeNode('Gujarat', 2)
    st1.add_child(TreeNode('Ahmadabad', 3))
    st1.add_child(TreeNode('Baroda', 3))
    st2 = TreeNode('Karnataka',1)
    st2.add_child(TreeNode('Bengluru', 3))
    st2.add_child(TreeNode('Mysore', 3))
    cty1.add_child(st1)
    cty1.add_child(st2)

    cty2 = TreeNode('USA', 1)
    st3 = TreeNode('Newjersey', 2)
    st3.add_child(TreeNode('Pricton', 3))
    st3.add_child(TreeNode('Trenton', 3))
    st4 = TreeNode('California', 2)
    st4.add_child(TreeNode('San Francisco', 3))
    st4.add_child(TreeNode('Mountmain view', 3))
    st4.add_child(TreeNode('Palo Alto', 3))
    cty2.add_child(st3)
    cty2.add_child(st4)

    root.add_child(cty1)
    root.add_child(cty2)

    return root

if __name__=='__main__':
    root_node = build_location_tree()
    root_node.print_tree(2)