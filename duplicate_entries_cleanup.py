# 2 Duplicate Entries Cleanup 
# You are given a list of customer IDs, some of which are duplicated. 
# Write a Python script to remove duplicates and display the unique customer IDs.

def cleanup_list(l):
    '''This function takes a list and removes all duplicates. It sorts the new list, prints it out, tells the user 
    how many customer IDs were removed, plus the new count, and returns the new list.'''
    try:
        # Check that the input is a list.
        if not isinstance(l, list):
            raise ValueError()
        else:
            # Converts the list to a set (removing duplicates), back to a list and sorts it.
            clean_list = sorted(list(set(l)))
    except ValueError:
        print("Please input a valid list.\n")
    else:
        # Calculates the counts
        original_count = len(l)
        new_count = len(clean_list)
        # Reports the counts
        print(f"\n{original_count-new_count} customer IDs have been removed from the original list. \nThere are now {new_count} customer IDs in the list.\n")
        # Prints the clean list in user-friendly way
        print("Here's the list of unique customer IDs:")
        print(", ".join(clean_list))
        # Returns the clean list
        return clean_list

def main():
    '''This function creates the list of customer IDs and calls the function to clean it up.'''
    import random
    try:
        # Prompts user to give how long the list should be
        x = int(input("How many customer IDs are in the list?\n"))
        # Raise error if x is not a positive number
        if x<1:
            raise ValueError()
        gen_nums = [random.randint(0, 1000) for a in range(x)] # Generate  list of random numbers (between 1 and 3 digits)
        # Generate list of custom IDs that follow a pattern "C" and the number (where the number is always 3 digits, filled in with zeros)
        custom_ids = []
        for n in gen_nums:
            zeros = "0"*(3-len(str(n)))
            custom_ids.append("C"+zeros+str(n))
        cleanup_list(custom_ids) # Clean up the list
    # Catches if the user inputs something other than an integer.
    except ValueError:
        print("Please input a whole number.")

if __name__ == "__main__":
    main()