from collections import defaultdict
import heapq


def fun(flights, src, dst, K):
    hash_map = defaultdict(list)
    for flight in flights:
        hash_map[flight[0]].append((flight[1], flight[2]))
    pq = [(0, src, -1)]

    while pq:
        weight, source, k = heapq.heappop(pq)
        if source == dst:
            return weight
        if k >= K:
            continue
        for flight in hash_map[source]:
            heapq.heappush(pq, (flight[1] + weight, flight[0], k + 1))

    return -1


def dijksra(flights, src, dst, K):
    """
    Original dijksra solution. This does not work for test because of K
    :param flights:
    :param src:
    :param dst:
    :param K:
    :return:
    """
    graph = defaultdict(list)
    for x, y, val in flights:
        graph[x].append((y, val))

    seen = set()
    heap = [(0, src, -1)]

    while heap:
        val, x, depth = heapq.heappop(heap)
        seen.add(x)
        if x == dst and depth <= K:
            return val
        for y, y_val in graph[x]:
            if y not in seen:
                heapq.heappush(heap, (val+y_val, y, depth+1))

    return -1


print(fun([[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))