import generate_random_demands,combining_paths,parse_input,tsp,numpy as np

def get_paths(distances,capacities,vehicle_capacity):
    (paths, ds_matrix, capacities_required) = combining_paths.initialize_paths(distances, capacities)
    path_indices_to_merge = combining_paths.get_index_of_paths_to_merge(paths, ds_matrix, distances, capacities, vehicle_capacity)
    while (path_indices_to_merge != (-1, -1)):
        (paths, ds_matrix) = combining_paths.merge_two_paths(paths, ds_matrix, path_indices_to_merge, distances, capacities)
        path_indices_to_merge = combining_paths.get_index_of_paths_to_merge(paths, ds_matrix, distances, capacities, vehicle_capacity)
    path_lengths = [tsp.get_path_distance(path,distances) for path in paths]
    total_path_length = sum(path_lengths)
    return (paths,path_lengths,total_path_length)

def generate_output(paths,total_path_length,out_filename):
    with open(out_filename, 'w') as outfile:
        print(total_path_length,0,file=outfile)
        for i in range(0,len(paths)):
            print(i, end ="\t", file=outfile)
            for j in range(1,len(paths[i])):
                print("t_0_", paths[i][j], sep="",end =" ", file=outfile)
            print("",file=outfile)
    return()

def vary_customers(num_customer):
    generate_random_demands.gen_demands(filename="cust_demand.txt", min_customers=num_customer, max_customers=num_customer,
                                        min_vehicles=10, max_vehicles=20, min_vehicle_capacity=25,
                                        max_vehicle_capacity=50, min_individual_demand=1, max_individual_demand=5,
                                        x_min=1, x_max=99, y_min=1, y_max=99)

    dm_tuple = parse_input.get_distance_matrix("cust_demand.txt");
    distances = dm_tuple[0]
    capacities = np.array(dm_tuple[3])
    vehicle_capacity = parse_input.get_vehicle_capacity("cust_demand.txt")
    num_vehicles = parse_input.get_num_vehicles("cust_demand.txt")
    (paths, path_lengths, total_path_length) = get_paths(distances, capacities, vehicle_capacity)
    return 0
if __name__== "__main__":

    generate_random_demands.gen_demands(filename = "cust_demand.txt", min_customers = 50, max_customers = 100,
                                        min_vehicles = 10, max_vehicles = 20, min_vehicle_capacity = 25,
                                        max_vehicle_capacity = 50,min_individual_demand = 1, max_individual_demand = 5,
                                        x_min = 1, x_max = 99, y_min = 1, y_max = 99)

    dm_tuple = parse_input.get_distance_matrix("cust_demand.txt");
    distances = dm_tuple[0]
    capacities = np.array(dm_tuple[3])
    vehicle_capacity = parse_input.get_vehicle_capacity("cust_demand.txt")
    num_vehicles = parse_input.get_num_vehicles("cust_demand.txt")

    (paths,path_lengths,total_path_length) = get_paths(distances,capacities,vehicle_capacity)
    # print("paths = ", paths)
    if(num_vehicles<len(paths)):
        print("Number of vehicles available less than number of trips required. Some vehicles may have to go on more than 1 round trip")
    generate_output(paths,total_path_length,"output.txt")

    import time
    for i in range(2,10):
        st_time = time.time()
        vary_customers(2**i)
        print("num demand points =",2**i,"; time taken = ", time.time() - st_time)



