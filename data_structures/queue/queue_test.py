import pytest
from queue import Queue


def construct_queue(l):
    q = Queue()
    for elem in l:
        q.enqueue(elem)
    return q


@pytest.mark.parametrize('init, ops, enqueue, output', [
    ([], [0], [], []),
    ([], [1], [1], [1]),
    ([], [1, 1, 1], [1, 2, 3], [1, 2, 3]),
    ([], [1, 1, 1, 0, 0], [1, 2, 3], [3]),
    ([], [0, 0, 1, 1, 0], [1, 2], [2])
])
def test_queue(init, ops, enqueue, output):
    queue = construct_queue(init)
    enqueue_index = 0
    for elem in ops:
        if elem:
            queue.enqueue(enqueue[enqueue_index])
            enqueue_index += 1
        else:
            queue.dequeue()
    assert queue.queue == output
