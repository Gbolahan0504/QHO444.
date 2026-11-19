# Week 5 - Tuple

# Activity 1: Simple Tuplu

def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    #Send back the smallest chance
    return min(likelihoods)



def run_tasks1():
    # Store the smallest chance in a local variable
    value =likelihood()
    print(f"Minimum likelihood of falling: {value}%")


# Only run when this file is executed directly
if __name__ == "__main__":
    run_tasks1()

