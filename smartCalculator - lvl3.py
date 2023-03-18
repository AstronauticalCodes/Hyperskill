while True:
    user = input().split()
    if '/exit' in user:
        print('Bye!')
        exit()
    elif len(user) == 0:
        continue
    elif '/help' in user:
        print('The program calculates the sum of numbers')
    else:
        print(sum([int(x) for x in user]))
