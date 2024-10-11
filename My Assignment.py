from collections import deque
class homeServiceBooking:
    def __init__(self):
        self.available_service = ['cleaning', 'home care', 'electrical','cooking']
        self.booking_request = deque()
        self.undo_service = []
    
    def request_booking(self, customer_name, service):
        if service in self.available_service:
            self.booking_request.append((customer_name, service))
            print(f"the request from {customer_name} for service {service}")
        else:
            print(f"the service {service} is Not available")

    def process_booking_request(self):
        if self.booking_request:
            customer_name, service = self.booking_request.popleft()
            self.available_service.remove(service)
            self.undo_service.append((customer_name, service))
            print(f"{customer_name} started service {service}")
        else:
            print("No process booking requested" )

    def undo_request(self):
        if self.undo_service:
            customer_name, service = self.undo_service.pop()
            self.available_service.append(service)
            print(f"{customer_name} refused to work {service}")
        else:
            print("No service to undo")

    def show_available_service(self):
        print("The service Available",self.available_service)
     
    def show_booking_request(self):
        for request in self.booking_request:
            print(request)  

if __name__ == "__main__":
    home_service_system = homeServiceBooking()

    def menu():
        while True:
            print("\n1. show available service.")
            print("2. booking_request.")
            print("3. show process booking request.")
            print("4. refused service. ")
            print("5. show remain service.")
            print("6. Exit.")
            choice=input("\n choose an option (1 up to 6):")
            if choice=='1':
                home_service_system.show_available_service()
            elif choice=='2':
                try:
                    customer_name = input("Enter your name: ")
                    service=input("Enter the service you want:")
                    home_service_system.request_booking( customer_name, service)
                except ValueError:
                    print("Invalid input. please try again.")
            elif choice=='3':
                home_service_system.process_booking_request()
            elif choice=='4':
                home_service_system.undo_request()
            elif choice=='5':
                home_service_system.show_available_service()
            elif choice=='6':
                print("\nExisting the system. Good byeee..!!!")
                break
            else:
                print("\nInvalid option. please select a valid option.")

    menu()
