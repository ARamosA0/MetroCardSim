
class TravelSystem:
    def __init__(self):
        self.station_charges = {}  
        self.passenger_summary = {}  
        self.station_passenger_type_counter = {}
        self.charges = {"ADULT":200, "SENIOR_CITIZEN":100, "KID":50}
        self.station = ["CENTRAL", "AIRPORT"]

    def balance(self, passenger_id, balance_amount):
        self.passenger_summary[passenger_id] = {"amount":balance_amount}


    def check_in(self, passenger_id, passenger_type, destination):
        if passenger_id in self.passenger_summary:
            for id, item in self.passenger_summary.items():
                item["from"] = destination
                item["type"] = passenger_type

        if destination in self.station_passenger_type_counter:
            self.tipe_passenger(passenger_id, passenger_type, destination)
        else:
            self.station_passenger_type_counter[destination] = {passenger_type:1, "total":0, "discount":0}

        charge = self.calculate_charge(passenger_id, passenger_type, destination)

        self.station_passenger_type_counter[destination]["total"] += charge

    def tipe_passenger(self, passenger_id, passenger_type, destination):
        if passenger_type in self.station_passenger_type_counter[destination]:
            self.station_passenger_type_counter[destination][passenger_type] += 1
        else:
            self.station_passenger_type_counter[destination][passenger_type] = 1

    def cal_fee(self, passenger, charge):
        if int(passenger["amount"]) < charge:
            total = charge - int(passenger["amount"])
            return total * 0.02
        else:
            return 0

    def calculate_charge(self, passenger_id, passenger_type, destination):
        passenger = self.passenger_summary[passenger_id]
        station = self.station_passenger_type_counter[destination]
        charge = 0
        if "to" in self.passenger_summary[passenger_id]:
            charge = self.charges[passenger_type]/2
            recharge = self.cal_fee(passenger, charge)
            station["discount"] += charge
            del self.passenger_summary[passenger_id]["to"] 
            return charge + recharge
        else:
            charge = self.charges[passenger_type]
            recharge = self.cal_fee(passenger, charge)
            if destination == self.station[0]:
                self.passenger_summary[passenger_id]["to"] = self.station[1]  
            elif destination == self.station[1]:
                self.passenger_summary[passenger_id]["to"] = self.station[0]  
            return charge + recharge
    
   

    def print_functions(self):
        for place, type in self.station_passenger_type_counter.items():
            print(f"TOTAL COLLECTION  {place}  {type['total']}  {type['discount']}")
            print("\nPASSENGER_TYPE_SUMMARY")
            for category, count in type.items():
                print(f"{category}  {count}")
            print("\n")

