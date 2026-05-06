# STRING FUNCTIONS
course = 'Python is perfect'
course.upper() # makes all letters uppercase
course.lower() # makes all letters lowercase
course.title() # changes first letters uppercase for each word in string
course.strip() # removes white spaces from beginning and ending part of string
course.lstrip() # removes white spaces from beginning part of string
course.rstrip() # removes white spaces from ending part of string
course.find("per") # finds the starting index of given substring. if not found it return -1
course.replace("thon", "charm") # changes "thon" substring with "charm"
print("charm" in course)
print("thon" not in course)