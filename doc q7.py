# Q7.Write function bmi that calculates body mass index (bmi = weight / height2).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"
def index(weight,height):
    bmi=weight/height
    if bmi<=18.5:
        return "underweight"
    elif bmi<=25.0:
        return "normal"
    elif bmi<=30.0:
        return "overweight"
    else:
        return "obese"
print(index(34,75))
