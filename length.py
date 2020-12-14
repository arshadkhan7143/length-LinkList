
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
#  iteratitve approach
def lengthLink(head):
    temp = head
    count = 0
    while(temp is not None):
        temp = temp.next
        count = count + 1
    return count
# recursive approach
def lengthLinkRecurr(node):
    if (node == None):
        return 0
    return 1 + lengthLinkRecurr(node.next)

def printList(head):
    temp = head
    while(temp is not None):
        print(temp.data)
        temp =temp.next

head = Node('a')
nodeB =Node('b')
nodeC =Node('c')
nodeD =Node('d')
nodeE =Node('e')
nodeF =Node('f')

head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF
nodeF.next = None

printList(head)
print("count is",lengthLink(head))
print("-----------")
printList(head)
print("count is",lengthLinkRecurr(head))