import numpy as np

def get_distance_matrix(filename):
    with open(filename, 'r') as inputs:
        num_customers = int(inputs.readline().split()[0]);
        customer_xs = []
        customer_ys = []
        customer_demands = []
        for i in range(0, num_customers):
            temp = inputs.readline().split()
            customer_demands.append(float(temp[0]))
            customer_xs.append(int(temp[1]))
            customer_ys.append(int(temp[2]))
    distance_matrix = np.zeros((num_customers,num_customers), dtype=float)
    for i in range(0,num_customers):
        for j in range(i+1,num_customers):
            distance_matrix[i,j] = round(((customer_xs[i]-customer_xs[j])**2 + (customer_ys[i]-customer_ys[j])**2)**0.5,4)
    distance_matrix = distance_matrix + np.transpose(distance_matrix)
    return((distance_matrix,customer_xs,customer_ys,customer_demands))

def get_vehicle_capacity(filename):
    with open(filename, 'r') as inputs:
        vehicle_capacity = int(inputs.readline().split()[2]);
    return (vehicle_capacity)

def get_num_vehicles(filename):
    with open(filename, 'r') as inputs:
        num_vehicles = int(inputs.readline().split()[1]);
    return (num_vehicles)

def get_num_customers(filename):
    with open(filename, 'r') as inputs:
        num_customers = int(inputs.readline().split()[0]);
    return (num_customers)

if __name__== "__main__":
    dm = get_distance_matrix("customer_demand.txt");
    np.savetxt("distance_matrix.txt", dm[0], delimiter=",",fmt='%d')
