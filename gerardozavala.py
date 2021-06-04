def generate_odd_nums(start, end):
    for num in range(start, end+1):

        if num % 2 !=0:
            print(num, end=" ")



generate_odd_nums(start = 0, end = 15)

