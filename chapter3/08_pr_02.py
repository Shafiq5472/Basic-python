#letter template #letter using escape sequences
letter='''Dear <|NAME|>, \n\tYou are selected! \n\t<|DATE|>'''
print(letter)
name=input("Enter Your Name")
date=input("Enter Date")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)
