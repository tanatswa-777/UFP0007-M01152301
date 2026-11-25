from devices import Sensor, Computer, Printer

devices = [
    Sensor("Server Room Sensor", "Block A", 34),
    Computer("Lab PC 01", "Lab 2", False),
    Printer("Library Printer", "Library", 8),
    Printer("Office Printer", "Admin", 70),
]


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")


def list_devices(items):
    if not items:
        print("No devices to show.")
    for number, device in enumerate(items, 1):
        print(f"{number}. {device}")


def add_device():
    kind = input("Type (1=Sensor, 2=Computer, 3=Printer): ")
    if kind not in ("1", "2", "3"):
        print("Invalid type.")
        return
    name = input("Name: ")
    location = input("Location: ")
    if kind == "1":
        devices.append(Sensor(name, location, get_number("Temperature (C): ")))
    elif kind == "2":
        online = input("Online? (y/n): ").lower() == "y"
        devices.append(Computer(name, location, online))
    else:
        devices.append(Printer(name, location, get_number("Toner (%): ")))
    print("Device added.")


def remove_device():
    list_devices(devices)
    number = int(get_number("Number to remove: "))
    if 1 <= number <= len(devices):
        devices.pop(number - 1)
        print("Device removed.")
    else:
        print("Invalid number.")


while True:
    print("\n--- Campus Device Monitor ---")
    print("1. List all devices")
    print("2. Show devices needing attention")
    print("3. Add a device")
    print("4. Remove a device")
    print("5. Exit")
    choice = input("Choose: ")

    if choice == "1":
        list_devices(devices)
    elif choice == "2":
        list_devices([d for d in devices if d.needs_attention()])
    elif choice == "3":
        add_device()
    elif choice == "4":
        remove_device()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
