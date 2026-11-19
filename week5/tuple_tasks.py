# Week 5 - Tuple

# Activity 1: Simple Tuple

def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    #Send back the smallest chance
    return min(likelihoods)



def run_task1():
    # Store the smallest chance in a local variable
    value =likelihood()
    print(f"Minimum likelihood of falling: {value}%")





# Activity 2: Tuple Return Type

def likelihood_min_max():
    # Chance (in %) that each step will fall
    likelihoods = (50, 38, 27, 99, 4)
    # Send back the smallest and largest chance together as a tuple
    return (min(likelihoods), max(likelihoods))


def run_task2():
    # Store the returned tuple in a local variable
    values = likelihood_min_max()
    print(f"Minimum likelihood of falling: {values[0]}%")
    print(f"Maximum likelihood of falling: {values[1]}%")


# Only run when this file is executed directly
if __name__ == "__main__":
    run_task2()




