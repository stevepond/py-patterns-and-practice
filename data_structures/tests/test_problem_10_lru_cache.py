from data_structures.problem_10_lru_cache import LRUCache


def test_lru_cache():
    cache = LRUCache(2)
    cache.put('a', 1)
    cache.put('b', 2)
    cache.get('a')
    cache.put('c', 3)
    assert cache.get('b') is None
    assert cache.get('a') == 1
