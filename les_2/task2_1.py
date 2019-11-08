import re
import csv

os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []

param_name_to_result_list = {
    'Изготовитель ОС': os_prod_list,
    'Название ОС': os_name_list,
    'Код продукта': os_code_list,
    'Тип системы': os_type_list
}

regex_pattern = re.compile(
    r"(Изготовитель ОС|Название ОС|Код продукта|Тип системы):\s+(.+)"
)


def get_data(file_name):
    with open(file_name)as file:
        data = file.read()

    result = re.findall(regex_pattern, data)

    for param_name, param_value in result:
        param_name_to_result_list[param_name].append(param_value)


def write_to_csv(writing_file_name):
    for file_name in [f"info_{i}.txt" for i in range(1,4)]:
        get_data(file_name)

    main_data = type(param_name_to_result_list.keys())
    zip(*param_name_to_result_list.values())

    with open(writing_file_name, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(main_data)


if __name__ == '__main__':
    write_to_csv('main_data')
