#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
二叉树的前、中、后序遍历(迭代解法)

Author: GrantLi

"""

import traceback


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
    
    def preorder_ergodic_recursion(self, root):
        """
        前序遍历(迭代法)：先遍历根节点，然后遍历左子树，最后遍历右子树
        步骤：
        1.初始化栈，并将根节点入栈;
        2.当栈不为空时:
        (1)弹出栈顶元素node,并将值添加到结果中;
        (2)如果node的右子树非空,将右子树入栈;
        (3)如果node的左子树非空,将左子树入栈;
        3.由于栈是“先进后出”的顺序,入栈时先将右子树入栈,结果为“根->左->右”的顺序。
        """
        if not root:
            return []
        #   初始化栈(将节点转换成列表)
        stack, res = [root], []
        # traceback.print_stack()
        while stack:
            #   弹出栈顶元素
            node = stack.pop()
            # print(node.val, node.left, node.right)
            if node:
                res.append(node.val)
                #   右
                if node.right:
                    stack.append(node.right)
                #   左
                if node.left:
                    stack.append(node.left)
        return res

            
    def middle__ergodic_recursion(self, root):
        """
        中序遍历(迭代法):先遍历左子树再遍历根节点再遍历右子树
        步骤：
        1.初始化栈，并将根节点入栈;
        2.当栈不为空时:
        (1)弹出栈顶元素node,并将节点tmp的值加入到结果中;
        (2)如果node的右子树非空,将右子树入栈;
        (3)如果node的左子树非空,将左子树入栈;
        3.由于栈是“先进后出”的顺序,入栈时先将右子树入栈,结果为“左->根->右”的顺序。
        """
        if not root:
            return []
        cur, stack, res = root, [], []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left  #   左
            #   弹出栈顶元素
            tmp = stack.pop()
            res.append(tmp.val)
            cur = tmp.right #   右
        return res
 

    def afterword__ergodic_recursion(self, root):
        """
        后序遍历(迭代法):先遍历左子树再遍历右子树再遍历根节点
        步骤：
        1.初始化栈，并将根节点入栈;
        2.当栈不为空时:
        (1)弹出栈顶元素node和flag;
        (2)如果flag为1,将节点的值加入到结果中;
        (3)如果flag为0,将flag变为1并连同该节点再次入栈;
        3.由于栈是“先进后出”的顺序,入栈时先将根子树入栈,结果为“左->右->根”的顺序。
        """
        if not root:
            return []
        stack, res = [(0, root)], []

        while stack:
            #   弹出栈顶元素
            flag, node = stack.pop()
            if not node:
                continue
            #   遍历完之后加入到结果里
            if flag == 1:
                res.append(node.val)
            else:
                stack.append((1, node)) 
                stack.append((0, node.right))   #   右
                stack.append((0, node.left))    #   左
        return res       

    def ergodic(self):
        """
        遍历二叉树
        """
        if self.is_empty():
            return "二叉树为空"
        else:
            # 递归法
            self.result = self.preorder_ergodic_recursion(self.root)  # 前序遍历
            print(self.result)
            self.result = list()
            self.result = self.middle__ergodic_recursion(self.root)  # 中序遍历
            print(self.result)
            self.result = list()
            self.result = self.afterword__ergodic_recursion(self.root)  # 后序遍历
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




