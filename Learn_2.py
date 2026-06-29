# ==================================================================================================================

# def user_name (name, age, country= "Unknown") :
#     if age >= 18 :
#         return f"Hello {name},Your age is {age}, You Are Allowed. Your Country Is {country}"
#     if age < 18 : 
#         return f"Hello {name}, You Are Too Young!"
    

# print(user_name('kais', 20, 'syria'))
# print(user_name('kais', 20))
# print(user_name('jawad', 16))
# ==================================================================================================================

# def calculate_bill(discount, *prices):
#     # 1. نجمع كل الأسعار الممررة أولاً لتصبح قيمة واحدة (200 + 300 + 400 = 900)
#     total_price = sum(prices)
    
#     # 2. نطبق المعادلة الذكية التي تعلمتها على المجموع الكلي
#     final_price = total_price - (total_price * discount / 100)
    
#     # 3. نرجع النص باستخدام return بدلاً من print لمنع ظهور None
#     return f"Total Price After Discount is: {final_price}"

# # الآن عند طباعة استدعاء الدالة ستظهر النتيجة الإجمالية الموحدة مباشرة
# print(calculate_bill(10, 200, 300, 400))
# ==================================================================================================================

# def show_skills(name, **skills) :
#     print(f"Hello {name}, Here Are Your Skills : ")
#     for skill,progress in skills.items() :
#         print(f"- {skill} => {progress}")
# show_skills("Kais", Python="90%", Football="95%", Gaming="85%")
# ==================================================================================================================

# user_status = "active"

# def process_user(name: str) -> str:
#     global user_status
    
#     # 1. ننظف الاسم أولاً في بداية الدالة
#     clean_name = name.strip().capitalize()
    
#     # 2. نفحص الاسم المنظف
#     if clean_name == "Kais":
#         user_status = "admin" # التغيير يحدث فقط لو كان Kais
#         return f"User {clean_name} is processed."
    
#     # 3. خروج بديل في حال كان المستخدم شخصاً آخر (حتى لا تظهر None)
#     return f"User {clean_name} is a regular guest."

# print(user_status)
# print(process_user("   kais   ")) # ستعمل الآن بكفاءة وبدون فراغات
# print(user_status)
# ==================================================================================================================
# shortcut_double = lambda number :  number * 2
# print(shortcut_double(15))
# ==================================================================================================================

# # القائمة التي نريد فلترتها
# numbers_list = [12, 5, 20, 8, 15, 30, 7]

# # الدالة التقليدية تستقبل القائمة، وتستقبل دالة الفحص (condition)
# def filter_numbers(lst, condition):
#     result = []
#     for num in lst:
#         # هنا الـ condition هي دالة الـ lambda التي سنمررها بالأسفل
#         if condition(num) == True: 
#             result.append(num)
#     return result

# # جرب الآن طباعة الاستدعاءات التالية وشاهد السحر في الـ Terminal:
# print(filter_numbers(numbers_list, lambda x: x > 10))  # ستطبع الأرقام الأكبر من 10
# print(filter_numbers(numbers_list, lambda x: x % 2 == 0))  # ستطبع الأرقام الزوجية
# ==================================================================================================================
# try : # Try The Code 

#     number = int(input("Please Write Your Age : "))

#     if number < 18 :
#         print("Sorry You'r Not In Legal Age, You are under 18.")

#     else :
#         print(f"Good, Your Age Is {number}, From Try ")

# except : # Handil The Error

#     print("Bad, This is Not Integer,\n Please Try Again but With Integer.!")
# ==================================================================================================================


#     # Generator Example
# def count_up_to(max_num):
#     count = 1
#     while count <= max_num:
#         yield count
#         count += 1

# counter = count_up_to(3)
# print(next(counter))  # 1
# print(next(counter))  # 2

# ==================================================================================================================