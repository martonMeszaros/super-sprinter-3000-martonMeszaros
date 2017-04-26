def get_new_id(filename="user_stories.csv", rowsep=",r,"):
    try:
        with open(filename, "r") as open_file:
            file_data = open_file.readline()
    except FileNotFoundError:
        return 1
    else:
        if not file_data:
            return 1
        file_data = file_data.split(rowsep)
        return len(file_data) + 1


def get_table(filename="user_stories.csv", rowsep=",r,", colsep=",c,"):
    identifier = 0
    buisness_val = 4
    estimation = 5

    try:
        with open(filename, "r") as open_file:
            file_data = open_file.readline()
    except FileNotFoundError:
        return False
    else:
        if not file_data:
            return False
        file_data = file_data.split(rowsep)
        table = []
        for row in file_data:
            table.append(row.split(colsep))
        for row in table:
            row[identifier] = int(row[identifier])
            row[buisness_val] = int(row[buisness_val])
            row[estimation] = float(row[estimation])
        del identifier, buisness_val, estimation
        return table


def save_table(table, filename="user_stories.csv", rowsep=",r,", colsep=",c,"):
    rows = []
    for row in table:
        row[0] = str(row[0])
        row[1] = str(row[1])
        row[2] = str(row[2])
        row[3] = str(row[3])
        row[4] = str(row[4])
        row[5] = str(row[5])
        row[6] = str(row[6])
        rows.append(colsep.join(row))
    file_data = rowsep.join(rows)
    with open(filename, "w") as open_file:
        open_file.write(file_data)


def update_story(table, story):
    idx = 0
    for i, row in enumerate(table):
        if row[0] == int(story[0]):
            idx = i
            break
    table[idx] = story
    return table


def del_story(table, story_id):
    pass


if __name__ == "__main__":
    print(get_table())
