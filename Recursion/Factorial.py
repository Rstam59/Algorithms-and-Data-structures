def iterative_factorial(number):
    f = 1
    for i in range(1, number+1):
        f = f * i
    return f

print(iterative_factorial(0))
#1
print(iterative_factorial(5))
#120
print(iterative_factorial(50))
#30414093201713378043612608166064768844377641568960512000000000000

def recursive_factorial(number):
    if number <= 1:
        return 1
    else:
        return number * recursive_factorial(number-1)

print(recursive_factorial(0))
#1
print(recursive_factorial(5))
#120
print(recursive_factorial(50))
#30414093201713378043612608166064768844377641568960512000000000000
print(recursive_factorial(1000))
