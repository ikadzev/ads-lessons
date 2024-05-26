class Node:
    def __init__(self, value, kids=None):
        self.value = value
        self.kids = kids if kids else []

    def __str__(self):
        return f'Node {self.value} with kids {[i.value for i in self.kids]}'


def rec_comp(nodes: dict) -> (list[Node], dict[str, bool]):
    nodes_linked = dict2link(nodes)
    is_recs = nodes_linked.values()
    is_recs = {func.value: is_rec(func) for func in is_recs}
    depens = []
    for node in nodes_linked.values():
        for kid in node.kids:
            depens.append((node.value, kid.value))

    reversed_nodes = {name: Node(name) for name in nodes_linked.keys()}
    for depen in depens:
        reversed_nodes[depen[1]].kids.append(reversed_nodes[depen[0]])

    visited, stack = [], []
    for node in reversed_nodes.values():
        visited, stack = dfs(node, visited, stack)

    visited = []
    comps = []
    while stack:
        node = stack.pop()
        comp = []
        visited, comp = dfs_comps(nodes_linked[node.value], visited, comp)
        comps.append(comp) if comp else None
    for comp in comps:
        for node in range(len(comp)):
            comp[node] = comp[node].value
    return comps, is_recs


def is_rec(node):
    def _is_rec_inner(node, init):
        if init in node.kids:
            return True
        for kiddo in node.kids:
            if _is_rec_inner(kiddo, init):
                return True
        return False

    for kid in node.kids:
        if _is_rec_inner(kid, node):
            return True
    return False


def dict2link(nodes: dict) -> dict:
    names = []
    depens = []
    for node, kids in nodes.items():
        names.append(node)
        for kid in kids:
            depens.append((node, kid))
    nodes = {name: Node(name) for name in names}
    for depen in depens:
        nodes[depen[0]].kids.append(nodes[depen[1]])
    return nodes


def dfs_comps(node: Node, visited: list[Node], comp: list[Node]) -> (list[Node], list[Node]):
    if node not in visited:
        comp.append(node)
        visited.append(node)
        for kid in node.kids:
            visited, comp = dfs_comps(kid, visited, comp)
    return visited, comp


def dfs(node, visited, stk):
    if node not in visited:
        visited.append(node)
        for kid in node.kids:
            visited, stk = dfs(kid, visited, stk)
        stk.append(node)
    return visited, stk


# funcs = {'0': ['4'],
#          '1': ['0', '7'],
#          '2': ['1', '4', '6'],
#          '3': ['0', '3'],
#          '4': ['0'],
#          '5': ['2'],
#          '6': ['4', '5'],
#          '7': ['1', '3']}
funcs = {'foo': ['bar', 'baz', 'qux'],
         'bar': ['baz', 'foo', 'bar'],
         'qux': ['qux'],
         'baz': []}
cycles, recs = rec_comp(funcs)
mx = max([len(i) for i in cycles])
maax = [i for i in cycles if len(i) == mx]
print(*maax, sep=' ')
rcs = [f'{i} is recursive!' for i, j in recs.items() if j]
print(*rcs, sep='\n')
