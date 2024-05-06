
import re
from typing import Callable
from functools import reduce


def generator_numbers(text:str):
    #\d+\.\d+|\d+ searches for numbers like 123.45 OR 678
    for match in re.finditer(r"\d+\.\d+|\d+", text):
        yield float(match.group(0))

def sum_profit(text: str, func: Callable[[str], float]) -> float:
    #sums all numbers in generator
    return reduce(lambda x,y : x+y, func(text))


def main():
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")


if __name__ == "__main__":
    main()
