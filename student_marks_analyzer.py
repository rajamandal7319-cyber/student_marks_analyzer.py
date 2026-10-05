print("STUDENT MARKS ANALYZER")

name = input("Apna naam likho: ")
print("Tumhara naam hai:", name)

maths = int(input("Maths ke marks likho: "))

if maths >= 90:
    maths_grade = "A+"
elif maths >= 80:
    maths_grade = "A"
elif maths >= 70:
    maths_grade = "B"
elif maths >= 60:
    maths_grade = "C"
elif maths >= 50:
    maths_grade = "D"
elif maths >= 40:
    maths_grade = "E"
else:
    maths_grade = "F"

print("Maths Grade:", maths_grade)

English = int(input("English ke marks likho: "))

if English >= 90:
    English_grade = "A+"
elif English >= 80:
    English_grade = "A"
elif English >= 70:
    English_grade = "B"
elif English >= 60:
    English_grade = "C"
elif English >= 50:
    English_grade = "D"
elif English >= 40:
    English_grade = "E"
else:
    English_grade = "F"

print("English grade:", English_grade)

science = int(input("Science ke marks likho: "))

if science >= 90:
    science_grade = "A+"
elif science >= 80:
    science_grade = "A"
elif science >= 70:
    science_grade = "B"
elif science >= 60:
    science_grade = "C"
elif science >= 50:
    science_grade = "D"
elif science >= 40:
    science_grade = "E"
else:
    science_grade = "F"

print("Science Grade:", science_grade)

bengali = int ( input("bengali ke marks likho:"))

if bengali >= 90:
    bengali_grade = "A+"
elif bengali >= 80:
    bengali_grade = "A"
elif bengali >= 70:
    bengali_grade = "B"
elif bengali >= 60:
    bengali_grade = "C"
elif bengali >= 50:
    bengali_grade = "D"
elif bengali >= 40:
    bengali_grade = "E"
else:
    bengali_grade = "F"

print("Bengali Grade:", bengali_grade)

computer = int(input("computer ke marks likho:"))

if computer >= 90:
    computer_grade = "A+"
elif computer >= 80:
    computer_grade = "A"
elif computer >= 70:
    computer_grade = "B"
elif computer >= 60:
    computer_grade = "C"
elif computer >= 50:
    computer_grade = "D"
elif computer >= 40:
    computer_grade = "E"
else:
    computer_grade = "F"

print("Computer Grade:", computer_grade)

history = int(input("history ke marks likho:"))

if history >= 90:
    history_grade = "A+"
elif history >= 80:
    history_grade = "A"
elif history >= 70:
    history_grade = "B"
elif history >= 60:
    history_grade = "C"
elif history >= 50:
    history_grade = "D"
elif history >= 40:
    history_grade = "E"
else:
    history_grade = "F"

print("History Grade:", history_grade)

geography = int(input("geography ke marks likho:"))

if geography >= 90:
    geography_grade = "A+"
elif geography >= 80:
    geography_grade = "A"
elif geography >= 70:
    geography_grade = "B"
elif geography >= 60:
    geography_grade = "C"
elif geography >= 50:
    geography_grade = "D"
elif geography >= 40:
    geography_grade = "E"
else:
    geography_grade = "F"

print("geography Grade:", geography_grade)

total = maths + English + science + bengali + computer + history + geography
print("Total marks:", total)

percentage = total / 7
print ("percentage: " , percentage , "%" )
if percentage >=90:
     grade = "A+"
elif percentage >=80:
     grade ="A"
elif percentage >=70:
     grade ="B"
elif percentage >=60:
      grade ="C"
elif percentage >=50:
      grade ="D"
elif percentage >=40:
       grade ="E"
else:
        grade ="F"
        
print("Grade:" , grade)        
        
if percentage >= 40:
        print("Result: Pass")
else:
        print( ' Result: Fail ' )
                
