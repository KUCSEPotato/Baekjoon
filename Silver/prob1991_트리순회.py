# ---------------------------------------------------------------------------------------------------- #
# https://www.acmicpc.net/problem/1991
# 문제
# 이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다.
# 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.

# 출력
# 첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.
# ---------------------------------------------------------------------------------------------------- #
CharSet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Node:
    def __init__(self, value: str):
        self.is_root = False
        self.left = None
        self.right = None
        self.value = value

    def __repr__(self):
        return self.value

class BinaryTree:
    def __init__(self, root: Node):
        self.root = root
    
    def __repr__(self):
        return f"Root Node({self.root})"
    
    def _PreorderTraversal(self, node: Node):
        if node is None:
            return
        
        print(node, end="")
        self._PreorderTraversal(node=node.left)
        self._PreorderTraversal(node=node.right)

    def _InorderTraversal(self, node: Node):
        if node is None:
            return
        
        self._InorderTraversal(node=node.left)
        print(node, end="")
        self._InorderTraversal(node=node.right)

    def _PostorderTraversal(self, node: Node):
        if node is None:
            return
        
        self._PostorderTraversal(node=node.left)
        self._PostorderTraversal(node=node.right)
        print(node, end="")

    # Public API Function
    def preorder(self):
        self._PreorderTraversal(self.root)
    
    def inorder(self):
        self._InorderTraversal(self.root)

    def postorder(self):
        self._PostorderTraversal(self.root)

def main():
    N = int(input())
    tree_info = {CharSet[i]: [] for i in range(N)}

    for _ in range(N):
        parent, left, right = input().split()
        tree_info[parent].append(left)
        tree_info[parent].append(right)

    nodes = {CharSet[i]: Node(CharSet[i]) for i in range(N)}

    for j in range(N):
        ch = CharSet[j]
        left = tree_info[ch][0]
        right = tree_info[ch][1]

        if j == 0: nodes[ch].is_root = True
        if left != ".": nodes[ch].left = nodes[left]
        if right != ".": nodes[ch].right = nodes[right]

    BT = BinaryTree(nodes['A'])
    BT.preorder()
    print()
    BT.inorder()
    print()
    BT.postorder()

if __name__ == "__main__":
    main()
