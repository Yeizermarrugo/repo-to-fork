
def fibonacci(n_terms):
    n1, n2 = 0, 1
    count = 0
    if n_terms == 1:
        print(n1)
    else:
        while count < n_terms:
            print(n1)
            nth = n1 + n2
            # Update
            n1 = n2
            n2 = nth
            count += 1

fibonacci(15)