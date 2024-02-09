num1 = 0
num2 = 0

for x in range(5):
    num1 = x
    for y in range(14):
        num2 = y + 3

print(num1 + num2)

x = 1
sum = 5
while x <= 10:
    sum += x
    x += 1
print(sum)
# Should print 55


number = 1 # Initialize the variable
while number<8: # Complete the while loop condition
    print(number, end=" ")
    number +=1 # Increment the variable

# Should print 1 2 3 4 5 6 7

def even_numbers(n):
    count = 0
    current_number = 0
    while current_number<n+1: # Complete the while loop condition
        if current_number % 2 == 0:
            count+=1 # Increment the appropriate variable
        current_number+=1 # Increment the appropriate variable
    return count

print(even_numbers(25))   # Should print 13
print(even_numbers(144))  # Should print 73
print(even_numbers(1000)) # Should print 501
print(even_numbers(0))    # Should print 1



def multiplication_table(start, stop):
    # Complete the outer loop range
    for x in range(start,stop+1):
        # Complete the inner loop range
        for y in range(start,stop+1):
            # Prints the value of "x" multiplied by "y"
            # and inserts a space after each value
            print(str(x*y), end=" ")
        # An empty print() function inserts a line break at the
        # end of the row
        print()


multiplication_table(1, 3)
# Should print the multiplication table shown above


def divisible(max, divisor):
    count=0 # Initialize an incremental variable
    x=1
    for x in range(max): # Complete the for loop
        if x % divisor == 0:
            count+=1 # Increment the appropriate variable
    x+=1
    return count

print(divisible(100, 10)) # Should be 10
print(divisible(10, 3)) # Should be 4
print(divisible(144, 17)) # Should be 9

def all_numbers(minimum, maximum):

    return_string = "" # Initializes variable as a string

    # Complete the for loop with a range that includes all
    # numbers up to and including the "maximum" value.
    x = minimum
    for x in range(minimum,maximum +1,1):

        return_string= return_string + " "+str(x)
        # Complete the body of the loop by appending the number
        # followed by a space to the "return_string" variable.


    # This .strip command will remove the final " " space
    # at the end of the "return_string".
    return return_string.strip()


print(all_numbers(2,6))  # Should be 2 3 4 5 6
print(all_numbers(3,10)) # Should be 3 4 5 6 7 8 9 10
print(all_numbers(-1,1)) # Should be -1 0 1
print(all_numbers(0,5))  # Should be 0 1 2 3 4 5
print(all_numbers(0,0))  # Should be 0

