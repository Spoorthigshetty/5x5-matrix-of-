def x_pattern(size):
    # Loop to handle the rows
    for i in range(size):
        # Loop to handle the columns
        for j in range(size):
            # Print '*' on the diagonals
            if i == j or i + j == size - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()  # Move to the next line after each row

# Define the size of the pattern (should be an odd number for proper intersection)
size = 5
x_pattern(size)
