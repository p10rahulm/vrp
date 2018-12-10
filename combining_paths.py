import tsp,parse_input,numpy as np

def get_capacity_requirement(path,capacities):
    return(capacities[path].sum())

def get_max_index(matrix):
    return(np.unravel_index(matrix.argmax(), matrix.shape))



def combine_paths(path1,path2,distances,capacities):
    shorter_path = path1 if len(path1)<len(path2) else path2
    longer_path = path2 if len(path1) < len(path2) else path1
    for i in shorter_path[1:-1]:
        longer_path = tsp.add_to_path(longer_path, i, distances)
    path1distance = tsp.get_path_distance(path1,distances)
    path2distance = tsp.get_path_distance(path2, distances)
    longer_path_d = tsp.get_path_distance(longer_path, distances)
    distance_saved = path1distance + path2distance - longer_path_d

    total_capacity_required = get_capacity_requirement(longer_path,capacities)

    return((longer_path,distance_saved,total_capacity_required))

def initialize_paths(distances,capacities):
    initial_paths = [[0,i,0] for i in range(1,len(distances))]
    capacities_required = [get_capacity_requirement(path,capacities) for path in initial_paths]
    distance_saved_on_merge = np.zeros((len(initial_paths), len(initial_paths)), dtype=float)
    for i in range(0, len(initial_paths)):
        for j in range(i + 1, len(initial_paths)):
            distance_saved_on_merge[i, j] = round(combine_paths(initial_paths[i], initial_paths[j], distances,capacities)[1], 4)
    return((initial_paths,distance_saved_on_merge,capacities_required))


def merge_two_paths(paths,distances_saved_matrix,paths_to_merge,distances,capacities):
    new_paths = []
    combined_path = combine_paths(paths[paths_to_merge[0]],paths[paths_to_merge[1]],distances,capacities)[0]
    new_paths.append(combined_path)
    for i in range(0, len(paths)):
        if(i not in paths_to_merge):
            new_paths.append(paths[i])
    new_ds_matrix = np.zeros((len(paths) - 1, len(paths) - 1), dtype=float)
    for i in range(1, len(new_paths)):
        new_ds_matrix[0, i] = round(combine_paths(new_paths[0], new_paths[i], distances,capacities)[1], 4)
    mask = np.ones(len(distances_saved_matrix), dtype=bool)
    mask[[paths_to_merge]] = False
    new_ds_matrix[1:,1:] = distances_saved_matrix[mask, :][:, mask]
    return (new_paths,new_ds_matrix)

def get_index_of_paths_to_merge(paths,distances_saved_matrix,distances,capacities,max_capacity):
    # we will use the largest in the distance saved matrix as long as it is below the capacity of the vehicle
    # lets make a copy of the distances saved matrix
    dist_saved = np.copy(distances_saved_matrix)
    max_index = (-1,-1)
    while(max_index == (-1,-1) and np.max(dist_saved)>0):
        max_index = get_max_index(dist_saved)
        capa_reqd = combine_paths(paths[max_index[0]], paths[max_index[1]], distances, capacities)[2]
        if (capa_reqd>max_capacity):
            dist_saved[max_index[0],max_index[1]] = float('-inf')
            max_index = (-1, -1)
    return max_index


if __name__== "__main__":
    dm_tuple = parse_input.get_distance_matrix("customer_demand.txt");
    distances = dm_tuple[0]
    capacities = np.array(dm_tuple[3])
    print("capacities=",capacities)
    path1_points = [1, 2, 3, 4, 7]
    path1 = tsp.get_shortest_path(0, path1_points, distances)
    print("path1=",path1)

    path2_points = [5,8,6]
    path2 = tsp.get_shortest_path(0, path2_points, distances)
    print("path2=",path2)

    (longer_path,distance_saved,capacity_required) = combine_paths(path1,path2,distances,capacities)
    # print(distance_saved)
    (initial_paths,ds_matrix,capacities_required) = initialize_paths(distances,capacities)
    print("initial_paths= ",initial_paths)
    print("get_capacity_requirement([0,1,2],capacities)= ", get_capacity_requirement([0,1,2],capacities))
    print("distance_saved_on_merge = \n", ds_matrix)
    print("np.max(distance_saved_on_merge)= \n",np.max(ds_matrix) )
    paths = initial_paths
    path_indices_to_merge = get_index_of_paths_to_merge(paths, ds_matrix, distances, capacities, 25)
    while(path_indices_to_merge!=(-1,-1)):
        print("paths",paths)
        print("path_indices_to_merge", path_indices_to_merge)
        (paths,ds_matrix) = merge_two_paths(paths,ds_matrix,path_indices_to_merge,distances,capacities)
        path_indices_to_merge = get_index_of_paths_to_merge(paths, ds_matrix, distances, capacities, 25)

    print("paths",paths)


