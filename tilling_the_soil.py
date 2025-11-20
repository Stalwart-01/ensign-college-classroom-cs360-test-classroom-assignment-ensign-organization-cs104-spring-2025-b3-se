import math

# Constants
COVERAGE_PER_BAG = 2000
BAG_COST = 27
NITROGEN_PER_BAG = 1
POTASSIUM_PER_BAG = 0.125
AREA_PER_HOUR = 2500
LABOR_RATE = 20

# Input
print("Enter lawn dimensions in feet (enter 0 if section is missing):")

front_length = float(input("Front length: "))
front_width = float(input("Front width: "))
rear_length = float(input("Rear length: "))
rear_width = float(input("Rear width: "))
left_length = float(input("Left length: "))
left_width = float(input("Left width: "))
right_length = float(input("Right length: "))
right_width = float(input("Right width: "))

# Calculations
total_area = (
    (front_length * front_width)
    + (rear_length * rear_width)
    + (left_length * left_width)
    + (right_length * right_width)
)

bags_needed = math.ceil(total_area / COVERAGE_PER_BAG)
fertilizer_cost = bags_needed * BAG_COST
labor_hours = math.ceil(total_area / AREA_PER_HOUR)
labor_cost = labor_hours * LABOR_RATE
total_cost = fertilizer_cost + labor_cost

# Nutrients using actual number of bags (not rounded)
actual_bags = total_area / COVERAGE_PER_BAG
nitrogen = actual_bags * NITROGEN_PER_BAG
potassium = actual_bags * POTASSIUM_PER_BAG

# Output
print("\n--- Fertilizer Application Summary ---")
print(f"Total Area: {int(total_area)} sq ft")
print(f"Bags Needed: {bags_needed}")
print(f"Fertilizer Cost: ${fertilizer_cost:.2f}")
print(f"Labor Hours: {labor_hours}")
print(f"Labor Cost: ${labor_cost:.2f}")
print(f"Total Cost: ${total_cost:.2f}")
print(f"Nitrogen Applied: {nitrogen:.3f} lbs")
print(f"Potassium Applied: {potassium:.3f} lbs")

