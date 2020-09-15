from linkedList import LinkedList

class LRUCache(object):
  __MAX_LEN = 1000

  def __init__(self):
    self.__l = LinkedList()


  def isFull(self):
    return self.__l.length() >= self.__MAX_LEN


  # callback should be: fun(key) -> value
  def getData(self, key, callback):
    curNode = self.__l.head  # first node
    pos = 0
    while curNode:
      if curNode.data and key in curNode.data.keys():
        self.__l.removeOneData(pos)
        self.__l.insertOneData(0, curNode.data)
        return curNode.data[key]
      else:
        curNode = curNode.next

      pos += 1
    else:
      data = callback(key)
      self.setData({key: data})
      return data


  # data = {key: value}
  def setData(self, data):
    if self.isFull():
      self.__l.removeOneData(self.__MAX_LEN)

    self.__l.insertOneData(0, data)


  def outputAll(self):
    self.__l.output()

def fallback(key):
  d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
  return d[key]

def main():
  c = LRUCache()
  v = c.getData('a', fallback)
  print(v)
  print(c.outputAll())
  v = c.getData('b', fallback)
  print(v)
  print(c.outputAll())
  v = c.getData('c', fallback)
  print(v)
  print(c.outputAll())
  v = c.getData('a', fallback)
  print(v)
  print(c.outputAll())


if __name__ == '__main__':
  main()