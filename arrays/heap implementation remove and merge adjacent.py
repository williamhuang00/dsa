import heapq

def maximize_remaining_charge(charges):
    """
    Maximizes the remaining system charge using a heap-based approach.
    
    Args:
    charges (list): List of integers representing charges.
    
    Returns:
    int: The maximum possible charge of the remaining system.
    """
    print(f"Initial charges: {charges}")
    
    # Min-heap for charges (value, index)
    heap = [(charge, i) for i, charge in enumerate(charges)]
    heapq.heapify(heap)
    
    # Active indices (to check if an element is valid for removal)
    active = set(range(len(charges)))
    
    while len(active) > 1:
        # Remove the smallest charge that's still active
        while True:
            min_charge, min_index = heapq.heappop(heap)
            if min_index in active:
                break
        
        # Remove this element from active set
        active.remove(min_index)
        print(f"Removed charge at index {min_index} (charge: {min_charge})")
        
        # Handle adjacent combination if possible
        left, right = min_index - 1, min_index + 1
        if left in active and right in active:
            # Combine left and right neighbors
            combined_charge = charges[left] + charges[right]
            charges[left] = combined_charge  # Update left charge
            active.remove(right)  # Remove right index from active
            heapq.heappush(heap, (combined_charge, left))  # Push new combined charge
            print(f"Combined charges at indices {left} and {right} into {combined_charge}")
        elif left in active:
            # Only left neighbor exists; nothing to combine
            heapq.heappush(heap, (charges[left], left))
        elif right in active:
            # Only right neighbor exists; nothing to combine
            heapq.heappush(heap, (charges[right], right))
        
        print(f"New state of charges: {[charges[i] for i in active]}")
    
    # Get the final remaining charge
    final_index = next(iter(active))
    final_charge = charges[final_index]
    print(f"Final charge: {final_charge}")
    return final_charge

# Example usage
charges = [-2, 4, 3, -2, 1]
maximize_remaining_charge(charges)
