class SegmentTree:
    def __init__(self, arr):
        self.tree = [0] * (len(arr)*4)
        self.size = len(arr)
        self.__build_tree(arr,0, len(arr)-1, 1)

    # private
    def __build_tree(self, arr, start, end, inx):
        if start == end:
            self.tree[inx] = arr[start]
            return

        # build subtree
        # left align divide -- 1 2 3 || 4 5
        mid = (start + end) // 2
        self.__build_tree(arr, start, mid, 2*inx)
        self.__build_tree(arr, mid+1, end, 2*inx+1)

        # fill max
        # because inx start from 1
        # so do 2*inx here, not 2*inx+1
        self.tree[inx] = self.tree[2*inx] + self.tree[2*inx+1]

    def query(self, start, end):
        return self.__query(0, self.size-1, start, end, 1)

    # private
    def __query(self, start, end, left, right, inx):
        # out of range
        if start < left or end > right:
            return -float('inf')

        # total overlap
        # ps: in the layer, the range will not overlap
        elif start >= left and end <= right:
            return self.tree[inx]

        # partial overlap
        else:
            mid = (start+end) //2
            left_child = self.__query(start, mid, left, right, 2*inx)
            right_child = self.__query(mid+1, end, left, right, 2*inx+1)
            return left_child + right_child

    def update(self, inx, val):
        if inx < 0 or inx >= self.size:
            raise IndexError('index out of range')
        self.__update(0, self.size-1, 1, inx, val)

    # start and end --> arr
    # cur_inx --> tree
    def __update(self, start, end, cur_inx, inx, val):
        # recurs-if can make it only focus the correct point
        # update leaf node
        if start == end:
            self.tree[cur_inx] = val
            return

        # update subtree
        mid = (start+end) // 2
        if inx <= mid:  # go left
            self.__update(start, mid, cur_inx*2, inx, val)
        else:   # go right
            self.__update(mid+1, end, cur_inx*2+1, inx, val)

        # update sum node
        self.tree[cur_inx] = self.tree[cur_inx*2] \
                                + self.tree[cur_inx*2+1]

st = SegmentTree([1,2,3,4])
print(st.tree)

# get sum in [0,3]
print(st.query(0,3))

# update arr[0] to 8
st.update(0, 8)
print(st.tree)
