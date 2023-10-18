from dataclasses import dataclass
@dataclass
class Node:
    value: int
    prev_node: None
    next_node: None

@dataclass
class doubly_Ordered_List:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of
list)'''
    head: 'Node' = None
    tail: 'Node' = None

    def is_empty(self):
        if self.head == None and self.tail == None:
            return True
        return False

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
        from lowest (at head of list) to highest (at tail of list) and returns True.
        If the item is already in the list, do not add it again and return False.
        MUST have O(n) average-case performance'''
        pass
    def remove(self, item):
                if self.is_empty():
            return False
        current_node = self.head
        if self.head.value == item:
            if self.head.next_node is not None:
                self.head = current_node.next_node
                current_node.next_node = None
                current_node.prev_node = None
                return True
            self.head.prev_node = None
            self.head.next_node = None
            return True
        while current_node is not None:
            if current_node.value == item:
                if current_node == self.tail:
                    current_node.prev_node.next_node = None
                    self.tail = current_node.prev_node
                    current_node.next_node = None
                    current_node.prev_node = None
                    return True
                current_node.prev_node.next_node = current_node.next_node
                current_node.next_node.prev_node = current_node.prev_node
                current_node.next_node = None
                current_node.prev_node = None
                return True
            current_node = current_node.next_node
        return False
    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of
        list is index 0).
        If item is not in list, return None
        MUST have O(n) average-case performance'''
        current_node = self.head
        index = 0
        while current_node is not None:
            if current_node.value == item:
                return index
            else:
                index = index + 1
                current_node = current_node.next_node
        return None
        
    def pop(self, index):
        if index<0:
            return "Error"
        current_node = self.head
        for i in range(0, index):
            current_node = current_node.next_node
        temp = current_node
        self.remove(current_node)
        return temp
    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
        To practice recursion, this method must call a RECURSIVE method that
        will search the list
        MUST have O(n) average-case performance'''
        current_node = self.head
        self.search_recurve(item, current_node)

    def search_recurve(self, item, next_node):
        if next_node.next_node is None:
            return False

        if next_node.value == item:
            return True
        else:
            next_node = next_node.next_node
            self.search_recurve(item, next_node)
    
    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
        For example, list with integers 1, 2, and 3 would return [1, 2, 3]
        MUST have O(n) performance'''
        current_node = self.head
        list = []
        while current_node is not None:
            list.append(current_node.value)
            current_node = current_node.next_node
        return list
        
    def python_list_reversed_recursive(self, my_list, current_node):
        if current_node is None:
            return my_list, current_node
        else:
            my_list.append(current_node.value)
            current_node=current_node.prev_node
            return my_list, current_node

    def python_list_reversed(self):
        my_list = []
        python_list_reversed_recursive(my_list, self.tail)
        return my_list
        
    def size(self):
        '''Returns number of items in the OrderedList
        To practice recursion, this method must call a RECURSIVE method that
        will count and return the number of items in the list
        MUST have O(n) performance'''
        pass
