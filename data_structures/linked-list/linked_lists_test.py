import pytest
from singly_linked_list import LinkedList, Node


@pytest.fixture
def empty_linked_list():
    """Return an empty LinkedList."""
    return LinkedList()


@pytest.fixture
def initialized_linked_list():
    """Return a LinkedList with an initialized head."""
    return LinkedList(10)


def construct_linked_list(l):
    """Construct a linked list given a list."""
    ll = LinkedList()
    for i in l:
        ll.append(i)
    return ll


def ll_to_list(ll):
    """Convert a LinkedList into a list"""
    list = []
    cur = ll.head
    while cur is not None:
        list.append(cur.data)
        cur = cur.next
    return list


@pytest.fixture
def one_to_ten_linked_list():
    """ Return a LinkedList with Nodes from 1 to 10. """
    ll = LinkedList
    for val in [i for i in range(0, 11)]:
        ll.append(val)
    return ll


def test_empty_linked_list(empty_linked_list):
    assert empty_linked_list.head is None


def test_initialized_linked_list(initialized_linked_list):
    assert initialized_linked_list.head.data == 10


@pytest.mark.parametrize('init, delete, output', [
    ([], 1, []),
    ([1], 1, []),
    ([1], 2, [1]),
    ([1, 2], 1, [2]),
    ([1, 2], 2, [1]),
    ([1, 2], 3, [1, 2]),
    ([1, 2, 3], 1, [2, 3]),
    ([1, 2, 3], 2, [1, 3]),
    ([1, 2, 3], 3, [1, 2]),
    ([1, 2, 3], 4, [1, 2, 3])
])
def test_delete_by_value(init, delete, output):
    ll = construct_linked_list(init)
    ll.delete_by_value(delete)
    assert ll_to_list(ll) == output
