"""Contains functions that read/write from a file."""
# All functions should be looked over in general for cleaner solutions.


def get_new_id(filename="user_stories.csv", rowsep=",r,"):
    """Return an intiger based on how many stories there are in a file."""
    try:
        with open(filename, "r") as open_file:
            file_data = open_file.readline()
    except FileNotFoundError:
        return 1
    else:
        if not file_data:  # file_data == ""
            return 1
        file_data = file_data.split(rowsep)
        return len(file_data) + 1


def get_table(filename="user_stories.csv", rowsep=",r,", colsep=",c,"):
    """Read the content of a file and organize it into a table in the followin fashion:
    Each row is a story, a row has:
    0: ID (int),
    1: Story title,
    2: User story,
    3: Acceptance criteria,
    4: Buisness value (int),
    5: Estimation (h) (float),
    6: Status
    """
    # For readibility only. There are indexes in a list.
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
        # del identifier, buisness_val, estimation
        return table


def save_table(table, filename="user_stories.csv", rowsep=",r,", colsep=",c,"):
    """Save a table to a file."""
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
    """Return an updated table. New story's ID must match an existing ones."""
    idx = 0
    for i, row in enumerate(table):
        if row[0] == int(story[0]):
            idx = i
            break
    table[idx] = story
    return table


def del_story(table, story_id):
    """Return an updated table. story_id must match an existing ID."""
    found_row = False
    for i in range(len(table)):
        if not found_row:
            if table[i][0] == story_id:
                del table[i]
                found_row = i
                break
    for i in range(len(table)):
        if i >= found_row:
            table[i][0] -= 1
    return table
