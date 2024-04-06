# doubleLinkedList.py
# 이중 연결 리스트
from SampleNode import node


class DoubleLinkedList:
    def __init__(self):
        # 리스트의 맨 처음과 마지막은 실제 데이터를 저장하지 않는 노드입니다. (더미노드)
        self.head = node.Node()
        self.tail = node.Node()
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
        new_node = node.Node(data) # 새로운 노드 생성

        new_node.prev = self.head
        new_node.next = self.head.next

        self.head.next = new_node
        self.head.next.prev = new_node

        self.d_size += 1

    