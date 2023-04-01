#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
二叉树的层次遍历(队列解法)
步骤为：
1.初始化队列 q,并将根节点root加入到队列中;
2.当队列不为空时:
(1)队列中弹出节点node,加入到结果中;
(2)如果左子树非空,左子树加入队列;
(3)如果右子树非空,右子树加入队列；

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
    
    def level_ergodic_recursion(self, root):
        """
        层次遍历：队列方式
        """
        if not root:
            return []
        q, res = [root], []
        while q:
            n = len(q)
            level = []
            for i in range(n):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)

        return res


    def ergodic(self):
        """
        遍历二叉树
        """
        if self.is_empty():
            return "二叉树为空"
        else:
            # 递归法
            self.result = self.level_ergodic_recursion(self.root)  # 前序遍历
            print(self.result)
       
                  
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




