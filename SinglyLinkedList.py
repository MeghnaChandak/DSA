'''
@author: Meghna Chandak
@date: 13th April 2025
@goal: To implement singly linked list of integers
'''
def generic_exception_handler(trace = False):
    from sys import exc_info
    excName, excData, excTb = exc_info()
    print(excName, excData, sep = ":", flush = True)
    if trace is True:
        from traceback import print_tb
        print_tb(exc_tb)


class SNode:
    '''
    This class implements a node fro singly linked list and singly circular linked list
    '''
    def __init__(self,init_data):
        '''
        @input: 
            @init_data: integer to be stored in a newly allocated node
        Constructor creates two attributes in a newly allocated node
        viz. 1) 'data': initialized by local variable 'init_data'
             2) 'next': initialized to None. This is a self reference to the next in sequence node in a collection
        '''
        print("----Entered SNode.__init__()----")
        if type(init_data) != int and init_data is not None:
            raise TypeError(f'{init_data} is not of type int')
        self.data = init_data
        self.next = None
        print("SNode.__init__(): self.__dict__", self.__dict__)
        print("----Leaving SNode.__init__()----")


class SinglyLinkedList:
    '''
    This class implements singly linked list ADT.
    '''
    def __init__(self):
        '''
        An attribute named 'head_node will be created in a newly allocated object of class SinglyLInked LIst. The attribute name will be assigned to a newly allocated dummy node object of class SNode. (Note that the dummy node is the one whose 'data' attribute is None)
        '''
        print("----Entered SinglyLinkedList.__init__()----")
        self.head_node = SNode(None)
        print("SinglyLinkedList.__init__(): self.__dict__", self.__dict__)
        print("----Leaving SinglyLinkedList.__init__()----")
    
    def insert_start(self,newData: int):
        '''
        @input: 
            @newData: new data to be inserted at the starting position of the linked list
        new data will be encapsulated in a new SNode object and the newly allocated SNode object will be positioned at the beginning after the linked list(immediately next to the head node)
        '''

        print("----Entered SinglyLinkedList.insert_start()----")
        if type(newData) != int:
            raise TypeError(f'{newData} is not of type int')

        newNode = SNode(newData)
        newNode.next = self.head_node.next
        self.head_node.next = newNode

        print("----Leaving SinglyLinkedList.insert_start()----")
    
    def insert_end(self,newData: int):
        '''
        @input: 
            @newData: new data to be inserted at the ending position of the linked list
        new data will be encapsulated in a new SNode object and the newly allocated SNode object will be positioned at the beginning after the linked list(immediately next to the head node)
        '''

        print("----Entered SinglyLinkedList.insert_end()----")
        if type(newData) != int:
            raise TypeError(f'{newData} is not of type int')

        newNode = SNode(newData)
        run = self.head_node
        while run.next is not None:
            run = run.next
        run.next = newNode

        print("----Leaving SinglyLinkedList.insert_end()----")

    # def insert_after(self,prevData,newData: int):
        
    #     print("----Entered SinglyLinkedList.insert_after()----")
    #     if type(newData) != int:
    #         raise TypeError(f'{newData} is not of type int')

    #     newNode = SNode(newData)
    #     run = self.head_node.next
    #     while run is not None:
    #         if run.data == prevData:
    #             newNode.next = run.next
    #             run.next = newNode
    #             break
    #         run = run.next

    #     print("----Leaving SinglyLinkedList.insert_after()----")

    # def insert_before(self,prevData,newData: int):
    #     print("----Entered SinglyLinkedList.insert_before()----")
    #     if type(newData) != int:
    #         raise TypeError(f'{newData} is not of type int')

    #     newNode = SNode(newData)
    #     run = self.head_node
    #     while run is not None:
    #         if run.next.data == prevData:
    #             newNode.next = run.next
    #             run.next = newNode
    #             break
    #         run = run.next

    #     print("----Leaving SinglyLinkedList.insert_before()----")

    def show(self):
        '''
        Display the data members of all nodes except the head node
        '''

        print("----Entered SinglyLinkedList.show()----")
        
        print("[START] ->", end = " ")
        run = self.head_node.next
        while run is not None:
            print("[",run.data,"] ->", end = " ")
            run = run.next
        print("[END]")

        print("----Leaving SinglyLinkedList.show()----")
    
    # def search_node(self,searchData):
    #     print("----Entered SinglyLinkedList.search_node()----")
    #     if type(searchData) != int:
    #         raise TypeError(f'{searchData} is not of type int')
        
    #     run = self.head_node.next
    #     while run is not None:
    #         if run.data == searchData:
    #             break
    #         run = run.next
        
    #     print("----Leaving SinglyLinkedList.search_node()----")

    #     return run.data

        # run = self.head_node.next
        # while run is not None:
        #     if run.data == searchData:
        #         return run
        #     run = run.next
        # return None

    
    def search_node2(self,searchData):
        '''
            @input: searchData: data value to be searched
        a) Return the node containing first occurrence of searchData and the node previous to it.
        b) Return None if the searchData is not present
        '''
        print("----Entered SinglyLinkedList.search_node2()----")
        if type(searchData) != int:
            raise TypeError(f'{searchData} is not of type int')
        
        run_back = self.head_node
        run = self.head_node.next
        while run is not None:
            if run.data == searchData:
                return run_back.data, run.data
            run_back = run
            run = run.next
        return None,None

        print("----Leaving SinglyLinkedList.search_node2()----")
        
        # run = self.head_node
        # while run is not None:
        #     if run.next.data == searchData:
        #         return run,run.next
        #     run = run.next
        # return None
    
    def insert_after(self, existingData, newData):
        '''
        @input:
            @existingData: Datavalue which is supposed to be present in the list
            @newData: Data value that must be inserted after the first occurrence of the @existingData
        a) Inserts a newly allocated node containing @newData after the node containing the first occurrence of existingData.
        b) raise VlaueError if existingData not found
        '''
        existingNode, _ = self.search_node2(existingData)
        if existingNode is None:
            raise ValueError(f"SinglyLinkedList.insert_after(): existingData : {existingData} not found")
            
        newNode = SNode(newData)
        newNode.next = existingNode.next
        existingNode.next = newNode
    
    def insert_before(self, existingData, newData):
        '''
        @input:
            @existingData: Datavalue which is supposed to be present in the list
            @newData: Data value that must be inserted before the first occurrence of the @existingData
        a) Inserts a newly allocated node containing @newData before the node containing the first occurrence of existingData.
        b) raise VlaueError if existingData not found
        '''
        existingNode, existingNodePrev = self.searchNode2(existingData)
        if existingNode is None:
            raise ValueError(f"SinglyLinkedList.insert_after(): existingData : {existingData} not found")
        newNode = SNode(newData)
        existingNodePrev.next = newNode
        newNode.next = existingNode

    def get_start(self):
        '''
        a) Returns data value in the first node with data without removing the first node
        b) Raise ValueError if the list is empty
        '''
        if self.head_node.next is None:
            raise ValueError("get_start() cannot be applied on empty list")
        
        return self.head_node.next

    def get_end(self):
        '''
        a) Returns data value in the first node with data without removing the first node
        b) Raise ValueError if the list is empty
        '''
        if self.head_node.next is None:
            raise ValueError("get_start() cannot be applied on empty list")
        
        run = self.head_node
        while run.next is not None:
            run = run.next
        return run.data

    def pop_start(self):
        '''
        a) Returns data value in the first node with data without removing the first node
        b) Raise ValueError if the list is empty
        '''
        if self.head_node.next is None:
            raise ValueError("get_start() cannot be applied on empty list")

        firstNode = self.head_node.next
        firstData = fisrtNode.data
        self.head_node.next = firstNode.next
        del firstNode
        return firstData

    def pop_end(self):
        '''
        a) Returns data value in the first node with data without removing the first node
        b) Raise ValueError if the list is empty
        '''
        if self.head_node.next is None:
            raise ValueError("get_start() cannot be applied on empty list")
        
        run_back = self.head_node
        run = self.head_node.next
        while run is not None:
            run_back = run
            run = run.next
        
        lastNode = run
        lastData = lastNode.data
        run_back.next = None
        del lastNode
        return lastData
    
    def remove_start(self):
        '''
        a) Removes the first node with data in the list
        b) Raise ValueError if list is empty
        '''
        if self.head_node.next is None:
            raise ValueError("get_start() cannot be applied on empty list")

        firstNode = self.head_node.next
        self.head_node.next = firstNode.next
        del firstNode
    
    def remove_end(self):
        '''
        a) Removes the first node with data in the list
        b) Raise ValueError if list is empty
        '''
        if self.head_node.next is None:
            raise ValueError("get_start() cannot be applied on empty list")
        
        run_back = self.head_node
        run = self.head_node.next
        while run.next is not None:
            run_back = run
            run = run.next
        
        run_back.next = None
        lastNode = run
        del lastNode

    def remove_data(self,rData):
        '''
        @input: 
            @rData: Data value whose first occurrence within linked list must be removed
        a) Removes the first node with data in the list
        b) Raise ValueError if @rdata is not present in the list
        '''

        rNode, rNodePrev = self.search_node2(rData)
        if rNode is None:
            raise ValueError(f"Data to be removed {rData} is not present in the list")
        
        rNodePrev.next = rNode.next
        del rNode

    def find(self, fData):
        '''
        @input: 
            @fData: Data value to be searched in the list
        a) Returns True if @fData is present in the list and False otherwise
        '''
        fNode, _ = self.search_node2(fData)
        if fNode is not None:
            return True
        else:
            return False

    def length(self):
        '''
        Returns the number of data nodes in the list
        '''
        ptr = 0
        run = self.head_node.next
        while run is not None:
            ptr = ptr + 1
            run = run.next
        return ptr

    def isEmpty(self):
        '''
        Returns whether or not the calling list object is empty
        '''
        if self.head_node.next is None:
            return True
        else:
            return False

