import heapq

class PriorityQueue:
    def __init__(self) -> None:
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def __str__(self) -> str:
        return str(self.elements)


if __name__ == "__main__":
    pq = PriorityQueue()

    print(pq.is_empty())

    pq.put("eat",2)
    pq.put("code",3)
    pq.put("wake up",1)
    print(pq.get())
    print(pq.get())
    print(pq.get())