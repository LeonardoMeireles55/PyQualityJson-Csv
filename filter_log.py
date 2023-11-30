def filter_text():
    path = "./log.txt"
    array_lines = []

    with open(path, 'r', encoding='utf-8', errors='ignore') as input_lines:
        lines = input_lines.readlines()

        for line in lines:
            if "PCCC1" in line or "PCCC2" in line:
                array_lines.append(line)

    def extract_date(line):
        steps = line.split(';')
        dates = steps[4]
        return dates

    sorted_lines = sorted(array_lines, key=extract_date)

    with open('./outfiles/archive_filtered.txt', 'a') as output_lines:
        output_lines.writelines(sorted_lines)

    print("Sucess :)")
