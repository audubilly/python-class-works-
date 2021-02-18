



class HourlyPaidEmployee(Employee):
    def __init__(self, name: str , employee_id: int, hourly_rate: float)
        super(HourlyPaidEmployee, self).__init__(name, employee_id,)
        self.hourly_rate = hourly_rate
        self.num_of_hours = 0



    def earn(self) -> float:
        if self.num_of_hours <= 40:
            earning = self.num_of_hours * self.hourly_rate

        else:

            earning = 40 * self.hourly_rate
            earning += (self.num_of_hours - 40) * (self.hourly_rate * 1.5)

            return earning