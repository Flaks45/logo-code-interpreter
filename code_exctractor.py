def get_logo_tokens_from_file(file_dir: str, valid_functions: tuple):
    with open(file_dir, 'r') as file:
        contents = file.read().replace("\n", " ").split(" ")

    final_instructions = []
    repeat_instructions = []
    repeat_amount = 0
    repeat_remaining = 0

    for index, token in enumerate(contents):
        if (token.replace('.', '', 1).isdigit() or token == "" or token == " "
                or all(item.isdigit() for item in token.split("|"))):
            continue

        if token not in valid_functions:
            raise NotImplementedError(token)

        value = contents[index + 1]

        if token == "repeat":
            repeat_amount = int(value.split("|")[0])
            repeat_remaining = int(value.split("|")[1])
            continue

        if value.isdigit():
            value = int(value)
        elif value.replace('.', '', 1).isdigit():
            value = float(value)
        elif all(item.isdigit() for item in value.split("|")):
            value = tuple(map(int, tuple(value.split("|"))))

        if repeat_remaining <= 0 and repeat_amount > 0:
            for i in range(repeat_amount):
                final_instructions += repeat_instructions

        elif repeat_remaining > 0:
            repeat_instructions.append((token, value))
            repeat_remaining -= 1
            if repeat_remaining <= 0:
                for i in range(repeat_amount):
                    final_instructions += repeat_instructions
            continue

        final_instructions.append((token, value))

    print(final_instructions)
    return final_instructions
