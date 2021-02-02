from singly_linked_list import SinglyLinkedList, Node


def test_new_linked_list():
   new_list = SinglyLinkedList()
   assert new_list.head == None
   assert new_list.tail == None


def test_new_linked_list_with_head():
    new_list = SinglyLinkedList()
    new_list.addAtHead(5)
    assert new_list.head.val == 5
    assert new_list.tail.val == 5
    assert new_list.length == 1 

def test_linked_list_with_head_add_tail():
    new_list = SinglyLinkedList()
    new_list.addAtHead(5)
    new_list.addAtTail(6)
    assert new_list.head.val == 5    
    assert new_list.tail.val == 6
    assert new_list.head.next.val == 6 
    assert new_list.length == 2

def test_get_head_tail_val():
    new_list = SinglyLinkedList()
    new_list.addAtHead(5)
    new_list.addAtTail(6)
    assert new_list.get(0) == 5
    assert new_list.get(1) == 6


def test_get_middel_values():
    new_list = SinglyLinkedList()
    new_list.addAtHead(3)
    new_list.addAtHead(2)
    new_list.addAtTail(5)
    new_list.addAtTail(6)
    
    assert new_list.get(1) == 3
    assert new_list.get(2) == 5
    

def test_linked_list_insert_invalid_index():
    new_list = SinglyLinkedList()
    new_list.addAtHead(5)
    new_list.addAtTail(6)
    assert new_list.addAtIndex(4,10) == None
    assert new_list.length == 2 
    
def test_linked_list_insert_middle_index():
    new_list = SinglyLinkedList()
    new_list.addAtHead(4)
    new_list.addAtTail(6)
    
    new_list.addAtIndex(1,5)
    assert new_list.head.val == 4
    assert new_list.tail.val == 6
    assert new_list.head.next.val == 5
    assert new_list.head.next.next.val == 6
    assert new_list.length == 3 

def test_linked_list_one_element_delete_head():
    new_list = SinglyLinkedList()
    new_list.addAtHead(4)    
    
    new_list.deleteAtIndex(1)        
    assert new_list.length == 1


def test_linked_list_delete_head():
    new_list = SinglyLinkedList()
    new_list.addAtHead(4)
    new_list.addAtTail(6)
    
    new_list.deleteAtIndex(0)
    assert new_list.head.val == 6
    assert new_list.tail.val == 6    
    assert new_list.length == 1 

def test_linked_list_delete_tail():
    new_list = SinglyLinkedList()
    new_list.addAtHead(4)
    new_list.addAtTail(5)
    new_list.addAtTail(6)
    
    new_list.deleteAtIndex(2)
    assert new_list.head.val == 4
    assert new_list.tail.val == 5    
    assert new_list.length == 2 

def test_linked_list_delete_middle():
    new_list = SinglyLinkedList()
    new_list.addAtHead(4)
    new_list.addAtTail(5)
    new_list.addAtTail(6)
    
    new_list.deleteAtIndex(1)
    assert new_list.head.val == 4
    assert new_list.tail.val == 6    
    assert new_list.length == 2
    

def test_linked_list_delete_middle():    
    new_list = SinglyLinkedList()
    new_list.addAtHead(7)
    new_list.addAtHead(2)
    new_list.addAtHead(1)
    new_list.addAtIndex(3,0)
    new_list.deleteAtIndex(2)    
    new_list.addAtHead(6)
    new_list.addAtTail(4)
        
    assert new_list.head.val == 6
    assert new_list.tail.val == 4    
    assert new_list.length == 4
    assert new_list.get(4) == 4
    

def test_custom_operations():    
    new_list = SinglyLinkedList()    
    new_list.addAtIndex(0,10)
    new_list.addAtIndex(0,20)
    new_list.addAtIndex(1,30)
        
    assert new_list.head.val == 20
    assert new_list.tail.val == 10    
    assert new_list.length == 3
    assert new_list.get(0) == 20
    