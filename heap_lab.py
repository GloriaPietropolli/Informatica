def min_order(a, b):
    return a <= b


class binheap_preserving_order(object):
    def __init__(self, list_keys, total_order=min_order):
        self._keys = list_keys
        self.tree_dimension = len(list_keys)
        self.total_order = total_order

        self.list_permutation = self._build_heap()

    def min(self):
        return self._keys[0]

    @staticmethod
    def neighborhood(index_node, side):
        if side == 'r':  # right
            return 2 * (index_node + 1)
        if side == 'l':  # left
            return 2 * index_node + 1
        if side == 'p':  # parent
            return (index_node - 1) // 2

    def test_total_order(self, node_i, node_j):
        key_i, key_j = self._keys[node_i], self._keys[node_j]
        answer = self.total_order(key_i, key_j)
        return answer

    def heapify(self, node_i, list_permutation):
        keep_fix = True
        while keep_fix:
            root_node = node_i
            for node in [binheap_preserving_order.neighborhood(node_i, 'l'),
                         binheap_preserving_order.neighborhood(node_i, 'r')]:
                if node < self.tree_dimension and self.test_total_order(node, node_i):
                    root_node = node
            if root_node != node_i:
                (self._keys[root_node], self._keys[node_i]) = (self._keys[node_i], self._keys[root_node])
                (list_permutation[root_node], list_permutation[node_i]) = (
                    list_permutation[node_i], list_permutation[root_node])
                node_i = root_node
            else:
                keep_fix = False

    def _build_heap(self):
        node = binheap_preserving_order.neighborhood(self.tree_dimension - 1, 'p')
        list_permutation = [index for index in range(self.tree_dimension)]
        for node_i in range(node, -1, -1):
            self.heapify(node_i, list_permutation)
        return list_permutation

    def __repr__(self):
        bt_str = '['

        level = 0
        next_level = 2 ** level
        for i in range(0, self.tree_dimension):
            bt_str += '{}'.format(self._keys[i])
            if i + 1 < self.tree_dimension:
                if next_level == i + 1:
                    bt_str += ']\n['
                else:
                    bt_str += ' '
            if next_level == i + 1:
                level += 1
                next_level += 2 ** level

        return bt_str + ']'


A = [1, 2, 3, 7, 4, 7, 88, 74, 32, 89, 56, 6, 31, 100, 130, 0]
a = binheap_preserving_order(A)
print(a.list_permutation)
print(a)
