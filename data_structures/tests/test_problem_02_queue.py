from data_structures.problem_02_queue import Queue


def test_queue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.is_empty()
