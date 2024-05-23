class Node:
    def __init__(self, value, kids=()):
        self.value = value
        self.kids = kids


def rec_comp(nodes: dict) -> list[Node]:
    nodes_linked = dict2link(nodes)
    visited = len(nodes_linked.keys())
    depens = []
    for node in nodes_linked.values():
        for kid in node.kids():
            depens.append((node.value, kid.value))
    depens = [(dep[1], dep[0]) for dep in depens]
    reversed_nodes = {name: Node(name) for name in nodes_linked.keys()}
    for depen in depens:
        reversed_nodes[depen[0]].kids.append(depen[1])
    visited, stack = [], []
    for node in reversed_nodes.values():
        visited, stack = dfs(node, visited, stack)
    comps = []
    while stack:
        node = stack.pop()
        visited = []
        comps = []
        comp = []
        visited, comp = dfs_comps(node, visited, comp)
        comps.append(comp)
    mx = []
    for i in comps:
        if len(mx) < len(i):
            mx = i
    return mx


def dict2link(nodes: dict) -> dict:
    names = []
    depens = []
    for node, kids in nodes.items():
        names.append(node)
        for kid in kids:
            depens.append((node, kid))
    nodes = {name: Node(name) for name in names}
    for depen in depens:
        nodes[depen[0]].kids.append(depen[1])
    return nodes


def dfs_comps(node: Node, visited: list[Node], comp: list[Node]) -> (list[Node], list[Node]):
    if node not in visited:
        comp.append(node)
        visited.append(node)
        for kid in node.kids():
            visited, comp = dfs_comps(node, visited, comp)
    return visited, comp


def dfs(node, visited, stk):
    if node not in visited:
        visited.append(node)
        for kid in node.kids:
            visited, stk = dfs(kid, visited, stk)
        stk.append(node)
    return visited, stk
