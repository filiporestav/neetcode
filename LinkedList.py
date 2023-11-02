class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0
    
    def get(self, index: int) -> int:
        if (index >= self.length or index < 0):
            return -1
        
        # Iterate through the linked list
        currNode = self.head
        i=0
        while (i < index):
            currNode = currNode.next
            i+=1
        return currNode.val

    def insertHead(self, val: int) -> None:
        newHead = Node(val)
        newHead.next = self.head
        self.head = newHead
        if self.tail is None:
            self.tail = self.head
        self.length+=1

    def insertTail(self, val: int) -> None:
        newTail = Node(val)
        if self.tail:
            self.tail.next = newTail # Pointing previous tail to the new tail
        else: 
            self.head = newTail
        self.tail = newTail # Changing the tail to the new tail
        self.length+=1

    def remove(self, index: int) -> bool:
        if index >= self.length:
            return False
        
        if index == 0:
            self.head = self.head.next
            self.length-=1
            if self.length==0:
                self.tail = None # Update the tail when the last element is removed
            return True
        
        prevNode = self.head
        currNode = prevNode.next
        counter = 1
        while (counter<index):
            prevNode = currNode
            currNode = currNode.next
            counter+=1

        # Moving the elements in the linked list
        prevNode.next = currNode.next
        if index == self.length-1:
            self.tail = prevNode # Update the tail when the last element is removed
        self.length-=1
        return True

    #  return an array of all the values in the linked list, ordered from head to tail.
    def getValues(self) -> List[int]:
        intList = []
        currNode = self.head
        while currNode:
            intList.append(currNode.val)
            currNode = currNode.next
        return intList
            

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None