from utils.statistics import validate_numbers

try:
    validate_numbers([])
    print("Проверка не пройдена")

except ValueError as error:
    print("Ошибка обработана:", error)


try:
    validate_numbers([10, 20, 30])
    print("Проверка непустого списка пройдена")

except ValueError as error:
    print("Ошибка:", error)
