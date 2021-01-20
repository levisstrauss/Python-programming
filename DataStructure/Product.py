class Product:

    def __init__(self, title, rating, isDealOfDay, price, isPrime, nextProduct):
        self.title = title
        self.rating = rating
        self.isDealOfDay = isDealOfDay
        self.price = price
        self.isPrime = isPrime
        self.nextProduct = nextProduct


class Node:

    def __init__(self, num, nextNode):
        self.num = num
        self.nextNode = nextNode


class LinkedList:
    # Is Property of Class
    head = None
    tail = None
    __size = 0

    def appendBack(self, object):

        LinkedList.__size += 1
        node = Node(object, None)

        if LinkedList.head is None:
            LinkedList.head = node
            LinkedList.tail = node

        else:
            LinkedList.tail.nextNode = node
            LinkedList.tail = node
        print()

    def appendFront(self, object):

        LinkedList.__size += 1
        node = Node(object, None)

        if LinkedList.head is None:
            LinkedList.head = node
            LinkedList.tail = node

        else:
            node.nextNode = LinkedList.head
            LinkedList.head = node
        print()

    def printList(self):

        temp = LinkedList.head

        while temp.nextNode is not None:
            print(temp.num)
            temp = temp.nextNode

        print(temp.num)

    def size(self):
        return LinkedList.__size


# Lets Create Node Object
# node = Node(85, None)

# Object of LinkedList
lRef = LinkedList()
lRef.appendBack(85)
lRef.appendBack(100)
lRef.appendFront(5)
lRef.appendFront(200)

lRef.printList()

print(">> Size of Linked List is:", lRef.size())
