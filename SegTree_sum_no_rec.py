class SegmentTree():    # sum
    def __init__(self, arr):
        self.tree = [0] * (4*len(arr))
        self.size = len(arr)
        self._build_tree(arr)


    def _build_tree(self, arr):
        stack = [(0, len(arr)-1, 0)]
        while stack:
            l, r, pos = stack.pop()
            if l == r:
                self.tree[pos] = arr[l]
                # update backward
                while pos >= 1:
                    if pos%2 == 0:
                        pos = (pos-2) // 2
                    else:
                        pos = (pos-1) // 2
                    self.tree[pos] = self.tree[2*pos+1] + self.tree[2*pos+2]
            else:
                mid = (l+r) // 2
                stack.append((mid+1, r, 2*pos+2))
                stack.append((l, mid, 2*pos+1))



    def query(self, start, end):
        stack = [(0, self.size-1, start, end, 0)]
        res = 0
        while stack:
            range_start, range_end, target_start, target_end, pos = stack.pop()
            # no cover
            if target_start > range_end or target_end < range_start:
                continue
            # inside
            elif target_start <= range_start and target_end >= range_end:
                res += self.tree[pos]
            # partial cover
            else:
                mid = (range_start + range_end) // 2
                stack.append((mid+1, range_end, target_start, target_end, 2*pos+2))
                stack.append((range_start, mid, target_start, target_end, 2*pos+1))
        return res

    def update(self, inx, val):
        stack = [0]
        start, end = 0, self.size-1
        pos = 0
        while pos < len(self.tree):
            mid = (start+end) // 2
            # start == end 才到endpoint
            if start == end:
                self.tree[pos] = val
                break
            elif inx <= mid:
                end = mid
                stack.append(pos)
                pos = pos*2 + 1
            else:
                start = mid+1
                stack.append(pos)
                pos = pos*2 + 2

        # update backward
        while stack:
            pos = stack.pop()
            self.tree[pos] = self.tree[pos*2+1] + self.tree[pos*2+2]



st = SegmentTree([1,2,3,4])
print(st.tree)

# update arr[0] to 8
st.update(0, 8)

# get sum in [0,2]
print(st.query(0,2))
print(st.tree)

