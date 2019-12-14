def fizzbuzz():
    for num in range(1, 21):
        fizz = num % 3 == 0
        buzz = num % 5 == 0
        if fizz and buzz:
            print("fizzbuzz")
        elif fizz:
            print("fizz")
        elif buzz:
            print("buzz")
        else:
            print(num)


if __name__ == '__main__':
    fizzbuzz()
