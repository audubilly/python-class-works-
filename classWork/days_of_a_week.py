my_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
tasks = ["java", "sleep", "Python", "Data Science", "Catch cruise", "Flex", "Flex"]

# print(dict(zip(my_week, tasks)))
zip(my_week, tasks)


def make_daily_plans(days_of_week, tasks):
    my_daily_plans = {}
    for x, y in zip(my_week, tasks):
        my_daily_plans[x] = y


make_daily_plans()
