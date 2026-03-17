"""

Fare Estimation
================
input:distance_in_km,base_fare
equation:estimated_fare=50+(distance*base_fare)
output: estimated_fare
"""
base_fare =30
distance_in_km=5
estimated_fare=base_fare+(distance_in_km*base_fare)
print("Estimated Fare:", estimated_fare)