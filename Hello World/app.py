# students_count: float = 1000
# rating: int = 4.99
# is_published = True
# course_name = "Pyth101"

# x, y = 1, 2
# x = y = 2

# print(type(rating))


# age: int = 20
# age = "Python"

# print(age)

# print(id(age))

# course = "Python Programming"
# print(len(course))
# print(course[0])
# print(course[-1])
# print(course[0-2])
# print(course[0:3])
# print(course[:3])
# print(course[0:])
# print(course[:])

# print(id(course))
# # \" show double quote
# # \' show single quote
# # \\ show back slash
# # \n new line
# message = "Python \\Programming"
# print(message)

# code_block = """
#             Python
#             Programming
#             """
# print(code_block)

# # ------------------------
# first = "jim"
# last = "Dandy"

# full = first + " " + last
# print(full)

# # or

# first = "jim"
# last = "Dandy"

# full = f"{first} {last}"
# print(full)

# # -----------------------------
# # Strings
# course = "   Python Programming"

# print(course.upper())
# print(course.lower())
# print(course.title())

# print(course.strip())

# print(course.find("pro"))
# print(course.replace("P", "-"))

# print("Programming" in course)
# print("Programming" not in course)

# -------------------------------------
# Numbers
# ---------------------------------------

# x = 10
# print(x)

# x = 0b10
# print(x)

# print(bin(x))

# x = 0x12c
# print(x)

# print(hex(x))

# # complex numbers (a + bi)
# x = 1 + 2j
# print(x)

# -----------------------------------------
# Conditional Statements
# -------------------------------------------

# age = 22

# if age >= 18:
#     print("Adult")
# elif age >= 13:
#     print("Teenager")
# else:
#     print("Child")

# print("Fine")


# # ternary operator
# message = "Eligble" if age >= 18 else "Not Eligble"

# -----------------------------------------------------
# Loops
# -----------------------------------------------------

# for x in "Python":
#     print(x)

# for x in [1, 2, 3, 4]:
#     print(x)


# for x in range(5):
#     print(x)

# for x in range(2, 5):
#     print(x)

# for x in range(0, 50, 5):
#     print(x)

# -------------------------------------------------------
# for-else
# -------------------------------------------------------

# names = ["John", "Mary"]
# for name in names:
#     if name.startswith("J"):
#         print("found")
#         found = True
#         break
# if not found:
#     print("Not Found")

# # or

# names = ["John", "Mary"]
# for name in names:
#     if name.startswith("J"):
#         print("found")
#         break
# else:
#     print("Not Found")

# ---------------------------------------------------------
# while
# ----------------------------------------------------------

# guess = 0
# answer = 5

# while answer != guess:
#     guess = int(input("Guess "))

# ----------------------------------------------------------
# Functions
# ----------------------------------------------------------


# def increment(number: int, by: int = 1) -> tuple:
#     return (number, number + by)


# print(increment(2))

# ------------------------------------------------------------
# *arqs
# ------------------------------------------------------------


# def multiply(*list):
#     total = 1
#     for number in list:
#         total *= number
#     return total


# print(multiply(2, 3, 4, 5))

# ------------------------------------------------------------
# **arqs
# ------------------------------------------------------------


# def save_user(**user):
#     print(user["name"])


# save_user(id=1, name="admin")

# ------------------------------------------------------------
# debugging
# ------------------------------------------------------------


def multiply(*list):
    total = 1
    for number in list:
        total *= number
    return total


print("start")
print(multiply(1, 2, 3))
print("finish")
