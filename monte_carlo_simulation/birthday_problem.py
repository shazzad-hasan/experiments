import random 
import datetime 

MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def getBirthdays(num_of_birthdays):
    """ Returns a list of random birthdays. """

    birthdays = []
    for i in range(num_of_birthdays):
        start_of_year = datetime.date(2000, 1, 1)
        random_num_of_days = datetime.timedelta(random.randint(0, 364)) # assume non-leap year
        birthday = start_of_year + random_num_of_days 
        birthdays.append(birthday)

    return birthdays 

def displayBirthdays(num_of_birthdays):
    birthdays = getBirthdays(num_of_birthdays)
    for birthday in birthdays:
        month_name = MONTHS[birthday.month - 1]
        print("{} {}".format(month_name, birthday.day))

def getMatch(birthdays):
    """ Returns the date if a birthday occurs more than once in the birthdays list.  """

    # if all birthdays are unique
    if len(set(birthdays)) == len(birthdays): 
        return None 
    
    # compare each birthday to each other birthday in the brithdays list
    for i, first_birthday in enumerate(birthdays):
        for j, second_birthday in enumerate(birthdays):
            if first_birthday == second_birthday:
                return first_birthday 
            

def monteCarlo(num_of_birthdays, num_sim):
    count_match = 0
    for i in range(num_sim):
        birthdays = getBirthdays(num_of_birthdays)
        if getMatch(birthdays) != None:
            count_match += 1
    return count_match


def simulate(num_sim):
    while True:
        try:
            num_of_birthdays = int(input("How many birthdays shall I generate?"))
            break
        except:
            raise ValueError("Invalid user input! Try again.")
        
    # generate and display birthdays
    birthdays = getBirthdays(num_of_birthdays)
    print("\nHere are ", num_of_birthdays, " birthdays: ")
    displayBirthdays(num_of_birthdays)

    # determine whether there exist two birthdays that match
    # and display the results
    match = getMatch(birthdays)
    if match is None:
        print("\nThere are no matching birthdays.")
    else:
        month_name = MONTHS[match.month - 1]
        print("\nMultiple people have birthday on {} {}.".format(month_name, match.day))

    # apply monte carlo 
    print("\nGenerating", num_of_birthdays, "random birthdays 100,000 times ... ")
    sim_match = monteCarlo(num_of_birthdays, num_sim)

    # simulation result
    probability = round(100* sim_match/num_sim, 2)
    print('Out of {} simulations of {} people, '
            'there was a matching birthday in that '
            'group {} times.'.format(num_sim, num_of_birthdays, sim_match))

    print('That means {} people have a {}% chance of having a matching '
          'birthday in their group.'.format(num_of_birthdays, probability))

    
if __name__ == "__main__":
    simulate(100_000)
    


