#Variables
#When defining variables, it is important to use descriptive variable names for easy reading and future use.


#Variable calculation_to_units calculates given units
calculation_to_units = 24 *60 * 60

#Variable name_of_units prints the standard measure of calculated units
name_of_units = "seconds"

#printed calculated units
print(f"20 days are {20 * calculation_to_units} {name_of_units}")
print(f"50 days are {50 * calculation_to_units} {name_of_units}")
print(f"70 days are {70 * calculation_to_units} {name_of_units}")
print(f"100 days are {100 * calculation_to_units} {name_of_units}")
print(f"366 days are {366 * calculation_to_units} {name_of_units}")