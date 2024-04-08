def validate_bebida(input_string):
    # This function validates a beverage input string, which should be in the format:
    # [beverage_name],[quantity1],[quantity2],...,[quantityN]
    # where beverage_name is a string (1-15 characters long) and quantities are integers between 1 and 48.
    # The function returns True if the input string is valid, and False otherwise.

    # Split the input string into an array using ',' as the delimiter, and remove any leading/trailing whitespaces
    split_array = input_string.split(',')
    split_array = [elem.strip() for elem in split_array]

    # Check if the length of the split array is between 1 and 6 (inclusive)
    if not (1 <= len(split_array) <= 6):
        return False

    # Check if the first element is a string and the rest are integers
    if not (split_array[0].isalpha() and all(elem.isnumeric() for elem in split_array[1:])):
        return False

    # Check if the length of the beverage name is between 2 and 15 characters (inclusive)
    if not (2 <= len(split_array[0]) <= 15):
        return False

    # Remove the beverage name from the array and convert the remaining elements to integers
    split_array = split_array[1:]
    int_list = [int(elem) for elem in split_array]

    # Check if all quantities are between 1 and 48 (inclusive)
    if not all(1 <= num <= 48 for num in int_list):
        return False

    # Check if the quantities are unique and sorted
    if int_list!= sorted(set(int_list)):
        return False

    return True