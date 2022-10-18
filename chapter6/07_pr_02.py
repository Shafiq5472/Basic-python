'''find out whether a student is pass or fail if it requires total 40%
and atleast 33% in each subject to pass.
Assume 3 subject and take makes an input from the user'''


sub1 = int(input("Enter first subject:\n"))
sub2 = int(input("Enter second subject:\n"))
sub3 = int(input("Enter third subject:\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail because you have less than 33% in one of the subject")

elif((sub3+sub2+sub1)/3 <40):
    print("You are fail due to total percentage less than 40")
else:
    print("pass")