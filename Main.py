
MENU = """
===== Campus Device Monitor =====
1. List all devices
2. Show devices needing attention
3. Add a device
4. Update a device reading
5. Remove a device
6. View device details
7. Summary
8. Load sample devices
0. Exit
"""


def ask_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please enter something.")


def ask_number(prompt, low=None, high=None):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a number.")
            continue
        if (low is not None and value < low) or (high is not None and value > high):
            print(f"Value must be between {low} and {high}.")
            continue
        return value


def ask_yes_no(prompt):
    while True:
        answer = input(prompt + " (y/n): ").strip().lower()
        if answer in ("y", "n"):
            return answer == "y"
        print("Please type y or n.")


def show(devices):
    if not devices:
        print("No devices to show.")
    for d in devices:
        print(d)  # polymorphism: each class formats its own status

