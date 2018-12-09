import numpy as np
import parse_input

def get_distance(node1,node2,distance_matrix):
    return(distance_matrix[node1,node2])

def get_path_distance(path,distances_matrix):
    distance = 0
    for i in range(0, len(path) - 1):
        distance = distance + distances_matrix[path[i], path[i + 1]]
    return(distance)

def add_to_path(existing_path,node,distances_matrix):
    # we can add new node to any one of the edges in the existing path.
    # we'll test all and see which is the shortest
    distance = get_path_distance(existing_path,distances_matrix)
    total_distance = np.full(len(existing_path)-1,dtype=float,fill_value=distance)
    for i in range(0, len(existing_path) - 1):
        total_distance[i] += distances_matrix[existing_path[i], node] + distances_matrix[node,existing_path[i + 1]] - distances_matrix[existing_path[i], existing_path[i + 1]]
    min_index = np.argmin(total_distance)
    new_path = existing_path[:min_index+1]+[node]+existing_path[min_index+1:]
    return(new_path)

def get_shortest_path(start_end_node,list_of_nodes_to_touch,distances):
    existing_path = [start_end_node,start_end_node]
    for i in list_of_nodes_to_touch:
        existing_path = add_to_path(existing_path, i, distances)
    return(existing_path)


if __name__== "__main__":
    dm_tuple = parse_input.get_distance_matrix("customer_demand.txt");
    distances = dm_tuple[0]
    existing_path = [0,1,3,0]
    print(add_to_path(existing_path,5,distances))
    print(add_to_path([0,1,2,0], 5, distances))
    print(add_to_path([0,1,5,0], 2, distances))
    print(add_to_path(add_to_path([0, 1, 0], 2, distances),5,distances))
    print(add_to_path(add_to_path([0, 1, 0], 5, distances),2, distances))

    # Get shortest path for multiple points
    list_of_points = [1,2,3,4,7]
    print(get_shortest_path(0,list_of_points,distances))
