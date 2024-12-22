def maximize_remaining_charge(charges):
    """
    Maximizes the remaining system charge while combining adjacent charges when
    removing elements from the middle of the list.

    Args:
    charges (list): List of integers representing charges.

    Returns:
    int: The maximum possible charge of the remaining system.
    """
    print(f"Initial charges: {charges}")
    
    while len(charges) > 1:
        # Find the index of the smallest charge to remove
        min_index = charges.index(min(charges))
        removed_charge = charges[min_index]

        # Handle adjacent combination for middle elements
        if 0 < min_index < len(charges) - 1:
            charges[min_index - 1] += charges[min_index + 1]  # Combine left and right neighbors
            charges.pop(min_index + 1)  # Remove the right neighbor
            charges.pop(min_index)  # Remove the current charge
        else:
            # Remove the first or last charge directly
            charges.pop(min_index)
        
        print(f"Removed charge at index {min_index} (charge: {removed_charge})")
        print(f"New state of charges: {charges}")
    
    print(f"Final charge: {charges[0]}")
    return charges[0]

# # Example usage
# charges = [-3, 1, 4, -1, 5, -9]
# maximize_remaining_charge(charges)

charges = [-2, 4, 3, -2, 1]
maximize_remaining_charge(charges)