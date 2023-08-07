def main(l1,l2):
    # Create an empty list to store the merged elements.
    merged_list = []
    i = 0 # Pointer for tracking the current position in l1.
    # Pointer for tracking the current position in l2.
    j = 0
    # Loop through both lists until one is fully completed.
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            # If the element in l1 is smaller, add it to merged_list and move the pointer i to the next element in l1.
            merged_list.append(l1[i])
            i+=1
        else:
            # If the element in l2 is smaller (or equal), add it to merged_list and move the pointer j to the next element in l2.
            merged_list.append(l2[j])
            j+=1

     # If there are any remaining elements in l1, add them to merged_list.
    while i < len(l1):
            merged_list.append(l1[i])
            i+=1

    # If there are any remaining elements in l2, add them to merged_list.
    while j < len(l2):
            merged_list.append(l2[j])
            j+=1
    return merged_list # Return the final merged and sorted list.

# Call the main function to merge the arrays and store the merged result in merged_result.

l1 = [1, 3, 5, 7, 9]
l2 = [2, 4, 6, 8, 10]
merged_result = main(l1, l2)
print(merged_result)