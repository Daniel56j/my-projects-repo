while True:
        try:
            num1 = float(input('Enter the first number: '))
            num2 = float(input('Enter the second number: '))

            while True:
                 op = input('Select operation (+, -, /, *, //, **): ')
                 if op == '+':
                    print("Result: ",round(num1 + num2, 2))
                    break

                 elif op == '-':
                    print("Result: ", round(num1 - num2, 2))
                    break

                 elif op == '/':
                    print("Result: ", round(num1 / num2, 2))
                    break

                 elif op == '*':
                    print("Result: ", round(num1 * num2, 2))
                    break

                 elif op == '//':
                    print('Result: ', round(num1 // num2, 2))
                    break

                 elif op == '**':
                    print('Result: ', round(num1 ** num2, 2))
                    break

                 else:
                    print("Invalid operation, please select from the suggested options!")

        except ValueError:
            print('Error: enter numbers!')
            continue
        except ZeroDivisionError:
            print('Error: division by zero is not allowed!')
            continue

        while True:
           again = input('Do you want to calculate something else? (y/n): ').lower()

           if again == 'y' or again == 'д':
            exit_program = False
            break
           elif again ==  'n' or again == 'н':
              exit_program = True
              break
           else:
            print("Please select y/n")
        if exit_program == True:
            break

