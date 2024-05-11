def physics_calculator():
    print("Keith McKenzie (2023)")
    print("Project Two - Licensed under the GPL-3.0")
    print("")
    print("Welcome to the Basic Physics Calculator!")
    print("If you do not want to calculate anything click enter to close this program.")
    print("Select what you want to calculate:")
    print("")
    print("1. Force")
    print("2. Mass")
    print("3. Acceleration")
    print("4. Speed")
    print("5. Distance")
    print("6. Time")
    print("")
    
    choice = int(input("Enter your choice (1-6): "))
    
    if choice == 1:
        # Calculate Force
        mass = float(input("Enter the mass (kg): "))
        acceleration = float(input("Enter the acceleration (m/s^2): "))
        force = mass * acceleration
        print("")
        print(f"Force = {force} N")
        print("")
        
    elif choice == 2:
        # Calculate Mass
        force = float(input("Enter the force (N): "))
        acceleration = float(input("Enter the acceleration (m/s^2): "))
        mass = force / acceleration
        print("")
        print(f"Mass = {mass} kg")
        print("")
        
    elif choice == 3:
        # Calculate Acceleration
        force = float(input("Enter the force (N): "))
        mass = float(input("Enter the mass (kg): "))
        acceleration = force / mass
        print("")
        print(f"Acceleration = {acceleration} m/s^2")
        print("")
        
    elif choice == 4:
        # Calculate Speed
        distance = float(input("Enter the distance (m): "))
        time = float(input("Enter the time (s): "))
        speed = distance / time
        print("")
        print(f"Speed = {speed} m/s")
        print("")
        
    elif choice == 5:
        # Calculate Distance
        speed = float(input("Enter the speed (m/s): "))
        time = float(input("Enter the time (s): "))
        distance = speed * time
        print("")
        print(f"Distance = {distance} m")
        print("")
        
    elif choice == 6:
        # Calculate Time
        distance = float(input("Enter the distance (m): "))
        speed = float(input("Enter the speed (m/s): "))
        time = distance / speed
        print("")
        print(f"Time = {time} s")
        print("")
    else:
        print("Invalid choice. Please select a number between 1 and 6.")
    
    input("Press any key to close...")
        
if __name__ == "__main__":
    physics_calculator()
