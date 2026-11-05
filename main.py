import logging
from pathlib import Path

from utils.statistics import (
    calculate_average,
    find_min,
    find_max,
    validate_numbers
)
from utils.reader import read_numbers


def main():
    current_dir = Path.cwd()
    print("Рабочая папка:", current_dir)

    project_dir = Path(__file__).resolve().parent

    logs_dir = project_dir / "logs"
    logs_dir.mkdir(exist_ok=True)

    logging.basicConfig(
        filename=logs_dir / "app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8"
    )

    input_file = project_dir / "data" / "measurements.txt"

    logging.info("Программа запущена")

    try:
        logging.info("Начинаем чтение файла: %s", input_file)

        numbers = read_numbers(input_file)

        logging.info("Прочитано измерений: %s", len(numbers))

        validate_numbers(numbers)

        print("Среднее значение:", calculate_average(numbers))
        print("Минимальное значение:", find_min(numbers))
        print("Максимальное значение:", find_max(numbers))

        logging.info("Расчёты успешно выполнены")

    except FileNotFoundError:
        logging.error("Файл с измерениями не найден")
        print("Программа не может продолжить работу: файл отсутствует")

    except ValueError as error:
        logging.error("Ошибка при обработке данных: %s", error)
        print("Программа не может продолжить работу:", error)

    finally:
        logging.info("Работа программы завершена")


if __name__ == "__main__":
    main()
