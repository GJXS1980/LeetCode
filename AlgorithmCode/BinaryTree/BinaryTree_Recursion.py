#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
二叉树的前、中、后序遍历(递归解法)

Author: GrantLi
"""

class TreeNode(object):
    """
    创建二叉链式节点
    """

    def __init__(self, val=None, left=None, right=None):
        self.val = val  # 数据
        self.left = left  # 左节点
        self.right = right  # 右节点

class BinaryTree(object):
    """
    二叉树
    """
    def __init__(self):
        """
        初始化二叉树
        """
        self.root = None  # 根结点
        self.result = list()  # 用于遍历

    def is_empty(self):
        """
        判断二叉树是否为空
        """
        return self.root is None
    
    def preorder_ergodic_recursion(self, data):
        """
        前序遍历：递归法
        """
        if data is None:
            return self.result
        else:
            self.result.append(data.val)
            self.preorder_ergodic_recursion(data.left)
            self.preorder_ergodic_recursion(data.right)   
            
    def middle__ergodic_recursion(self, data):
        """
        中序遍历：递归法
        """
        if data is None:
            return self.result
        else:
            self.middle__ergodic_recursion(data.left)
            self.result.append(data.val)
            self.middle__ergodic_recursion(data.right)      

    def afterword__ergodic_recursion(self, data):
        """
        后序遍历：递归法
        """
        if data is None:
            return self.result
        else:
            self.afterword__ergodic_recursion(data.left)
            self.afterword__ergodic_recursion(data.right)
            self.result.append(data.val)            

    def ergodic(self):
        """
        遍历二叉树
        """
        if self.is_empty():
            return "二叉树为空"
        else:
            # 递归法
            self.preorder_ergodic_recursion(self.root)  # 前序遍历
            print(self.result)
            self.result = list()
            self.middle__ergodic_recursion(self.root)  # 中序遍历
            print(self.result)
            self.result = list()
            self.afterword__ergodic_recursion(self.root)  # 后序遍历
            print(self.result)
            self.result = list()            
                  
   
if __name__ == '__main__':
    #   创建二叉树节点
    tree = BinaryTree()
    tree_root = TreeNode('F')
    treenode1_left = TreeNode('B')
    treenode1_right = TreeNode('G')
    treenode21_left = TreeNode('A')
    treenode22_left = TreeNode('D')
    # treenode21_right = TreeNode('None')
    treenode22_right = TreeNode('I')
    # treenode31_left = TreeNode('None')
    # treenode31_right = TreeNode('None')    
    treenode32_left = TreeNode('C')
    treenode32_right = TreeNode('E')
    treenode34_left = TreeNode('H')
    # treenode34_right = TreeNode('None')
    
    #   关联二叉树
    tree.root = tree_root
    tree_root.left = treenode1_left
    tree_root.right = treenode1_right
    treenode1_left.left = treenode21_left
    treenode1_left.right = treenode22_left
    # treenode1_right.left = treenode21_right
    treenode1_right.right = treenode22_right
    # treenode21_left.left = treenode31_left
    # treenode21_left.right = treenode31_right
    treenode22_left.left = treenode32_left
    treenode22_left.right = treenode32_right
    treenode22_right.left = treenode34_left
    # treenode22_right.right = treenode34_right        
    print(tree.is_empty())
    tree.ergodic()