#Client Side
#Create a new object of class SinglyLinkedList for testing purpose
print("----------START---------")
print("\n Creating a new SinglyLinkedList object \n")
L = SinglyLinkedList()

print("\n Testing get_start() on empty list \n")
try: 
    L.get_start()
except:
    generic_exception_handler()

print("\n Testing get_end() on empty list \n")
try: 
    L.get_end()
except:
    generic_exception_handler()

print("\n Testing pop_start() on empty list \n")
try: 
    L.pop_start()
except:
    generic_exception_handler()

print("\n Testing pop_end() on empty list \n")
try: 
    L.pop_end()
except:
    generic_exception_handler()

print("\n Testing remove_start() on empty list \n")
try: 
    L.remove_start()
except:
    generic_exception_handler()

print("\n Testing remove_end() on empty list \n")
try: 
    L.remove_end()
except:
    generic_exception_handler()

print("\n Testing length() on empty list")
n = L.length()
print("Length of list : ",n)

print("\n Testing isEmpty() on empty list")
b = L.isEmpty()
print("L is empty : ",b)

print("\n Testing insert_start() \n")
L.insert_start(200)
L.insert_start(100)
L.show()

print("\n Testing insert_end() \n")
L.insert_end(300) 
L.insert_end(400)
L.show()

