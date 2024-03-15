import heapq


def heapsort(list):
    heap = []
    for item in list:
        heapq.heappush(heap, item)
    return [heapq.heappop(heap) for i in range(len(heap))]


def get_median(m_list):
    sorted_list = heapsort(m_list)

    mid_index = len(sorted_list) // 2
    median = sorted_list[mid_index]
    if len(sorted_list) % 2 == 0:
        median = (sorted_list[mid_index-1] + sorted_list[mid_index]) / 2

    return median


test_list = [4, 5, 8, 9, 10]
print(get_median(test_list))
