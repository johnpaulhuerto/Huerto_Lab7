name = (input("Enter Your Name:"))
section = (input("Enter Your Section:"))

#Grade

prelim = float (input("Enter Your Prelim Grade (40-100):"))
if prelim < 40 or prelim > 100:
    print("Invalid input, your grade must stay only betwenn (40-100)")
    
else:
    midterm = float (input("Enter Your Midterm Grade (40-100):"))

if midterm < 40 or midterm > 100:
    print("Invalid input, your grade must stay only betwenn (40-100)")
    
else:
    final = float (input("Enter Your Final Grade (40-100):"))
    
if final < 40 or final > 100:
    print("Invalid input, your grade must stay only betwenn (40-100)") 
        
#Final Grade

final_grade = (prelim * 0.3333) + (midterm * 0.3333) + (final * 0.3333)
print(f"Hi {name} from {section}, Your Final Grade is {final_grade:.0f}")

#GPA

if 99 <= final_grade <= 100:
    print("GPA: 1.00 = Exellecnt")
elif 96 <= final_grade <= 98:
    print("GPA: 1.25 = Outstanding")
elif 93 <= final_grade <= 95:
    print("GPA: 1.50 = Superior")       
elif 90 <= final_grade <= 92:
    print("GPA: 1.75 = Very Good")   
elif 87 <= final_grade <= 89:
    print("GPA: 2.00 = Good")   
elif 84 <= final_grade <= 86:
    print("GPA: 2.25 = Satisfactory")          
elif 81 <= final_grade <= 83:
    print("GPA: 2.50 = Fairly Satisfactory")         
elif 78 <= final_grade <= 80:
    print("GPA: 2.75 = Fair")         
elif 75 <= final_grade <= 77:
    print("GPA: 3.00 = Passed")
elif 0 <= final_grade <= 74:
    print("GPA: 5.0 = Failed")              