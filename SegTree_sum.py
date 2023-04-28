class SegmentTree():    # sum
    def __init__(self, arr):
        self.tree = [0] * (4*len(arr))
        self.size = len(arr)
        self._build_tree(arr, 0, len(arr)-1, 1)

    def _build_tree(self, arr, start, end, inx):
        if start == end:
            self.tree[inx] = arr[start]
            return

        # build subtree
        mid = (start + end) // 2
        self._build_tree(arr, start, mid, 2*inx)
        self._build_tree(arr, mid+1, end, 2*inx + 1)

        # fill max
        self.tree[inx] = self.tree[2*inx] + self.tree[2*inx+1]

    def query(self, start, end):
        return self._query(0, self.size-1, 1, start, end)

    def _query(self, start, end, cur_inx, target_start, target_end):
        # out of range
        # also dealing with endpoint
        if target_start > end or target_end < start:
            return 0

        # current range right inside target, just return
        # dealing with endpoint
        elif target_start <= start and target_end >= end:
            return self.tree[cur_inx]

        # partial -- go deeper
        else:
            mid = (start+end) // 2
            left_child = self._query(start, mid, 2*cur_inx, target_start, target_end)
            right_child = self._query(mid+1, end, 2*cur_inx+1, target_start, target_end)
            return left_child + right_child

    def update(self, inx, val):
        self._update(0, self.size-1, 1, inx, val)

    # start, end -- range
    # inx -- compare to mid for select
    # cur_inx -- tree -- 2*cur_inx represent go down a layer
    def _update(self, start, end, cur_inx, inx, val):
        if start == end:
            self.tree[cur_inx] = val
            return

        # update subtree
        mid = (start+end) // 2
        if inx <= mid:
            self._update(start, mid, 2*cur_inx, inx, val)
        else:
            self._update(mid+1, end, 2*cur_inx+1, inx, val)

        # update sum
        # ps: cant just add val
        self.tree[cur_inx] = self.tree[2*cur_inx] + self.tree[2*cur_inx+1]

st = SegmentTree([1,2,3,4])

# update arr[0] to 8
st.update(0, 8)

# get sum in [0,3]
print(st.query(0,3))
print(st.tree)

