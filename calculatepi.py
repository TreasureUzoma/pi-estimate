import mpmath

def calculate_pi_to_high_precision(line_length_cm, precision):
    # Set the precision for mpmath
    mpmath.mp.dps = precision
    
    # Calculate pi to the specified precision
    pi = mpmath.pi
    
    # Calculate the diameter of the circle
    diameter = mpmath.mpf(line_length_cm) / pi
    
    # Calculate the ratio of circumference to diameter
    pi_approximation = mpmath.mpf(line_length_cm) / diameter
    
    return pi_approximation, diameter

# User input for the line length and precision
line_length_cm = 1000
precision = int(input("Enter the precision for π calculation (number of decimal places): "))

pi_approx, diameter = calculate_pi_to_high_precision(line_length_cm, precision)

print(f"Length of the line: {line_length_cm} cm")
print(f"Diameter of the circle: {diameter}")
print(f"Approximated value of π: {pi_approx}")
