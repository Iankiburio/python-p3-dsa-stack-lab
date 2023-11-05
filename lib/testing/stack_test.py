from Stack import Stack

class TestStack:
    '''Class Stack in Stack.py'''

    def test_init(self):
        '''Initialize Stack with list'''
        stk = Stack([1,2,3,4,5])
        expected = [1,2,3,4,5]
        for index in range(len(expected)):
            assert expected[index] == stk.stack[index]

    def test_push(self):
        '''Push 0 to stack'''
        stk = Stack([1,2,3,4,5])
        stk.push(0)
        expected = [1,2,3,4,5,0]
        for index in range(0,len(expected)):
            assert expected[index] == stk.stack[index]

    def test_pop(self):
        '''Pop 1 off the stack'''
        stk = Stack([1,2,3,4,5])
        stk.pop()
        expected = [1,2,3,4]
        for index in range(len(expected)):
            assert expected[index] == stk.stack[index]

    def test_size(self):
        '''Test Stack size() method'''
        stk = Stack([1,2,3,4,5])
        expected = [1,2,3,4,5]
        assert stk.size() == len(expected)

    def test_empty(self):
        '''Test Stack empty() method'''
        stk = Stack()
        assert stk.empty() == True
        assert stk.size() == 0
        assert stk.pop() == None
        stk.push(1)
        assert stk.empty() == False
        assert stk.size() == 1
        assert stk.pop() == 1

    def test_full(self):
       '''Test Stack full() method'''
       stk = Stack([])  # Pass an empty list as the initial stack
       assert stk.full() == False  # Stack should not be full initially
       assert stk.size() == 0      # Check if the size is 0


    def test_search(self):
        '''Test Stack search() method. How far is the element in the stack? '''
        stk = Stack([5,6,7,8,9,10])
        assert stk.search(5) == 6  # The element is at the top of the stack
        assert stk.search(6) == 5  # The element is one position below the top
        assert stk.search(7) == 4  # The element is two positions below the top
        assert stk.search(8) == 3
        assert stk.search(9) == 2
        assert stk.search(10) == 1
        # Case with target not in Stack
        assert stk.search(15) == -1