print("\n Testing search_node() \n")
#print(L.search_node(200))
print(L.search_node2(100))

print("\n Testing insert_after() for non-existent data \n")
try:
    L.insert_after(-50, 1000)
except:
    generic_exception_handler()

print("\n Testing insert_after() for middle node \n")
L.insert_after(200, 250)
L.show()

print("\n Testing insert_after() for the last node \n")
L.insert_after(400,450)
L.show()

print("\n Testing insert_before() for non-existent data \n")
try:
    L.insert_before(-50, 1000)
except:
    generic_exception_handler()

print("\n Testing insert_before() for middle node \n")
L.insert_before(200, 150)
L.show()

print("\n Testing insert_before() for the first node \n")
L.insert_before(100,50)
L.show()

print("\n Testing getStart() and getEnd() on non-empty list")
firstData = L.get_start()
lastData = L.get_end()
print(f' First Data : {firstData} and Last Data : {lastData}')
print("Showing list after L.get_start() and L.get_end() to prove that start and end nodes are not removed")
L.showList()

print('Testing pop_start() and pop_end() on non-empty list')
firstData = L.pop_start() 
lastData = L.pop_end() 
print(f'First Data:{firstData}, Last Data:{lastData}')
print("Showing list after L.pop_start() and L.pop_end() to prove that start and end nodes are removed")
L.showList()

print("\n Testing remove_start() and remove_end() on non-empty list\n")
L.remove_start()
L.show()
L.remove_end()
L.show()

print("\n Testing remove_data() on existing data value \n")
try:
    remove_data(350)
except:
    generic_exception_handler()

print("\n Testing remove_data() on the middle node \n")
L.remove_data(250)
L.show()

print("\n Testing remove_data() on the first node \n")
L.remove_data(50)
L.show()

print("\n Testing remove_data() on the last node \n")
L.remove_data(450)
L.show()

print("\n Testing find() on non-existing data value \n")
try:
    find(450)
except:
    generic_exception_handler()

print("\n Testing find() on the middle node \n")
ans = L.find(200)
print(f"200 is present in the list : {ans}")

print("\n Testing find() on the first node \n")
ans = L.remove_data(100)
print(f"100 is present in the list : {ans}")

print("\n Testing find() on the last node \n")
ans = L.remove_data(200)
print(f"400 is present in the list : {ans}")

print("\n Testing length() on non-empty list")
n = L.length()
print("Length of list : ",n)

print("\n Testing isEmpty() on non-empty list")
b = L.isEmpty()
print("L is empty : ",b)

print("--------END---------")