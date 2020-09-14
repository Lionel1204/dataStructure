# List：
class Node(object):
  __data = {}
  __next = None
  __prev = None

  def __init__(self, data, nextdata=None, prevdata=None):
    self.__data = data
    self.__next = nextdata
    self.__prev = prevdata

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

  @property
  def prev(self):
    return self.__prev

  @prev.setter
  def prev(self, value=None):
    self.__prev = value


def initDoubleLinkedList(data):
  head = Node(None)  # Guard node
  curNode = head
  for d in data:
    node = Node(d)
    curNode.next = node
    node.prev = curNode
    curNode = node

  return head


def main():
  data = [1, 2, 5, 0, 7]
  h = initDoubleLinkedList(data)


if __name__ == '__main__':
  main()
