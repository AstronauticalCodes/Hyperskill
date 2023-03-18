while True:
    user = input().split()
    if '/exit' in user:
        print('Bye!')
        exit()
    elif len(user) == 0:
        continue
    else:
        print(sum([int(x) for x in user]))
