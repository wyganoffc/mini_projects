import sys

def add(a: float, b: float = 0) -> (int, float):
    return a + b

def subtract(a: float, b: float = 0) -> (int, float):
    return a - b

def multiply(a: float, b: float = 0) -> (int, float):
    return a * b

def divide(a: float, b: float = 1) -> (float, str):
    try:
        return a / b
    except ZeroDivisionError as e:
        return f"{e}: нельзя делить на 0"

def power(a: float, b: float = 0) -> (int, float):
    return a ** b

def inputer():
    a = input("первое число:")
    o = input("операция:")
    b = input("второе число:")
    return [a, o, b]

def main():
    history = set()
    while True:
        print("""=== УМНЫЙ КАЛЬКУЛЯТОР ===
            1. Выполнить вычисление
            2. Показать историю
            3. Очистить историю
            4. Выход""")
        d = input("выбирете действие:")
        if d == "1":
            data = inputer()

            try:
                if data[1] == "+":
                    n = add(float(data[0]), float(data[2]))
                    res = f"{data[0]} {data[1]} {data[2]} = {n}"
                    print(res)
                elif data[1] == "-":
                    n = subtract(float(data[0]), float(data[2]))
                    res = f"{data[0]} {data[1]} {data[2]} = {n}"
                    print(res)
                elif data[1] == "*":
                    n = multiply(float(data[0]), float(data[2]))
                    res = f"{data[0]} {data[1]} {data[2]} = {n}"
                    print(res)
                elif data[1] == "/":
                    n = divide(float(data[0]), float(data[2]))
                    res = f"{data[0]} {data[1]} {data[2]} = {n}"
                    print(res)
                elif data[1] == "**":
                    n = power(float(data[0]), float(data[2]))
                    res = f"{data[0]} {data[1]} {data[2]} = {n}"
                    print(res)
                else:
                    print("некоректно введена операция")
                history.add(res)
            except ValueError:
                print("нужно ввести число!")
            except ZeroDivisionError:
                print("на 0 делить нельзя!")
            except FileNotFoundError:
                print("файл не найден!")
            except KeyboardInterrupt:
                print("досвидания!")
                sys.exit(0)

        elif d == "2":
            print(history)

        elif d == "3":
            history.clear()
            print("история очищена!")

        elif d == "4":
            break
            sys.exit(0)

        else:
            print("неверно введена команда!")

if __name__ == "__main__":
    main()