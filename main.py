from utils.statistics import calculate_average, find_min, find_max
from utils.reader import read_numbers


def main():
    numbers = read_numbers("data/measurements.txt")

    print("Среднее значение:", calculate_average(numbers))
    print("Минимальное значение:", find_min(numbers))
    print("Максимальное значение:", find_max(numbers))


if __name__ == "__main__":
    main()
