while True:
    print("What is your name? ")
    name = input()
    while name != 'Sergei':
        print(input("Wrong name. Try again. "))
        name = input()
        if name == 'Sergei':
            break
    if name == 'Sergei':
        print("Welcome, Sergei. What is the password? ")
        password = input()
        while password != '37':
            print("Incorrect password. Try again.")
            password = input()
            if password == '37':
                break
    break
print("Access granted.")