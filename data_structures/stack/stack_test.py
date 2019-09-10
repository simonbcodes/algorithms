import pytest
from stack import Stack

@pytest.fixture
def empty_stack():
    """Return an empty Stack."""
    return Stack()


def construct_stack(l):
    """Construct a stack given a list."""
    s = Stack()
    for elem in l:
        s.push(elem)
    return s


@pytest.mark.parametrize('init, ops, push, output', [
    ([1,2,3], [1], [10], [1,2,3,10]),
    ([1,2,3], [0], [], [1,2]),
    ([], [1], [None], []),
    ([], [0], [], []),
    ([], [1,1,1], [10,20,30], [10, 20, 30]),
    ([1,2,3], [0,0,0,0], [], []),
    ([1,2,3], [1,0,1,1,0], [10, 20, 30], [1,2,3,20])
])
def test_stack(init, ops, push, output):
    """Test the Stack implementation using pytest paramterization.
        Parameters:
        -----------
        init: list
            List used to initialize the stack. Each element is pushed to the stack.
        ops: list
            List of operations to carry out on the stack. 1 is push, 0 is pop.
        push: list
            List of elements to push to the list for testing.
        output: list
            Expected list after operations are carried out.
    """
    stack = construct_stack(init)
    push_index = 0
    for operation in ops:
        if operation:
            stack.push(push[push_index])
            push_index += 1
        else:
            stack.pop()
    assert stack.stack == output
