import tsp,parse_input,generate_random_demands
import itertools,numpy as np

def generate_path_permutations(start_end_node,points_to_touch):
    permutations_iterator = itertools.permutations(points_to_touch)
    path_permutations = []
    for path_perm in permutations_iterator:
        path_permutations.append([start_end_node] + list(path_perm) + [start_end_node])
    return path_permutations

def check_shortest_path(start_end_node,points_to_touch,distances):
    shortest_path_predicted = tsp.get_shortest_path(start_end_node, points_to_touch, distances)
    path_permutations = generate_path_permutations(start_end_node, points_to_touch)
    path_distances = [tsp.get_path_distance(path, distances) for path in path_permutations]
    min_index = np.argmin(path_distances)
    minpath = path_permutations[min_index]
    return minpath==shortest_path_predicted


def list_all_subsets(input_list):
    """returns a list of all subsets of a list"""
    subsets = []
    for i in range(0, len(input_list) + 1):
        listing = [list(x) for x in itertools.combinations(input_list, i)]
        subsets.extend(listing)
    return subsets



def list_all_proper_subsets(input_list):
    """returns a list of all subsets of a list"""
    subsets = []
    for i in range(0, len(input_list)):
        listing = [list(x) for x in itertools.combinations(input_list, i)]
        subsets.extend(listing)
    return subsets

def check_all_tsps(start_end_node,points_to_touch,distances,filename = 'check_tsps.txt'):
    all_points_to_touch = list_all_subsets(points_to_touch)
    with open(filename, 'w') as outfile:
        print("Subset of Points\tShortest Path Predicted\shortest path predicted distance\tShortest Path Actual\tactual shortest path distance\tPredicted=Actual",file=outfile)
        for subset_of_points in all_points_to_touch:
            print(subset_of_points, end="\t",file=outfile)
            shortest_path_predicted = tsp.get_shortest_path(start_end_node, subset_of_points, distances)
            print(shortest_path_predicted,end="\t",file=outfile)
            print(round(tsp.get_path_distance(shortest_path_predicted,distances),2), end="\t", file=outfile)
            path_permutations = generate_path_permutations(start_end_node, subset_of_points)
            path_distances = [tsp.get_path_distance(path, distances) for path in path_permutations]
            min_index = np.argmin(path_distances)
            min_path_actual = path_permutations[min_index]
            print(min_path_actual, file=outfile, end="\t")
            print(round(tsp.get_path_distance(min_path_actual, distances),2), end="\t", file=outfile)
            print(min_path_actual==shortest_path_predicted or min_path_actual[::-1] == shortest_path_predicted, end="\n",file=outfile)


if __name__== "__main__":
    # generate_random_demands.gen_demands(filename="check_tsp_generated_customers.txt", min_customers=8, max_customers=10, min_vehicles=4, max_vehicles=10,
    #             min_vehicle_capacity=25, max_vehicle_capacity=50, min_individual_demand=1, max_individual_demand=5,
    #             x_min=1, x_max=99, y_min=1, y_max=99)

    dm_tuple = parse_input.get_distance_matrix("check_tsp_generated_customers.txt");
    distances = dm_tuple[0]
    points_to_touch = [1,2,6,7]
    shortest_path_predicted = tsp.get_shortest_path(0,points_to_touch,distances)
    print(shortest_path_predicted)
    path_permutations = generate_path_permutations(0,points_to_touch)
    path_distances = [tsp.get_path_distance(path,distances) for path in path_permutations]
    min_index = np.argmin(path_distances)
    minpath = path_permutations[min_index]
    print(minpath)
    print(minpath==shortest_path_predicted)
    print(check_shortest_path(0,points_to_touch,distances))
    print(list_all_subsets([1, 2, 3]))
    print(list_all_proper_subsets([1, 2, 3]))
    points_to_touch = list(range(1,parse_input.get_num_customers("check_tsp_generated_customers.txt")))
    print(points_to_touch)

    all_points_to_touch = list_all_subsets(points_to_touch)
    # print(all_points_to_touch)
    check_all_tsps(0,points_to_touch,distances)