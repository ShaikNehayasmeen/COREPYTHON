
def convert_distance(feet):
    inches = feet * 12
    yards = feet / 3
    miles = feet / 5280
    
    
    print(f"Distance in feet : {feet}")
    print(f"Distance in inches : {inches}")
    print(f"Distance in yards : {yards}")
    print(f"Distance in miles : {miles}")


feet = float(input("Enter the distance in feet : "))

convert_distance(feet)
