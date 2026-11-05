def calculate_average(numbers):
    return sum(numbers) / len(numbers)


def find_min(numbers):
    return min(numbers)


def find_max(numbers):
    return max(numbers)


def validate_numbers(numbers):
    if not numbers:
        raise ValueError("Список измерений пуст")

    return True
