import tkinter as tk
from tkinter import messagebox

def calculate_life_expectancy():
    try:
        age = int(age_entry.get())
        if age < 0:
            raise ValueError("Age cannot be negative")

        life_expectancy = 80

        if exercise_var.get() == "Daily":
            life_expectancy += 4
        elif exercise_var.get() == "Weekly":
            life_expectancy += 2
        elif exercise_var.get() == "Rarely":
            life_expectancy -= 1
        elif exercise_var.get() == "Never":
            life_expectancy -= 3

        if diet_var.get() == "Healthy":
            life_expectancy += 4
        elif diet_var.get() == "Average":
            life_expectancy += 1
        elif diet_var.get() == "Unhealthy":
            life_expectancy -= 3

        if smoking_var.get() == "No":
            life_expectancy += 5
        elif smoking_var.get() == "Yes":
            life_expectancy -= 8

        if alcohol_var.get() == "Never":
            life_expectancy += 3
        elif alcohol_var.get() == "Rarely":
            life_expectancy += 1
        elif alcohol_var.get() == "Weekly":
            pass
        elif alcohol_var.get() == "Daily":
            life_expectancy -= 3

        if stress_var.get() == "Low":
            life_expectancy += 2
        elif stress_var.get() == "High":
            life_expectancy -= 3

        estimated_life_expectancy = life_expectancy - age
        result_message = f"Your estimated life expectancy is around {int(age + estimated_life_expectancy)} years."
        messagebox.showinfo("Life Expectancy Estimate", result_message)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid age.")

root = tk.Tk()
root.title("Life Expectancy Estimator")
root.geometry("400x500")
root.configure(bg="#f7f7f7")

tk.Label(root, text="Enter your age:", font=("Arial", 12), bg="#f7f7f7").pack(pady=5)
age_entry = tk.Entry(root, font=("Arial", 12))
age_entry.pack(pady=5)

tk.Label(root, text="How often do you exercise?", font=("Arial", 12), bg="#f7f7f7").pack(pady=5)
exercise_var = tk.StringVar(value="Select")
for text in ["Daily", "Weekly", "Rarely", "Never"]:
    tk.Radiobutton(root, text=text, variable=exercise_var, value=text, font=("Arial", 10), bg="#f7f7f7").pack(anchor="w")

tk.Label(root, text="How would you describe your diet?", font=("Arial", 12), bg="#f7f7f7").pack(pady=5)
diet_var = tk.StringVar(value="Select")
for text in ["Healthy", "Average", "Unhealthy"]:
    tk.Radiobutton(root, text=text, variable=diet_var, value=text, font=("Arial", 10), bg="#f7f7f7").pack(anchor="w")

tk.Label(root, text="Do you smoke?", font=("Arial", 12), bg="#f7f7f7").pack(pady=5)
smoking_var = tk.StringVar(value="Select")
for text in ["Yes", "No"]:
    tk.Radiobutton(root, text=text, variable=smoking_var, value=text, font=("Arial", 10), bg="#f7f7f7").pack(anchor="w")

tk.Label(root, text="How often do you drink alcohol?", font=("Arial", 12), bg="#f7f7f7").pack(pady=5)
alcohol_var = tk.StringVar(value="Select")
for text in ["Never", "Rarely", "Weekly", "Daily"]:
    tk.Radiobutton(root, text=text, variable=alcohol_var, value=text, font=("Arial", 10), bg="#f7f7f7").pack(anchor="w")

tk.Label(root, text="How would you rate your stress levels?", font=("Arial", 12), bg="#f7f7f7").pack(pady=5)
stress_var = tk.StringVar(value="Select")
for text in ["Low", "Moderate", "High"]:
    tk.Radiobutton(root, text=text, variable=stress_var, value=text, font=("Arial", 10), bg="#f7f7f7").pack(anchor="w")

calculate_button = tk.Button(root, text="Calculate Life Expectancy", command=calculate_life_expectancy, font=("Arial", 12), bg="#4CAF50", fg="white")
calculate_button.pack(pady=20)

root.mainloop()

