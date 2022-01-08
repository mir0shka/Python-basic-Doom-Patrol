while True:
    num1 = int(input('Write first number: '))
    print('+ ' + '- ')
    menu_flag = input("Type your choose: ")
    num2 = int(input('Write second number: '))
    if menu_flag == '+':
        result = num1 + num2
        with open('result.txt', 'w') as file:
            file.write(f'{num1} + {num2} = {result}')

    elif menu_flag == '-':
        result = num1 - num2
        with open('result.txt', 'a') as file:
            file.write(f'\n{num1} - {num2} = {result}')