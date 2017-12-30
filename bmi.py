#!/bin/python

def gather_info():
    height = float(raw_input("What is your height? "))
    weight = float(raw_input("What is your weight? "))
    unit = raw_input("Are your measurments in metric or imperial units? ").lower().strip()
    return ( height, weight, unit)

def calculate_bmi(height, weight, unit='metric'):
    if unit == 'imperial':
        bmi = 703 * ( weight / (height ** 2))
    else:
        bmi = (weight / (height ** 2))
    print("your BMI is %s" % bmi)

while True:
    height, weight, unit = gather_info()
    if unit.startswith('i'):
        calculate_bmi(height=height, weight=weight, unit='imperial')
    elif unit.startswith('m'):
        calculate_bmi(height=height, weight=weight)
    else:
        print("Error: Unknown Measurement system.")
