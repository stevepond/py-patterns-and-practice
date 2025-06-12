from data_structures.problem_17_cycle_linked_list import Node, has_cycle


def test_has_cycle():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.next = b
    b.next = c
    c.next = a
    assert has_cycle(a)
    c.next = None
    assert not has_cycle(a)
