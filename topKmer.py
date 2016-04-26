import random
import heapq


def randomStream(seed=0):
    while True:
        yield round(random.random(), 4)

data = []
heap = []
k = 5
n = 0

for r in randomStream():
    data.append(r)
    if len(heap) < k:
        heapq.heappush(heap, r)
    else:
        hpmin = heapq.nsmallest(1, heap)

        if r > hpmin[0]:
            heapq.heappushpop(heap, r)

    n += 1
    if n % 100 == 0:
        break

print sorted(heap)
print sorted(data)[-5:]
