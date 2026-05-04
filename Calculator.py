while True:
        try:
            num1 = float(input('Введите первое число: '))
            num2 = float(input('Введите второе число: '))

            while True:
                 op = input('Выберите операцию (+, -, /, *, //, **): ')
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
                    print("Неверная операция, выберите из предложенного")

        except ValueError:
            print('Ошибка: введите числа')
            continue
        except ZeroDivisionError:
            print('Ошибка: деление на ноль невозможно!')
            continue

        while True:
           again = input('Вы хотите что то еще посчитать? (y/n): ').lower()

           if again == 'y' or again == 'д':
            exit_program = False
            break
           elif again ==  'n' or again == 'н':
              exit_program = True
              break
           else:
            print("Пожайлуста выберите y/n")
        if exit_program == True:
            break

