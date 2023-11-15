def get_logo_tokens_from_file(file_dir: str, valid_functions: tuple):
    with open(file_dir, 'r') as file:
        contents = file.read().replace("\n", " ").split(" ")

    final_instructions = []

    for index, token in enumerate(contents):
        if token.replace('.', '', 1).isdigit() or token == "" or token == " ":
            continue

        if token not in valid_functions:
            raise NotImplementedError(token)

        value = contents[index+1]
        if value.isdigit():
            value = int(value)
        elif value.replace('.', '', 1).isdigit():
            value = float(value)

        final_instructions.append((token, value))

    return final_instructions
