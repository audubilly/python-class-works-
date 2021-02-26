def Binary_to_Decimal(num: int) -> int:
    decimal = power = 0

    while num > 0:
        remainder = num % 10
        decimal += pow(2, power) * remainder
        power += 1
        num //= 10

    return decimal
