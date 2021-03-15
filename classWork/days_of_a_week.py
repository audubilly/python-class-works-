# my_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# tasks = ["java", "sleep", "Python", "Data Science", "Catch cruise", "Flex", "Flex"]
#
# print(dict(zip(my_week, tasks)))
# zip(my_week, tasks)
#
#
# def make_daily_plans(days_of_week, tasks_):
#     my_daily_plans = {}
#     for x, y in zip(my_week, tasks):
#         my_daily_plans[x] = y
#
#
# def square(squares, values):
#     result = {}
#     for x, y in zip(squares, values):
#         result[x] = y * y
#     return result
#
#
# squares = ["Ones", "Two", "Three", "Four", "Five"]
# values = [1, 2, 3, 4, 5]
#
# print(square(squares, values))
#
#
# # print(dict(zip(squares, (values * values))))
#
#
# def lazy_range(n):
#     """ a lazy version of range"""
#     i = 0
#     while i < n:
#         yield i
#         i += 1
#     return i
#
#
# print(list(lazy_range(10)))
#

ds_group_collection = {}


def group_names():
    for i in range(1):
        x = input("enter key here: ")
        y = input("enter values: ")
        ds_group_collection[x] = y.split(",")
    return print(ds_group_collection)


if __name__ == '__main__':
    group_names()
