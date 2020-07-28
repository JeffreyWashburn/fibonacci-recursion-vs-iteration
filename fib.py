# the algorithm:

# input is a range of integers:
# [0, 1, 2, 3, 4, 5, 6]

# build a new list:
# [0] if 0, just return 0     
# [0, 1] if 1, just return 1
# [0, 1, 1] else, add cur_idx to cur_idx - 1 and cur_idx - 2
# [0, 1, 1, 2] rinse and repeat

# using a for loop to do this is much faster
def fib(rng):
    new = []
    for idx in rng:
        if idx == 0 or idx == 1:
            new.append(idx)
        else:
            val = new[idx - 1] + new[idx - 2]
            new.append(val)
    return new

# recursion does look a little more pretty though
def fib_recursive(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

# uncomment and run the non recursive function first
#print(fib(range(100)))

# to see the difference, uncomment and run the recursive version
#print([fib(n) for n in range(100)])