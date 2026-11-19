# Week 5 - Tuple

# Activity 1: Simple Tuple

def likelihood():
    # Chance (in %) that each step will fall
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


# Activity 3: Nested Tuples

def steps():
    # A list of tuples: each tuple holds a step name and its chance of falling
    likelihoods = [
        ("step 1", 50),
        ("step 2", 38),
        ("step 3", 27),
        ("step 4", 99),
        ("step 5", 4),
    ]
    return likelihoods


def run_task3():
    # Store the returned list in a local variable
    all_steps = steps()
    # Empty lists to sort the steps into
    good_steps = []
    bad_steps = []
    # Check each step's chance of falling
    for step in all_steps:
        if step[1] >= 50:
            bad_steps.append(step)
        else:
            good_steps.append(step)
    print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")




# Only run when this file is executed directly
if __name__ == "__main__":
    run_task3()




