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


def initCircularList(data):
  head = Node(None)  # Guard node
  curNode = head
  for d in data:
    node = Node(d)
    curNode.next = node
    curNode = node

  curNode.next = head.next
  return head


def main():
  data = [1, 2, 5, 0, 7]
  h = initCircularList(data)


if __name__ == '__main__':
  main()
