# Avery King

# asks the user how manmy passowrd to audit and 
# keep asking until they give a valid postive whole number
def get_password_count():
    """Prompt until the user enters a positive whole number; return that number."""
    while True:
        try:
            #  response stores the user input
            response = input("please enter the amount of passsword being audited. ")
            # try converting it to an integer,
            number = int(response)
            # only accept only numbers greater than zero
            if number > 0:
                return number
            else:
                print("Please enter a whole number great than zero.")

        # runs if int(response) fails
        except ValueError:
            print("Please enter a valid number greater than zero")

# look at password and de c ied if its Strong, Moderate, or Weak.
def evaluate_password(password):
    # local variables to track which character types show up in the password
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False


    # check every character in the password one at a time
    for character in password:
        if character.isupper():
            has_uppercase = True
        elif character.islower():
            has_lowercase = True
        elif character.isdigit():
            has_digit = True
        else:
            has_special = True

    # count how many of the four character tyypes were found.
    type_total = sum([has_uppercase, has_lowercase, has_digit, has_special])
    # apply the rating rules
    if len(password) >= 12 and type_total == 4:
        return "Strong"
    elif len(password) >= 8 and type_total >= 3:
        return "Moderate"
    else:
        return "Weak"
  

# print the final counts of Strong/Moderate/Weak passwords.
def display_summary(strong_count, moderate_count, weak_count):
    """Display the totals for each password-rating category."""
    print("Password Audit Summary")
    print("Strong passwords:    ", strong_count)
    print("Moderate password:   ", moderate_count)
    print("Weak passwords:      ", weak_count)
   


def main():
    # local counters, one for each rating
    strong_count = 0
    moderate_count = 0
    weak_count = 0

    # ask for how many passwords the user wants to check
    password_count = get_password_count()

    # loop once per password the user entered
    for password_number in range(1, password_count + 1):
        password = input(f"Password {password_number}: ")
        rating = evaluate_password(password)
        print("Rating: ", rating)

        #update the matching counter based on the rating returned
        if rating == "Strong":
            strong_count += 1
        elif rating == "Moderate":
            moderate_count += 1
        else:
            weak_count += 1

     # display the final summary after all password have been checked       
    display_summary(strong_count, moderate_count, weak_count)


if __name__ == "__main__":
    main()
