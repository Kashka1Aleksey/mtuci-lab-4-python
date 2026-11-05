from pathlib import Path

from utils.statistics import calculate_average, find_min, find_max, validate_numbers
from utils.reader import read_numbers


def main():
    current_dir = Path.cwd()
    print("Рабочая папка:", current_dir)

    project_dir = Path(__file__).resolve().parent

    logs_dir = project_dir / "logs"
    logs_dir.mkdir(exist_ok=True)

    input_file = project_dir / "data" / "measurements.txt"

    try:
        numbers = read_numbers(input_file)

        validate_numbers(numbers)

        print("Среднее значение:", calculate_average(numbers))
        print("Минимальное значение:", find_min(numbers))
        print("Максимальное значение:", find_max(numbers))

    except FileNotFoundError:
        print("Программа не может продолжить работу: файл отсутствует")

    except ValueError as error:
        print("Программа не может продолжить работу:", error)


if __name__ == "__main__":
    main()
