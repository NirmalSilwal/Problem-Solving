# Write a program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the 
# number and for the multiples of five print "Buzz". For numbers which are multiples of both three 
# and five print "FizzBuzz".

testcases = int(input())
if 1 <= testcases <= 10:
    lst = list(map (int, input().split()))
    
    for N in lst:
        for displayCount in range(1,N+1):
            if displayCount % 3 == 0 and displayCount % 5 == 0:
                print('FizzBuzz')
            elif displayCount % 3 == 0:
                print('Fizz')
            elif displayCount % 5 == 0:
                print('Buzz')
            else:
                print(displayCount) 
