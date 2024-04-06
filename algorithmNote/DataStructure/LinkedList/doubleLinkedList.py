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