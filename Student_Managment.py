import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Student Management System")
window.geometry("400x420")
window.config(bg="#f5f5f5")

# Your Data Dictionary and Generator
student_database = {}

def id_generator():
    student_id = 1001
    while True:
        yield student_id
        student_id += 1

id_factory = id_generator()

def get_student_status(score):
    if score >= 90:
        return "Excellent!!"
    elif score >= 60:
        return "Acceptable!!"
    else: 
        return "Failed."

def add_student_action():
    name = name_entry.get().strip()
    score_raw = score_entry.get().strip()
    
    if not name or not score_raw:
        messagebox.showwarning("Empty Fields", "Please fill in all fields!")
        return 

    try:
        score = float(score_raw)
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100.")
            
        current_id = next(id_factory)
        status = get_student_status(score)
        
        # Storing data in the dictionary as a valid sub-dictionary
        student_database[current_id] = {"name": name, "score": score, "status": status}
        
        success_msg = f"Student Added Successfully!\n🆔 ID: {current_id}\n📊 Status: {status}"
        messagebox.showinfo("Success", success_msg)
        
        name_entry.delete(0, tk.END)
        score_entry.delete(0, tk.END)
        
    except ValueError as error:
        messagebox.showerror("Invalid Input", f"Error: {error}")

# ==========================================
# New function for the report save button (File Logic)
# ==========================================
def save_report_action():
    # 1. First, check if the dictionary is empty and the user has not yet added any student.
    if not student_database:
        messagebox.showwarning("No Data", "No student data to save! Please add students first.")
        return

    try:
        # 2. Opening the file and writing to it using your organized code
        with open(r"D:\kais2\Python\student_report.txt", "w") as file:
            file.write("=== STUDENTS FINAL REPORT ===\n")
            
            for s_id, info in student_database.items():
                line = f"Id: {s_id} | Name: {info['name']} | Score: {info['score']} | Status: {info['status']}\n"
                file.write(line)
        
        # 3. Display a success message to the user after successfully writing the file.
        messagebox.showinfo("Saved", "All data has been saved successfully to 'student_report.txt'!")
        
    except Exception as e:
        # Warning in case of an issue with the folder path or permissions.
        messagebox.showerror("File Error", f"Could not save file: {e}")


# ==========================================
# Graphical User Interface Design
# ==========================================
header_label = tk.Label(window, text="🎓 Student System 📚", font=("Arial", 16, "bold"), bg="#f5f5f5", fg="#333333")
header_label.place(x=90, y=20)

name_label = tk.Label(window, text="👤 Student Name:", font=("Arial", 12), bg="#f5f5f5", fg="#555555")
name_label.place(x=30, y=90)

score_label = tk.Label(window, text="📝 Student Score:", font=("Arial", 12), bg="#f5f5f5", fg="#555555")
score_label.place(x=30, y=140)

name_entry = tk.Entry(window, font=("Arial", 12), width=20, bd=2, relief="groove")
name_entry.place(x=170, y=90)

score_entry = tk.Entry(window, font=("Arial", 12), width=20, bd=2, relief="groove")
score_entry.place(x=170, y=140)

# The Add button is linked to its function.
add_btn = tk.Button(window, text="➕ Add Student", font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", width=14, bd=3, relief="raised", command=add_student_action)
add_btn.place(x=40, y=210)

# ------------------------------------------
# Final binding of the Save button to the command parameter
# ------------------------------------------
save_btn = tk.Button(
    window, 
    text="💾 Save Report", 
    font=("Arial", 11, "bold"), 
    bg="#008CBA", 
    fg="white", 
    width=14, 
    bd=3, 
    relief="raised",
    command=save_report_action  # The save button has been successfully linked to the function!
)
save_btn.place(x=210, y=210)

window.mainloop()