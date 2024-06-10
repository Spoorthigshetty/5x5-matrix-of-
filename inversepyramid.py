# Function to print a reverse pyramid
def reverse_pyramid(n):
    # Loop to handle the number of rows
    for i in range(n, 0, -1):
        # Loop to handle the number of spaces before the numbers
        for j in range(n - i):
            print(" ", end=" ")
        # Loop to handle the number of numbers in each row
        for k in range(1, i + 1):
            print(k, end=" ")
        print()  # Move to the next line after each row

# Define the height of the pyramid
height = 5
reverse_pyramid(height)
