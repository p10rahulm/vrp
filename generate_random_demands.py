import random;
import fileinput
def gen_demands(filename,min_customers,max_customers,min_vehicles,max_vehicles,min_vehicle_capacity,max_vehicle_capacity,
                min_individual_demand,max_individual_demand,x_min,x_max,y_min,y_max):
    num_customers = random.randint(min_customers,max_customers);
    vehicles = random.randint(min_vehicles,max_vehicles);
    capacity = random.randint(min_vehicle_capacity,max_vehicle_capacity)
    with open(filename, 'w') as outfile:
        print(num_customers,vehicles,capacity,file=outfile)
        for i in range(0,num_customers):
            cust_demand = 0 if (i == 0) else random.randint(min_individual_demand,max_individual_demand)
            print(cust_demand,random.randint(x_min,x_max),random.randint(y_min,y_max),file=outfile)


if __name__== "__main__":
    gen_demands(filename = "customer_demand.txt", min_customers = 10, max_customers = 15, min_vehicles = 4, max_vehicles = 10,
                min_vehicle_capacity = 25,max_vehicle_capacity = 50,min_individual_demand = 1, max_individual_demand = 5,
                x_min = 1, x_max = 99, y_min = 1, y_max = 99)

