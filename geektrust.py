from sys import argv
from src.travelsystem import TravelSystem
   
def main():


    travel_system = TravelSystem()

    if len(argv) !=2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    for line in Lines:
        parts = line.strip().split(' ')
        if parts[0] == "BALANCE":
            passenger_id = parts[1]
            passenger_amount = parts[2]
            travel_system.balance(passenger_id, passenger_amount)

        if parts[0] == "CHECK_IN":
            passenger_id = parts[1]
            passenger_type = parts[2]
            destination = parts[3]
            travel_system.check_in(passenger_id, passenger_type, destination)

        """
        passenger_id = parts[0] 
        passenger_type = parts[1]
        source = parts[2]
        destination = parts[3]
        travel_system.record_journey(passenger_id, passenger_type, source, destination)
"""
    #travel_system.print_collection_summary()
    #travel_system.print_passenger_summary()
    travel_system.print_functions()
 

    
if __name__ == "__main__":
    main()
