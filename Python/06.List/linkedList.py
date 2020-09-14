# List：
class Node(object):
  __data = {}
  __next = None

  def __init__(self, data, nextdata=None):
    self.__data = data
    self.__next = nextdata

  @property
  def data(self):
    return self.__data

  @data.setter
  def data(self, value):
    self.data = value

  @property
  def next(self):
    return self.__next

  @next.setter
  def next(self, value=None):
    self.__next = value

class LinkedList(object):
  __head = None

  def __init__(self, data = None):
    if not data:
      return Node(None)

    self.__head = self.initLinkedList(data)

  @property
  def head(self):
    return self.__head


  # Linked list with guard
  def initLinkedList(self, data):
    head = Node(None)  # Guard node
    curNode = head
    for d in data:
      node = Node(d)
      curNode.next = node
      curNode = node

    return head


  def gotoPos(self, pos):
    if pos < 0:
      return 0

    curNode = self.__head
    for i in range(pos):
      curNode = curNode.next

      if curNode.next is None:
        break

    return curNode


  def insertOneData(self, pos, d):
    curNode = self.gotoPos(pos)
    newNode = Node(d)
    newNode.next = curNode.next
    curNode.next = newNode


  def removeOneData(self, pos):
    listLen = self.length()
    if pos >= listLen:
      pos = listLen - 1

    curNode = self.gotoPos(pos)
    removedNode = curNode.next
    curNode.next = removedNode.next
    return removedNode.data


  def length(self):
    count = 0
    curNode = self.__head
    while curNode:
      count += 1
      curNode = curNode.next

    return count-1

  def output(self):
    curNode = self.__head.next
    print('head', end='')
    while curNode:
      print('->{}'.format(curNode.data), end='')
      curNode = curNode.next
    print('->None')


def main():
  data = [1, 2, 5, 0, 7]
  h = LinkedList(data)
  h.output()
  h.insertOneData(0, 9)
  h.output()
  h.removeOneData(0)
  h.output()


if __name__ == '__main__':
  main()
