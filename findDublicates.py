# Define a function to find duplicates in a list of outcomes
def find_duplicates(outcomes):
    # Create an empty set to track already seen outcomes
    seen = set()
    # Create an empty list to store the duplicate outcomes
    duplicates = []

    # Loop through each outcome in the list
    for outcome in outcomes:
        # If the outcome has already been seen, it's a duplicate
        if outcome in seen:
            # Add the duplicate outcome to the duplicates list
            duplicates.append(outcome)
        else:
            # If it's the first time the outcome is seen, add it to the set
            seen.add(outcome)

    # Return the list of duplicates found
    return duplicates

# List of outcomes to check for duplicates
outcomes = [123456, 234567, 123347, 456789, 567890, 678901, 789012, 890123, 
            901234, 112233, 223344, 334455, 789012, 222234, 123347]

# Call the function to find duplicates in the outcomes list
duplicates = find_duplicates(outcomes)

# Print the duplicates found in the list
print("Duplicates:", duplicates)