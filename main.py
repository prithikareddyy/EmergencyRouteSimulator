print("=" * 45)
print("       EMERGENCY ROUTE SIMULATOR")
print("=" * 45)

print("\nWelcome to the Emergency Route Simulator!")
print("Find an available route to the hospital.")

# Store route information
routes = {
    "1": {"name": "Route A", "time": 15, "condition":"Clear"},
    "2": {"name": "Route B", "time": 20, "condition":"Heavy Traffic"},
    "3": {"name": "Route C", "time": 12, "condition":"Clear"}
}

blocked_routes = []
trip_history = []
# Display available routes
print("\n--- AVAILABLE ROUTES ---")

for number in routes:
    travel_time = routes[number]["time"]
    condition = routes[number]["condition"]

    if condition == "heavy traffic":
        travel_time = travel_time + 10

    print(
        number + ". " + routes[number]["name"]
        + " - " + str(travel_time)
        + " minutes"
        + " - " + condition.title()
    )

# Ask the user to select a route
choice = input("\nSelect a route (1/2/3): ").strip()

if choice not in routes:
    print("Invalid selection! Please enter 1, 2, or 3.")

else:
    # Check the selected road
    answer = input("Is this road blocked? (yes/no): ").strip().lower()

    if answer not in ["yes", "no"]:
        print("Invalid response! Please enter yes or no.")

    elif answer == "yes":
        print("Road blocked!")

    else:
        print("Road available!")
        
    if answer == "yes":
        blocked_routes.append(choice)

        print("\nRoad blocked! Please choose an alternative.")

        print("\n--- ALTERNATIVE ROUTES ---")

        for number in routes:
            if number not in blocked_routes:
                if number != choice:
                    print(
                        number + ". " + routes[number]["name"]
                        + " - " + str(routes[number]["time"])
                        + " minutes"
                    )


        alternative = input("\nSelect an alternative route: ")

        if alternative not in routes or alternative in blocked_routes or alternative == choice:
            print("Invalid alternative route.")

        else:
            print("\n--- EMERGENCY ROUTE REPORT ---")
            selected_route = routes[alternative]
            travel_time = selected_route["time"]

            if selected_route["condition"] == "heavy traffic":
                travel_time = travel_time + 10

            print("Selected route:", selected_route["name"])
            print("Estimated travel time:", travel_time, "minutes")
            print("Road status: Available")
            print("Destination: Hospital")
            print("Status: Alternative route selected")

    elif answer == "no":
        print("\n--- EMERGENCY ROUTE REPORT ---")
        selected_route = routes[choice]
        travel_time = selected_route["time"]

        if selected_route["condition"] == "heavy traffic":
            travel_time = travel_time + 10

        print("Selected route:", selected_route["name"])
        print("Estimated travel time:", travel_time, "minutes")
        original_time = routes[choice]["time"]

        if routes[choice]["condition"] == "heavy traffic":
            original_time = original_time + 10

        if travel_time < original_time:
            time_saved = original_time - travel_time
            print("Time saved:", time_saved, "minutes")

        elif travel_time > original_time:
            extra_time = travel_time - original_time
            print("Additional time:", extra_time, "minutes")

        else:
            print("Both routes have the same travel time.")
            print("Road status: Available")
            print("Destination: Hospital")
            print("Status: Route selected")

    else:
        print("Invalid response. Please enter yes or no.")
    
def show_history():
    print("\n--- TRIP HISTORY ---")

    if len(trip_history) == 0:
        print("No completed trips yet.")

    else:
        for trip in trip_history:
            print(
                "Route:", trip["route"],
                "| Travel time:", trip["time"], "minutes"
            )

        print("Total completed trips:", len(trip_history))
        
def show_menu():
    print("\n" + "=" * 40)
    print("       EMERGENCY ROUTE SIMULATOR")
    print("=" * 40)
    print("1. View available routes")
    print("2. Start emergency simulation")
    print("3. View project information")
    print("4. Exit")

def start_simulation():
    print("\n--- START EMERGENCY SIMULATION ---")

    choice = input("Select a route (1/2/3): ").strip()

    if choice not in routes:
        print("Invalid selection! Please enter a valid route number.")
        return

    answer = input("Is this road blocked? (yes/no): ").strip().lower()

    if answer not in ["yes", "no"]:
        print("Invalid response! Please enter yes or no.")
        return

    if answer == "yes":
        print("Road blocked! Please choose an alternative.")

        for number in routes:
            if number != choice:
                print(
                    number + ". " + routes[number]["name"]
                    + " - " + routes[number]["condition"].title()
                )

        alternative = input("Select an alternative route: ").strip()

        if (
            alternative not in routes
             or alternative == choice
        ):
            print("Invalid alternative route.")
            return

        selected_route = routes[alternative]
        original_route = routes[choice]

        if selected_route["condition"] == "blocked":
            print("That alternative road is blocked.")
            return

        travel_time = selected_route["time"]

        if selected_route["condition"] == "heavy traffic":
            travel_time += 10

        original_time = original_route["time"]

        if original_route["condition"] == "heavy traffic":
            original_time += 10

        print("\n--- EMERGENCY ROUTE REPORT ---")
        print("Selected route:", selected_route["name"])
        print("Estimated travel time:", travel_time, "minutes")
        trip_history.append({
            "route": selected_route["name"],
            "time": travel_time
        })

        if travel_time < original_time:
            print("Time saved:", original_time - travel_time, "minutes")
        elif travel_time > original_time:
            print("Additional time:", travel_time - original_time, "minutes")
        else:
            print("Both routes have the same travel time.")

    else:
        selected_route = routes[choice]
        travel_time = selected_route["time"]

        if selected_route["condition"] == "heavy traffic":
            travel_time += 10

        print("\n--- EMERGENCY ROUTE REPORT ---")
        print("Selected route:", selected_route["name"])
        print("Estimated travel time:", travel_time, "minutes")
        print("Road status: Available")
        print("Destination: Hospital")

while True:
    show_menu()

    choice = input("\nEnter your choice (1-4): ").strip()

    if choice == "1":
        print("\n--- AVAILABLE ROUTES ---")

        for number in routes:
            travel_time = routes[number]["time"]
            condition = routes[number]["condition"]

            if condition == "heavy traffic":
                travel_time = travel_time + 10

            print(
                number + ". " + routes[number]["name"]
                + " - " + str(travel_time)
                + " minutes - " + condition.title()
            )

    elif choice == "2":
        start_simulation()

    elif choice == "3":
        print("\n--- PROJECT INFORMATION ---")
        print("Project: Emergency Route Simulator")
        print("Purpose: Simulate ambulance route selection")
        print("Routes available:", len(routes))
        print("Traffic delay: 10 minutes")
        print("Road conditions: Clear, Heavy Traffic, Blocked")
        print("Technology: Python")
        print("Data source: Simulated sample data")

    elif choice == "4":
        print("\nExiting Emergency Route Simulator. Goodbye!")

    else:
        print("\nInvalid choice! Please enter a number from 1 to 4.")