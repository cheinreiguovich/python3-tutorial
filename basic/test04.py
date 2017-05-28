# BMI check

h = 1.75
w = 80.5

bmi = w/(h*h)

if bmi < 18.5:
    print('Over light')
elif 18.5 <= bmi < 25:
    print('Normal')
elif 25 <= bmi < 28:
    print('Overweight')
elif 28 <= bmi < 32:
    print('Corpulent')
else:
    print('Heavily overweight')