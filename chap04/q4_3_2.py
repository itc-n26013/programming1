def func(*args):
    results =[]
    for n in args:
        results.append(n * n)
    return results

"""number=[1,2,3,4]
print(func(*number))"""

number=list(range(100))
print(func(*number))
