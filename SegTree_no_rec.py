class SegmentTree:
    def __init__(self, arr):
        self.tree = [0] * (4 * len(arr))
        self.build_tree(arr)

    def build_tree(self, arr):
        n = len(arr)
        stack = [(0, n - 1, 0)]
        while stack:
            l, r, pos = stack.pop()
            if l == r:
                self.tree[pos] = arr[l]
            else:
                mid = (l + r) // 2
                stack.append((mid + 1, r, 2 * pos + 2))
                stack.append((l, mid, 2 * pos + 1))
                self.tree[pos] = self.tree[2 * pos + 1] + self.tree[2 * pos + 2]

    def update(self, i, val):
        n = (len(self.tree) + 1) // 2
        pos = i + n - 1
        self.tree[pos] = val
        while pos > 0:
            pos = (pos - 1) // 2
            self.tree[pos] = self.tree[2 * pos + 1] + self.tree[2 * pos + 2]

    def query(self, ql, qr):
        n = (len(self.tree) + 1) // 2
        stack = [(0, n - 1, 0)]
        res = 0
        while stack:
            l, r, pos = stack.pop()
            if ql <= l and r <= qr:
                res += self.tree[pos]
            elif ql > r or qr < l:
                continue
            else:
                mid = (l + r) // 2
                stack.append((mid + 1, r, 2 * pos + 2))
                stack.append((l, mid, 2 * pos + 1))
        return res


st = SegmentTree([1,2,3,4])
print(st.query(0,2))
