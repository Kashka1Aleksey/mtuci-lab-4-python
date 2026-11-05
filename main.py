import json
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
    project_dir = Path(__file__).resolve().parent

    config_file = project_dir / "config.json"

    with open(config_file, "r", encoding="utf-8-sig") as file:
        config = json.load(file)

    input_file = project_dir / config["input_file"]
    log_file = project_dir / config["log_file"]

    log_file.parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8"
    )

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
