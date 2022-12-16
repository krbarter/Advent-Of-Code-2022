from collections import defaultdict, deque

def read_input(path: str = 'input.txt'): # New python function type
    inputs = dict()
    with open(path) as filet:
        for line in filet.readlines():
            line = line.rstrip()
            name = line.split(' ')[1]
            flow = int(line.split(' ')[4].split('=')[1][:-1])
            next_elements = line.split('valve')[1].replace('s ', '').replace(' ', '').split(',')
            inputs[name] = [flow, tuple(next_elements)]
    return inputs

def get_shortest_path(start, end, graph):
    queue = deque([(start, 0)])
    cost = defaultdict(lambda: float('inf'))
    while queue:
        position, steps = queue.popleft()
        if position == end:
            break
        if steps > cost[position]:
            continue
        for neighbour in graph[position][1]:
            nsteps = steps + 1
            if nsteps < cost[neighbour]:
                cost[neighbour] = nsteps
                queue.append((neighbour, nsteps))
    return cost[end]


def get_worthy_valves(inputs: dict):
    non_zero = {name for name, value in inputs.items() if value[0] > 0}
    non_zero.add('AA')
    return non_zero

def get_shortest_connections(worthy_valves: set, graph: dict):
    shortest_path = defaultdict(dict)
    non_zero_list = list(worthy_valves)
    for idx, start in enumerate(non_zero_list):
        for end in non_zero_list[idx + 1:]:
            path_cost = get_shortest_path(start, end, graph)
            shortest_path[start][end] = path_cost
            shortest_path[end][start] = path_cost
    return shortest_path

def traverse_everything(shortest_path, graph, time):
    pathes = defaultdict(lambda: -1)
    queue = deque([('AA', 0, time, set())])
    while queue:
        position, accumulated_flow, time, visited = queue.popleft()
        neighbours = (neighbor for neighbor in shortest_path[position]
                      if neighbor not in visited and shortest_path[position][neighbor] < time)

        if pathes[frozenset(visited)] < accumulated_flow:
            pathes[frozenset(visited)] = accumulated_flow

        for neighbor in neighbours:
            new_flow = (time - shortest_path[position][neighbor] - 1) * graph[neighbor][0]
            new_set = visited | {neighbor}
            queue.append((neighbor, accumulated_flow + new_flow, time - shortest_path[position][neighbor] - 1, new_set))
    return pathes
    
def __main__():
    # Part One
    inputs = read_input()
    non_zero = get_worthy_valves(inputs)
    shortest_path = get_shortest_connections(non_zero, inputs)
    pathes = traverse_everything(shortest_path, inputs, 30)
    print(f'The result for solution 1 is: {max(pathes.values())}')

    # Part Two
    inputs = read_input()
    non_zero = get_worthy_valves(inputs)
    shortest_path = get_shortest_connections(non_zero, inputs)
    pathes = traverse_everything(shortest_path, inputs, 26)
    result = max(
        flow1 + flow2 for path1, flow1 in pathes.items() for path2, flow2 in pathes.items() if not path1 & path2)
    print(f'The result for solution 2 is: {result}')

__main__()