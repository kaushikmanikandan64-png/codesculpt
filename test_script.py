def add_numbers(a, b):
    return a + b

def calculate_velocity(distance, time):
    if time == 0:
        raise ValueError("Time cannot be zero")
    return distance / time