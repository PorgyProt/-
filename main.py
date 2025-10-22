import heapq
import sys


def merge(in_fn, out_fn):
    with open(in_fn, 'r') as f:
        n = int(f.readline().strip())
        lists = []
        for _ in range(n):
            line = f.readline().strip()
            if line:
                numb = list(map(int, line.split()))
                lists.append(numb)

    heap = []

    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    fin = []

    while heap:
        val, l_i, e_i = heapq.heappop(heap)
        fin.append(val)

        if e_i + 1 < len(lists[l_i]):
            nv = lists[l_i][e_i + 1]
            heapq.heappush(heap, (nv, l_i, e_i + 1))

    with open(out_fn, 'w') as f:
        f.write(' '.join(map(str, fin)))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    in_F = sys.argv[1]
    out_F = sys.argv[2]
    merge(in_F, out_F)
