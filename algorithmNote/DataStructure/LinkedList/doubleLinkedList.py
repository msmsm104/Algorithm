# doubleLinkedList.py
# 이중 연결 리스트
from SampleNode import sampleNode


class DoubleLinkedList:
    def __init__(self):
        # 리스트의 맨 처음과 마지막은 실제 데이터를 저장하지 않는 노드입니다. (더미노드)
        self.head = sampleNode.Node()
        self.tail = sampleNode.Node()
        # 초기화
        # head 와 tail을 연결합니다.
        self.head.next = self.tail
        self.tail.prev = self.head
        # 데이터 개수를 저장할 변수
        self.d_size = 0

    # empty() 메서드 
    def empty(self):
        if self.d_size == 0:
            return True
        else:
            return False
        
    # size() 메서드
    def size(self):
        return self.d_size
    
    # add_first() 메서드 
    # new_node 의 prev, next 지정
    # 기존 연결리스트의 head.next.prev, head.next 지정
    def add_first(self, data):
        new_node = sampleNode.Node(data) # 새로운 노드 생성

        new_node.next = self.head.next
        new_node.prev = self.head

        self.head.next.prev = new_node
        self.head.next = new_node

        self.d_size += 1

    # add_last() 메서드
    # new_node의 prev, next 지정
    # 기존 연결리스트의 tail.prev.next, tail.prev 를 new_node로 지정
    def add_last(self, data):
        new_node = sampleNode.Node(data)

        new_node.prev = self.tail.prev
        new_node.next = self.tail

        self.tail.prev.next = new_node
        self.tail.prev = new_node

        self.d_size += 1

    def inser_after(self, data, node):
        new_node = sampleNode.Node(data)

        new_node.next = node.next
        new_node.prev = node

        node.next.prev = new_node
        node.next = new_node

        self.d_size += 1

    def insert_before(self, data, node):
        new_node = sampleNode.Node(data)

        new_node.prev = node.prev
        new_node.next = node

        node.prev.next = new_node
        node.prev = new_node

        self.d_size += 1

    # 요소를 탐색하는 연산
    def search_forward_all(self):
        cur = self.head.next

        while cur is not self.tail:
            print(cur.data, end = " ")
            cur = cur.next

    def search_forward(self, target):
        cur = self.head.next 

        while cur is not self.tail:
            if cur.data == target:
                return cur
            cur = cur.next
        return None
    
    def search_backward(self, target):
        cur = self.tail.prev

        while cur is not self.head:
            if cur.data == target:
                return cur
            cur = cur.prev
        return None
    
    # 삭제 연산
    def delete_first(self):
        if self.empty():
            return
        self.head.next = self.head.next.next
        self.head.next.prev = self.head

        self.d_size -= 1
    
    def delete_last(self):
        if self.empty():
            return
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail

        self.d_size -= 1

    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        self.d_size -= 1


if __name__=="__main__":
    a = DoubleLinkedList()

    a.add_last(1)
    a.add_last(2)
    a.add_last(3)
    a.add_last(5)

    a.inser_after(4, 3)

    a.search_forward_all()
    
        
        
    