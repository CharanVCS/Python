from Tree1 import *

class TreeNode(TreeNode):
    def __init__(self, data, designation):
        super().__init__(data)
        self.designation = designation

    def print_tree(self, type):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if type=='both':
            print(prefix + self.data, self.designation)
        elif type=='name' :
            print(prefix + self.data)
        elif type=='designation' :
            print(prefix + self.designation)
        if self.children:
            for child in self.children:
                child.print_tree(type)
        
def build_management_tree():
    root = TreeNode('Nilupul', '(CEO)')

    CTO = TreeNode('Chinmay', '(CTO)')
    head1 = TreeNode('Viswa', '(Infratructure Head)')
    head1.add_child(TreeNode('Dhaval', '(Cloud Manager)'))
    head1.add_child(TreeNode('Abhijit', '(App Manager)'))
    head2 = TreeNode('Aamir', '(Application Head)')
    CTO.add_child(head1)
    CTO.add_child(head2)

    HR = TreeNode('Gels', '(HR Head)')
    HR.add_child(TreeNode('Peter', '(Recruitment Manager)'))
    HR.add_child(TreeNode('Waqas', '(Policy Manager)'))

    root.add_child(CTO)
    root.add_child(HR)

    return root

if __name__=='__main__':
    root_node = build_management_tree()
    root_node.print_tree('name') # prints only name hierarchy
    print()
    root_node.print_tree("designation") # prints only designation hierarchy
    print()
    root_node.print_tree("both") # prints both (name and designation) hierarchy