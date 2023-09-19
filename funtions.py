#Variable calculation_to_units calculates given units
calculation_to_units = 24 *60 * 60

#Variable name_of_units prints the standard measure of calculated units
name_of_units = "seconds"

#A function is defined with the keyword 'def'
#days_to_units: a function to calculate days to units.
def days_to_units():
#printed calculated units
    print(f"20 days are {20 * calculation_to_units} {name_of_units}")
    print("All good!")

#After creating the function, you have to call the function in order for it to print the output.
days_to_units()