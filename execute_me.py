from filter_log import filter_text
from generate_csv import import_csv

filter_text()


path = "./outfiles/archive_filtered.txt"
with open(path, 'r') as archive_text:
    archive = archive_text.readlines()

lines = [line.strip() for line in archive]
array_values = []

unique_entries = set()

for line in lines:
    fields = line.strip().split(';')
    fields = [field.strip('"') for field in fields]
    
    date = str(fields[4] + "/" + fields[5])
    formatted_date = f"{date[6:8]}-{date[4:6]}-{date[:4]} {date[9:]}"

    level = str(fields[15])
    level_lot = str(fields[16])
    test_lot = str(fields[17])
    unit_value = str(fields[12])
    name = str(fields[9])
    value_test = str(fields[10])
    mean = str(fields[20])
    sd = str(fields[21])

    entry_key = (
        formatted_date, level_lot, test_lot,
        level, unit_value, name, value_test, mean, sd
    )

    if entry_key not in unique_entries:
        unique_entries.add(entry_key)

        array_values.append({
            "date": formatted_date,
            "level_lot": level_lot,
            "test_lot": test_lot,
            "level": level,
            "unit_value": unit_value,
            "name": name,
            "value": value_test,
            "mean": mean,
            "sd": sd
        })

with open('./outfiles/integra_400.json', 'w') as arquivo_saida:
    if arquivo_saida.tell() == 0:
        arquivo_saida.write("[\n")
    for i, values in enumerate(array_values):
        arquivo_saida.write(
            f'{{"date": "{values["date"]}", "level": "{values["level"]}", "level_lot": "{values["level_lot"]}", '
            f'"test_lot": "{values["test_lot"]}", "unit_value": "{values["unit_value"]}", "name": "{values["name"]}", '
            f'"value": "{values["value"]}", "mean": "{values["mean"]}", "sd": "{values["sd"]}"}}')
        if i < len(array_values) - 1:
            arquivo_saida.write(',\n')
        else:
            arquivo_saida.write('\n]')
import_csv()