import pytest
from stack import Stack

def test_stack_creation():
    """Test that a new stack is empty"""
    s = Stack()
    assert s.is_empty() == True
    assert s.size() == 0

def test_push_and_peek():
    """Test pushing items and peeking at the top"""
    s = Stack()
    s.push("apple")
    assert s.is_empty() == False
    assert s.size() == 1
    assert s.peek() == "apple"
    
    s.push("banana")
    assert s.size() == 2
    assert s.peek() == "banana"  # Last item in should be at top

def test_pop():
    """Test popping items from the stack"""
    s = Stack()
    s.push("first")
    s.push("second")
    s.push("third")
    
    # Test LIFO order (Last-In, First-Out)
    assert s.pop() == "third"
    assert s.pop() == "second"
    assert s.pop() == "first"
    assert s.is_empty() == True
    assert s.size() == 0

def test_pop_empty_stack():
    """Test that popping from empty stack raises error"""
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()

def test_peek_empty_stack():
    """Test that peeking empty stack raises error"""
    s = Stack()
    with pytest.raises(IndexError):
        s.peek()

def test_size_after_operations():
    """Test size changes correctly after operations"""
    s = Stack()
    assert s.size() == 0
    
    s.push("item1")
    s.push("item2")
    assert s.size() == 2
    
    s.pop()
    assert s.size() == 1
    
    s.pop()
    assert s.size() == 0
