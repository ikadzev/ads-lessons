class Node:
    def __init__(self, value, kids=None):
        self.value = value
        self.kids = kids if kids else []

    def __str__(self):
        return f'Node {self.value} with kids {[i.value for i in self.kids]}'


def rec_comp(nodes: dict) -> (list[Node], dict[str, bool]):
    nodes_linked, depens = dict2link(nodes)

    reversed_nodes = {name: Node(name) for name in nodes_linked.keys()}
    for depen in depens:
        reversed_nodes[depen[1]].kids.append(reversed_nodes[depen[0]])

    visited, stack = [], []
    for node in reversed_nodes.values():
        visited, stack = dfs(node, visited, stack, False)

    visited = []
    comps = []
    mx = ([None], -1)
    while stack:
        node = stack.pop()
        comp = []
        visited, comp = dfs(nodes_linked[node.value], visited, comp, True)
        comps.append(comp) if comp else None
        if len(comp) > mx[1]:
            mx = ([c.value for c in comp], len(comp))
    for comp in comps:
        for node in range(len(comp)):
            comp[node] = comp[node].value
    return comps, mx


def dict2link(nodes: dict) -> (dict, dict):
    names = []
    depens = []
    for node, kids in nodes.items():
        names.append(node)
        for kid in kids:
            depens.append((node, kid))
    nodes = {name: Node(name) for name in names}
    for depen in depens:
        nodes[depen[0]].kids.append(nodes[depen[1]])
    return nodes, depens


def dfs(nod: Node, vst: list[Node], stk: list[Node], comp: bool) -> (list[Node], list[Node]):
    if nod not in vst:
        stk.append(nod) if comp else None
        vst.append(nod)
        for kid in nod.kids:
            vst, stk = dfs(kid, vst, stk, comp)
        stk.append(nod) if not comp else None
    return vst, stk


funcs = {'foo': ['bar', 'baz', 'qux'],
         'bar': ['baz', 'foo', 'bar'],
         'qux': ['qux'],
         'baz': []}

cycles, mx = rec_comp(funcs)
print('Max component:', *mx[0], '\nLength:', mx[1],  sep=' ')

if cycles:
    lst_recs = set([func for cycle in cycles for func in cycle])
    print('Functions', lst_recs, 'is recursive')
