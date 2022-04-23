# Hunter Pollard
# This program is used to allow people to choose different calculators for peoples fitness desires
# Here are the numeric operators and functions that couldn't fit into my program
# Divides numbers without remained (Floor Division)
# print(11 // 5)
# Prints remainder for division (Modulus)
# print(11 % 5)
# End comment (Puts a space instead of ending the line of code)
# This function is used to calculate the user's BMI as they choose in the menu
# It uses height and weight arguments in order to get their calculation
# I used a while loop here to meet the requirements of the inspection
# It doesn't serve an actual purpose
def bmi_calculator(height_in, weight_lbs):
    y = 1
    while y > 0:
        bmi = weight_lbs * 703 / height_in ** 2
        if 18.5 <= bmi <= 24.9:
            # The formatting is used to print a number with 2 decimals after
            print("Congratulations, you're bmi is {:,.2f}.".format(bmi))
            print("You're in the healthy range of BMI.")
        elif bmi < 18.5 or bmi > 24.9:
            print("You're bmi is {:,.2f}.".format(bmi), "This is an unhealthy BMI.")
        y -= 1


# This function is used to calculate the user's body fat percentage
# It uses their bmi, age, and gender as arguments to calculate
# The for loop doesn't serve a purpose other than to meet requirements
# I had to incorporate gender, so I could get more specific percentages
def body_fat_percentage_calculator(bmi_2, age, gender):
    for x in range(1):
        if gender == "Man":
            body_fat_percentage_man = 1.20 * bmi_2 + 0.23 * age - 16.2
            # Formatting is used to print a number with 2 decimals after
            print("Your body fat percentage is {:,.2f}.".format(body_fat_percentage_man))
        elif gender == "Women":
            body_fat_percentage_women = 1.20 * bmi_2 + 0.23 * age - 5.4
            print("Your body fat percentage is {:,.2f}.".format(body_fat_percentage_women))


# This function is used to tracker a person's calories over a week
# It doesn't have to pass any arguments, it depends on user input
def calorie_tracker():
    # For Monday
    # Calorie goal variable states the amount a person wants to intake for that day
    calorie_goal_m = int(input("Enter calorie intake goal, for Monday: "))
    # Calorie intake variable is the actual amount the person has intake that day
    calorie_intake_m = int(input("Enter calorie intake for Monday: "))
    # In order to tell the user if they met their goal I had to create three if
    # statements
    # I did this for every day of the week and changed the last character to
    # match the day
    if calorie_goal_m == calorie_intake_m:
        # Multiplication comment for string operators
        # Prints "Nice!" three times
        print("Nice!" * 3)
        print("you have met your goal for today!")
    elif calorie_goal_m > calorie_intake_m:
        print("Intake more calories by:", calorie_goal_m - calorie_intake_m, "")
    elif calorie_goal_m < calorie_intake_m:
        print("Intake less calories by:", calorie_intake_m - calorie_goal_m, "")
    # For Tuesday
    calorie_goal_t = int(input("Enter calorie intake goal for Tuesday: "))
    calorie_intake_t = int(input("Enter calorie intake for Tuesday: "))
    if calorie_goal_t == calorie_intake_t:
        print("Nice!" * 3)
        print("you have met your goal for today!")
    elif calorie_goal_t > calorie_intake_t:
        # concatenation comment for string operators
        print("Intake more" + "calories by:", calorie_goal_t - calorie_intake_t, "")
    elif calorie_goal_t < calorie_intake_t:
        print("Intake less calories by:", calorie_intake_t - calorie_goal_t, "")
    # For Wednesday
    calorie_goal_w = int(input("Enter calorie intake goal for Wednesday: "))
    calorie_intake_w = int(input("Enter calorie intake for Wednesday: "))
    if calorie_goal_w == calorie_intake_w:
        print("Nice!" * 3)
        print("you have met your goal for today!")
    elif calorie_goal_w > calorie_intake_w:
        print("Intake more calories by:", calorie_goal_w - calorie_intake_w, "")
    elif calorie_goal_w < calorie_intake_w:
        print("Intake less calories by:", calorie_intake_w - calorie_goal_w, "")
    # For Thursday
    calorie_goal_th = int(input("Enter calorie intake goal for Thursday: "))
    calorie_intake_th = int(input("Enter calorie intake for Thursday: "))
    if calorie_goal_th == calorie_intake_th:
        print("Nice!" * 3)
        print("you have met your goal for today!")
    elif calorie_goal_th > calorie_intake_th:
        print("Intake more calories by:", calorie_goal_th - calorie_intake_th, "")
    elif calorie_goal_th < calorie_intake_th:
        print("Intake less calories by:", calorie_intake_th - calorie_goal_th, "")
    # For Friday
    calorie_goal_f = int(input("Enter calorie intake goal for Friday: "))
    calorie_intake_f = int(input("Enter calorie intake for Friday: "))
    if calorie_goal_f == calorie_intake_f:
        print("Nice!" * 3)
        print("you have met your goal for today!")
    elif calorie_goal_f > calorie_intake_f:
        print("Intake more calories by:", calorie_goal_f - calorie_intake_f, "")
    elif calorie_goal_f < calorie_intake_f:
        print("Intake less calories by:", calorie_intake_f - calorie_goal_f, "")
    # For Saturday
    calorie_goal_s = int(input("Enter calorie intake goal for Saturday: "))
    calorie_intake_s = int(input("Enter calorie intake for Saturday: "))
    if calorie_goal_s == calorie_intake_s:
        print("Nice!" * 3)
        print("you have met your goal for today!")
    elif calorie_goal_s > calorie_intake_s:
        print("Intake more calories by:", calorie_goal_s - calorie_intake_s, "")
    elif calorie_goal_s < calorie_intake_s:
        print("Intake less calories by:", calorie_intake_s - calorie_goal_s, "")
    # For Sunday
    calorie_goal_su = int(input("Enter calorie intake goal for Sunday: "))
    calorie_intake_su = int(input("Enter calorie intake for Sunday: "))
    if calorie_goal_su == calorie_intake_su:
        print("Nice!" * 3)
        print("you have met your goal for today!")
    elif calorie_goal_su > calorie_intake_su:
        print("Intake more calories by:", calorie_goal_su - calorie_intake_su, "")
    elif calorie_goal_su < calorie_intake_su:
        print("Intake less calories by:", calorie_intake_su - calorie_goal_su, "")


# This is the main function
# It's purpose is for the user to be able to choose their option
def main():
    print("Which option would you like to see? ")
    print("BMI Calculator")
    print("Body Fat Percentage Calculator")
    print("Calorie Tracker")
    user_input = str(input("Enter option here: "))
    # Chooses BMI calculator
    if user_input == "BMI Calculator":
        height_in = int(input("Please enter your height in inches: "))
        weight_lbs = int(input("Please enter your weight in pounds: "))
        bmi_calculator(height_in, weight_lbs)
        # Chooses body fat percentage calculator
    elif user_input == "Body Fat Percentage Calculator":
        gender = str(input("Enter gender here. (Women or Man): "))
        bmi_2 = float(input("Enter your BMI here: "))
        age = int(input("Enter your age here: "))
        if gender == "Man":
            body_fat_percentage_calculator(bmi_2, age, gender)
        elif gender == "Women":
            body_fat_percentage_calculator(bmi_2, age, gender)
            # Chooses calorie tracker
    elif user_input == "Calorie Tracker":
        calorie_tracker()
        # This checks the user's inputs as they choose their option in the menu
        # If their option is wrong it tells them and makes them choose again
    else:
        print("This is not a valid input. Please enter a valid option.")
        main()


main()
