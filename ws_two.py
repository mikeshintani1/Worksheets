# 1.	Happy Numbers
# a.	https://en.wikipedia.org/wiki/Happy_number
# 
# b.	A happy number is a number defined by the following process:
# starting with any positive integer

# from operator import truediv

# # Mikes Notes function performs the squaring of individual integers and then multiplying them together
# def numSquareSum(n):
#     squareSum = 0;
#     while(n):
#         squareSum += (n % 10) * (n % 10);
#         n = int(n / 10);
#     return squareSum;
 
# # method return true if
# # n is Happy number to be cycled in loop
# def isHappynumber(n):
 
#     # initialize slow
#     # and fast by n
#     slow = n;
#     fast = n;
#     # This loop will check slow vs fast using the numSquareSum function initially created
#     while(True):
         
#         # Mikes Notes: numSquareSum(slow) is going to check the first number input by the user and verify if it meets the criteria of equaling 1 after square + adding numbers back together.
#         slow = numSquareSum(slow);
 
#         # Mikes Notes: numSquareSum(numSquareSum(fast)) is going to check values that are further down the chain of splitting the integer, squaring the numbers, then adding them.
#         fast = numSquareSum(numSquareSum(fast));
#         if(slow != fast):
#             continue;
#         else:
            # break; 
 
#     # if both number meet at 1, then return true as the number is "happy"
#     return (slow == 1);
 
# # # Happy code result
# n = int(input('select a number: '));
# if (isHappynumber(n)):
#     print(n , "is a Happy number");
# else:
#     print(n , "is not a Happy number");


# 2.	Prime Numbers
# a.	A prime number is a number that is only divisible by one and itself.
# b.	Write a method that prints out all prime numbers between 1 and 100 

# n = int(input('input a number: '))

def prime(x, y):
    prime_list = []
    for a in range(x, y):
        if a == 0 or a ==1:
            continue
        else:
            for b in range(2, int(a/2) + 1):
                if a % b == 0:
                    break
            else:
                prime_list.append(a)
    return prime_list

first_no = 1
end_no = 100
lst = prime(first_no, end_no)
if len(lst) == 0:
    print('No prime numbers')
else:
    print('Prime numbers are: ', lst)


# 3.	Fibonacci
# a.	A series of numbers in which each number (Fibonacci number) is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.
# b.	Write a method that does the Fibonacci sequence starting at 1
# c.	HARDER VERSION: Write a method that does the Fibonacci sequence starting at a number that a user inputs


def recursion_fibo(n):
    # number must be greater than 1 in order for fib to work
   if n <= 1:
       return n
   else:
       return(recursion_fibo(n-1) + recursion_fibo(n-2))
    #    if n=3 (3-1) + (3-2) -> 2+1=3 -> this will place 

#user inputs how many times(range) the function will re-occur(loop).
nterms = int(input('select a number: '))

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
    #    i = 0,1,2,3... and will move through the range, loop through recursion_fibo(n) until the limit established by nterms is reached.
       print(recursion_fibo(i))