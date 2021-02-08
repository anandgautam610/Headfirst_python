Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(5)
SyntaxError: invalid syntax
>>> for i in range(5):
	right_this_minutes = datetime.today().minute

if right_this_minutes in odds:
    print("This minutes seems a little odd.")
else:
    print("Not an odd minute.")
    
SyntaxError: invalid syntax
>>> for i in range(5):
	right_this_minutes = datetime.today().minute
        if right_this_minutes in odds:
            print("This minutes seems a little odd.")
        else:
            print("Not an odd minute.")
            
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for i in range(5):
	right_this_minutes = datetime.today().minute
        if right_this_minutes in odds:
                print("This minutes seems a little odd.")
        else:
                print("Not an odd minute.")
                
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> from datetime import datetime
>>> odds = [1,3,5,7,9,11,13,15,17,19,
        21,23,25,27,29,31,33,35,37,39,
        41,43,45,47,49,51,53,55,57,59]
>>> for i in range(5):
	right_this_minutes = datetime.today().minute
	if right_this_minutes in odds:
		print("This minutes seems a little odd.")

		
This minutes seems a little odd.
This minutes seems a little odd.
This minutes seems a little odd.
This minutes seems a little odd.
This minutes seems a little odd.
>>> for i in range(5):
	right_this_minutes = datetime.today().minute
	if right_this_minutes in odds:
		print("This minutes seems a little odd.")
	else:
		print("Not an odd minute.")

		
Not an odd minute.
Not an odd minute.
Not an odd minute.
Not an odd minute.
Not an odd minute.
>>> for i in range(5):
	right_this_minutes = datetime.today().minute
	if right_this_minutes in odds:
		print("This minutes seems a little odd.")
	else:
		print("Not an odd minute.")

		
This minutes seems a little odd.
This minutes seems a little odd.
This minutes seems a little odd.
This minutes seems a little odd.
This minutes seems a little odd.
>>> 