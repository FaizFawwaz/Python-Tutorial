# Weight (in pounds) and height (in inches) are input by the user
weight = float(input('Enter your weight in pounds: '))
height = float(input('Enter your height in inches: '))

# BMI 
def BMI(height, weight):
    BMI = weight / (height * height) * 703
    
    
    if (BMI < 16):
        return 'severely underweight', BMI
    
    elif (BMI < 18.5):
        return 'underweight', BMI
    
    elif (BMI < 25):
        return 'normal', BMI
    
    elif (BMI < 30):
        return 'overweight', BMI
    
    elif (BMI < 35):
        return 'obese', BMI
    
quote, BMI = BMI(height, weight)
print('your BMI is: {} and you are: {}'.format(BMI,quote))
    
            