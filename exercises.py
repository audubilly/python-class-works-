my_week = ["sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


def modify_week(weeks):
    weeks.append(weeks.pop(0))
    print(weeks)


if __name__ == '__main__':
    modify_week(my_week)
