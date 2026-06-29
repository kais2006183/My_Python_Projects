#======================================================================================================================
# myfavoritwebs = []

# # =======================================================
# #  (اPassword)
# # =======================================================
# Password = "kais@123"
# Attempts = 4
# access_granted = False  ا

# print("=== Welcome to Bookmark Manager ===")

# while Attempts > 0:
#     inputpassword = input("Write the password here to unlock the program: ").strip()
    
#     if inputpassword == Password:
#         print("Correct Password. Program Unlocked!\n")
#         access_granted = True
#         break 
#     else:
#         Attempts -= 1
#         if Attempts > 0:
#             print(f"Wrong Password! {'Last' if Attempts == 1 else Attempts} Tries Left. Try again.")
#         else:
#             print("You've Finished All Tries. Access Denied!")

# # =======================================================
# # if password write open bookmark
# # =======================================================
# if access_granted:
    
#    #     maxwebs = 3
    
#     while maxwebs > 0:
#         web = input("Write Website Name Without https:// ")
#         myfavoritwebs.append(web.strip().lower())
        
#         maxwebs -= 1
#         print(f"Website Added, {maxwebs} Places Left")
#         print(f"['https://{web.strip().lower()}']")
#         print(myfavoritwebs)
#     else:
#         print("Bookmark Is Full, You Can't Add Any Webs More.")
        
#     print("=" * 50)
    
#   
#     qustion = input("Do you need to look in your websites list? ").lower().capitalize()
    
#     if qustion == "Yes" or qustion == "Y":
#         print("that's your list of websites. ")
#         if len(myfavoritwebs) > 0:
#             myfavoritwebs.sort()
            
#             index = 0
#             print("Printing the websites list in your bookmark: ")
#             while index < len(myfavoritwebs):
#                 print(myfavoritwebs[index])
#                 index += 1
#         else:
#             print("Your list is empty.")
            
#     elif qustion == "No" or qustion == "N":
#         print("Ok Thank you .")



#======================================================================================================================




# skill_level = {
#     "Html" : "70%",
#     "CSS" : "70%",
#     "Python" : "80%"
# }

# for skill, progress in skill_level.items() :
#     print(f"your skill {skill} => {progress}")

#======================================================================================================================



# raw_names = ["  kaIs ", " osama", "KAIS  ", "  AhMeD ", "osama "]
# Clean_Names = []

# for name in raw_names:
#     fixed_name = name.strip().capitalize()
    
#     if fixed_name not in Clean_Names:
#         Clean_Names.append(fixed_name)
#         
#         print(f"Added to list: '{fixed_name}'")

# print(f"\nFinal Clean List: {Clean_Names}")


#======================================================================================================================


# websites = ["www.google.com", "www.elzero.org", "www.facebook.com", "www.python.org", "www.github.com"]

# for website in websites :

#     print(f"Valid Website => {website[4:][:-4]}") 

#     if website == "www.elzero.org" :
#         print("This is an Organization Website.")
#         break

#======================================================================================================================


# grades = [45, 82, 33, 91, 50, 48, 70]
# total_grades = 0

# for grade in grades:
#     if grade < 50:
#         boosted_grade = grade + 5
#         print(f"{boosted_grade} (Boosted)")
#         total_grades += boosted_grade  
#     elif grade >= 50:
#         print(f"{grade} (Passed)")
#         total_grades += grade        

# # نطبع المتغير total_grades وليس القائمة grades
# print(f"\nAll Total grade: {total_grades}")

#======================================================================================================================


# prices = [15, 120, 8, 250, 45, 12]
# total_cost = 0

# for price in prices :

#     if price >= 100 :
#         print(f"{price} (Expensive Piece)")
#     elif price < 100 :
#         print(f"{price} (Cheap Piece)")
    
#     total_cost += price 

# print(f"\nTotal Cost is : {total_cost}$")

#======================================================================================================================


# developers = {
#     "Kais": "Python", 
#     "Osama": "PHP", 
#     "Ahmed": "Python", 
#     "Ali": "Java"
# }

# python_count = 0


# for name, lang in developers.items():
#     print(f"Developer => {name} - Language => {lang}")
    
#     if lang == "Python":
#         python_count += 1

# print(f"Total Developer Python : {python_count}")
#======================================================================================================================

# data = [["Kais", 2], ["Osama", 10], ["Ahmed", 5], ["Anas", 1]]

# for name, years in data :

#     if years > 3 :
#         print (f"Programer : {name} - Experince : {years} years - sinior")
#     elif years <= 3 :
#         print (f"Programer : {name} - Experince : {years} years - junior")
#======================================================================================================================


# mixed_data = ["Kais", 100, "Python", True, 400, "Elzero", 700]
# numbers_only = []
# total_num = 0

# for numbers in mixed_data :
#     if type(numbers) == int :
#      numbers_only.append(numbers)
#      total_num += numbers

# print (numbers_only)
# print (f"Total numbers : {total_num}")

#======================================================================================================================
# students = ["Kais", "Ahmed", "Osama", "Anas", "Ali"]

# serach = input("Please Write Your Name : ").capitalize().strip()

# for name in students :
#     if name == serach :
#         print(f"Welcome {name} to the class.")
#         break
# else :
#     print("Sorry, You are not in the class.")
#======================================================================================================================

# users_data = {}
# counter = 1 
# while counter <= 3 :
#     print (f"Entring employee {counter} :")

#     name = input("Write Your name here :")
#     job = input("Write Your job here :")

#     users_data[name] = job 
#     counter += 1 

# print("\nFinal rebort : ")
# print(users_data)

#======================================================================================================================

# users_data = {}

# while True :
#         name = input("Write Your name here : ").capitalize().strip()
#         job = input("Write Your job here : ").capitalize().strip()

#         users_data[name] = job 
#         key = input("Type 'quit' or 'q' to stop or any key to continue: ").strip().lower()

#         if key == 'quit' or key == 'q' :
#                 print("thank you")
#                 break

# print("\nFinal Report : ")
# print(users_data)

#======================================================================================================================
# z = 5

# while z > 0 :
#     z -= 1
#     if z % 2 == 0 :
#         print(f"Even Number: {z}")
#     else :
#         print(f"Odd Number: {z}")

#======================================================================================================================

# team = {
#     "Kais": 500,
#     "Ahmed": 120,
#     "Osama": 300,
#     "Ali": 50
# }
# Total_bonus = 0
# for name, lines in team.items() : 
#     if lines >= 200 :
#         print(f"{name} => Bonus : 50$ ")
#         Total_bonus += 50
#     elif lines >= 100 and lines < 200 :
#         print(f"{name} => Bonus : 25$ ")
#         Total_bonus  += 25
#     else :
#         print(f"{name} => No Bonus. ")
#         Total_bonus += 0 

# print(Total_bonus) 
#======================================================================================================================
