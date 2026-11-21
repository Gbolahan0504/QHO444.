# Main program: a menu to run every program from weeks 1 to 5

import week1.output_tasks as wk1_output
import week1.input_tasks as wk1_input
import week2.if_statements as wk2_if
import week2.nested_if as wk2_nested
import week2.multiple_nested as wk2_multi_nested
import week2.multiple_conditions as wk2_conditions
import week2.review as wk2_review
import week3.while_loops as wk3_while
import week3.for_loops as wk3_for
import week3.nested_loops as wk3_nested
import week4.built_in_functions as wk4_built_in
import week4.custom_functions as wk4_custom
import week4.module_tasks as wk4_modules
import week5.list_tasks as wk5_lists
import week5.tuple_tasks as wk5_tuples


def run_week_one():
    print("Which program in 'Week 1' do you wish to run?")
    print("1) Box")
    print("2) Escape message")
    print("3) Robot")
    print("4) Greeting")
    print("5) Robot eyes")
    print("6) BMI calculator")
    print("7) Health bars")
    response = input()
    print()
    # Call the function that matches the choice
    if response == "1":
        wk1_output.display_box()
    elif response == "2":
        wk1_output.display_escape_message()
    elif response == "3":
        wk1_output.display_robot()
    elif response == "4":
        wk1_input.greet_user()
    elif response == "5":
        wk1_input.robot_eyes()
    elif response == "6":
        wk1_input.bmi_calculator()
    elif response == "7":
        wk1_input.health_bars()
    else:
        print("Invalid option!")


def run_week_two():
    print("Which program in 'Week 2' do you wish to run?")
    print("1) Adventure book")
    print("2) Perform activity")
    print("3) Robot direction")
    print("4) Even or odd")
    print("5) Smallest number")
    print("6) Count even and odd")
    print("7) Book cover")
    print("8) Find phone")
    print("9) Choose route")
    print("10) Check creature")
    print("11) Cave adventure")
    response = input()
    print()
    # Call the function that matches the choice
    if response == "1":
        wk2_if.adventure_book()
    elif response == "2":
        wk2_if.perform_activity()
    elif response == "3":
        wk2_if.robot_direction()
    elif response == "4":
        wk2_if.even_or_odd()
    elif response == "5":
        wk2_if.smallest_number()
    elif response == "6":
        wk2_if.count_even_odd()
    elif response == "7":
        wk2_nested.book_cover()
    elif response == "8":
        wk2_multi_nested.find_phone()
    elif response == "9":
        wk2_conditions.choose_route()
    elif response == "10":
        wk2_conditions.check_creature()
    elif response == "11":
        wk2_review.cave_adventure()
    else:
        print("Invalid option!")


def run_week_three():
    print("Which program in 'Week 3' do you wish to run?")
    print("1) Remove apples")
    print("2) Avoid obstacles")
    print("3) Charge battery")
    print("4) Repeating word")
    print("5) Sum 100")
    print("6) Sum user numbers")
    print("7) Mountains")
    print("8) Count down")
    print("9) Brightness")
    print("10) Characters")
    print("11) Reverse phrase")
    print("12) Print letters")
    print("13) Emoji grid")
    print("14) Marker distance")
    response = input()
    print()
    # Call the function that matches the choice
    if response == "1":
        wk3_while.remove_apples()
    elif response == "2":
        wk3_while.avoid_obstacles()
    elif response == "3":
        wk3_while.charge_battery()
    elif response == "4":
        wk3_while.repeating_word()
    elif response == "5":
        wk3_while.sum_100()
    elif response == "6":
        wk3_while.sum_user_numbers()
    elif response == "7":
        wk3_for.display_mountains()
    elif response == "8":
        wk3_for.count_down()
    elif response == "9":
        wk3_for.adjust_brightness()
    elif response == "10":
        wk3_for.show_characters()
    elif response == "11":
        wk3_for.reverse_phrase()
    elif response == "12":
        wk3_for.print_letters()
    elif response == "13":
        wk3_nested.emoji_grid()
    elif response == "14":
        wk3_nested.marker_distance()
    else:
        print("Invalid option!")


def run_week_four():
    print("Which program in 'Week 4' do you wish to run?")
    print("1) ASCII value")
    print("2) ASCII character")
    print("3) Listen")
    print("4) Identify")
    print("5) Escape plans")
    print("6) Cross bridge")
    print("7) Climb ladder")
    print("8) Create ladder")
    print("9) Weights")
    print("10) Word manipulation")
    print("11) Guess the number")
    response = input()
    print()
    # Call the function that matches the choice
    if response == "1":
        wk4_built_in.ascii_value()
    elif response == "2":
        wk4_built_in.ascii_character()
    elif response == "3":
        wk4_custom.listen()
    elif response == "4":
        wk4_custom.identify()
    elif response == "5":
        # This function needs a plan passed in, so try all three
        wk4_custom.escape_by("jumping over")
        wk4_custom.escape_by("running around")
        wk4_custom.escape_by("cross bridge ahead")
    elif response == "6":
        wk4_custom.cross_bridge(3)
        wk4_custom.cross_bridge(6)
    elif response == "7":
        wk4_custom.climb_ladder(5, 2)
        wk4_custom.climb_ladder(2, 5)
    elif response == "8":
        wk4_custom.create_ladder()
    elif response == "9":
        wk4_custom.run()
    elif response == "10":
        wk4_custom.run_word_program()
    elif response == "11":
        wk4_modules.play_guess_the_number()
    else:
        print("Invalid option!")



def run_week_five():
    print("Which program in 'Week 5' do you wish to run?")
    print("1) Simple list")
    print("2) Indexing")
    print("3) Iterate")
    print("4) Populate")
    print("5) Simple tuple")
    print("6) Tuple return type")
    print("7) Nested tuples")
    response = input()
    print()
    # Call the function that matches the choice
    if response == "1":
        wk5_lists.run_task1()
    elif response == "2":
        wk5_lists.run_task2()
    elif response == "3":
        wk5_lists.run_task3()
    elif response == "4":
        wk5_lists.run_task4()
    elif response == "5":
        wk5_tuples.run_task1()
    elif response == "6":
        wk5_tuples.run_task2()
    elif response == "7":
        wk5_tuples.run_task3()
    else:
        print("Invalid option!")


def run():
    # Keep showing the menu until the user chooses to quit
    while True:
        print()
        print("What would you like to do?")
        print("[1] Run 'week 1' programs")
        print("[2] Run 'week 2' programs")
        print("[3] Run 'week 3' programs")
        print("[4] Run 'week 4' programs")
        print("[5] Run 'week 5' programs")
        print("[q] Quit")
        response = input()
        print()

        # Open the menu for the week chosen
        if response == "1":
            run_week_one()
        elif response == "2":
            run_week_two()
        elif response == "3":
            run_week_three()
        elif response == "4":
            run_week_four()
        elif response == "5":
            run_week_five()
        elif response == "q":
            # break stops the while loop, which ends the program
            break
        else:
            print("Invalid option! Please try again.")


# Start the main menu
run()