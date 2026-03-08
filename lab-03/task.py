#task 1
# check = (lambda num: "Положительное" if num > 0 else "Отрицательно" if num < 0 else "Ноль")

# print(check(5))
# print(check(-3))
# print(check(0))

#task 2
# words =["арбуз", "кот", "машина", "дом", "ананас"]

# print(sorted(words, key=lambda w: (len(w), w[0])))

#task 3
# num = [5, 12, 7, 20, 33, 8]

# print(list(filter(lambda n: n % 2 == 0 and n > 10, num)))

#task 4
# numbers = [1, 2, 3, 4, 5, 6]

# print(list(map( lambda n: n ** 2 if n % 2 == 0 else n * 3, numbers)))

#task 5

# compare = lambda a,b: "a больше" if a > b else "b больше" if b > a else "равны"

# print(compare(10, 7))
# print(compare(3, 5))
# print(compare(4, 4))

#task 6

# numbers = [0, -3, 5, -7, 8]

# new_lst = [(lambda n: "положительно" if n > 0 else "отрицательно" if n < 0 else "ноль")(n) for n in numbers]

# print(new_lst)

###       Генераторы
#task 1
# def even_numbers(n):
#     return ("кратно 4" if x % 4 == 0 else x for x in range(2, n+1, 2))

# for x in even_numbers(10):
#     print(x)

#task 2
# words = ["кот", "машина", "арбуз", "дом"]

# filter_words = ("с а" if len(w) > 4 else w for w in words if "а" in w)

# for w in filter_words:
#     print(w)

#task 3
# def infinite_numbers():
#     n = 1
#     while True:
#         if n % 3 == 0 and n % 5 == 0:
#             yield "FizzBuzz"
#         elif n % 3 == 0:
#             yield "Fizz"
#         elif n % 3 == 0:
#             yield "Buzz"
#         else:
#             yield n
#         n += 1

# gen = infinite_numbers()

# for g in range(15):
#     print(next(gen))

#task 4
# n = 5
# gen = ("четний квадрат" if i **2 % 2 == 0 else i ** 2 for i in range(1, n+1))

# for x in gen:
#     print(x)




###  3 - Итераторы и comprehension
#task 1 
# lst = [n**2 for n in range(20) if n % 2 == 0]
# print(lst)

#task 2
# matrix = [[1, 2, 3], [4,5,6], [7,8,9]]
# lst = [(lambda i: i[0]*i[1]*i[2])(i) for i in matrix]

# print(lst)

#task 3
# words = ["кот", "машина", "ананас", "дом", "телефон"]
# lst = [w for w in words if "а" not in w and len(w) > 4]
# print(lst)

#task 4
# numbers = [1, 2, 3, 4, 5]

# d = {n: "четное" if n % 2 == 0 else "нечетное" for n in numbers}

# print(d)

#task 5
# matrix = [[1,2], [3,4], [5,6]]

# lst = [x for row in matrix for x in row]

# print(lst)

#task 6
# lst = [
#     "FizzBuzz" if n % 3 == 0 and n % 5 == 0
#     else "Fizz" if n % 3 == 0
#     else "Buzz" if n % 5 == 0
#     else n
#     for n in range(1,21)
# ]

# print(lst)

### Смешанные сложные задачи (5 штук)
#task 1

# def is_prime(x):
#     if x <= 1:
#         return False
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             return False
#     return True


# def special_numbers(n):
#     for n in range(1, n+1):
#         if n % 3 == 0 and n % 5 == 0:
#             yield "FizzBuzz"
#         elif n % 3 == 0:
#             yield "Fizz"
#         elif n % 5 == 0:
#             yield "Buzz"
#         elif is_prime(n):
#             yield "простое"
            
#         else:
#             yield n

    



# for x in special_numbers(15):
#     print(x)

#task 2
# words = ["кот", "машина", "арбуз", "дом", "ананас"]

# process_word = lambda w: (w.upper() + "*" if "а" in w else w.upper()) if len(w) > 4 else  ("short*" if "a" in w else "short") 

# lst = [process_word(w) for w in words]

# print(lst)

#task 3
# def process_numbers(n):
#     filtered = filter(lambda x: x >= 0, numbers)

#     mapped = map(lambda x: x/2 if x%2 == 0 else x*3 + 1, filtered)

#     for num in mapped:
#         yield num

# numbers = [5, -2, 8, 0, -7, 3]

# for x in process_numbers(numbers):
#     print(x)

#task 4
# students = [("Иван", 85), ("Анна", 72), ("Пётр", 90), ("Мария", 60)]

# grade = lambda score: (
#     "Отлично" if score >= 90
#     else "Хорошо" if score >= 70
#     else "Удовлетворительно"
# )

# result = {name: grade(score) for name, score in students}

# print(result)

#task 5
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# def matrix_transform(matrix):
#     gen = (
#         "Кратно 6" if x % 6 == 0
#         else "четное" if x % 2 == 0
#         else "Кратно 3" if x % 3 == 0
#         else x
#         for row in matrix
#         for x in row
#     )

#     for item in gen:
#         yield item

# for x in matrix_transform(matrix):
#     print(x)




### Задачи для понимания map and filter
#task 1
# numbers = [1, 2, 3, 4, 5]
# doubled = list(map(lambda x: x * 2, numbers))
# print(doubled)

#task 2
# words = ["кот", "машина", "арбуз", "дом"]

# result = list(map(lambda w: w.upper() + "!" if len(w) > 3 else w.upper(), words))
# print(result)

#task 3
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# evens = list(filter(lambda x: x % 2 == 0, numbers))

# print(evens)

#task 4
# numbers = [0, 5, 12, 7, 20, -3, 8]

# result = list(
#     map(lambda x: x /2 if x % 2 == 0 else x * 3,
#     filter(lambda x: x> 5, numbers))
# )

# print(result)
