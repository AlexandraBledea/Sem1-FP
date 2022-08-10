# Source code for Test 1 program. Success!


def create_function(name, parameters, formula):
    return {'function_name': name, 'parameters_list': parameters, 'formula': formula}


def get_function_name(item):
    return item['function_name']


def get_parameters_list(item):
    return item['parameters_list']


def get_formula(item):
    return item['formula']


def split_command(command):  # we split the command in command_word and command_params
    tokens = command.strip().split(' ', 1)
    tokens[0] = tokens[0].strip().lower()
    return tokens[0], '' if len(tokens) == 1 else tokens[1].strip().lower()


def split_command_parameters(command_parameters, item_list):
    first_bracket = command_parameters.find("(")
    name = command_parameters[:first_bracket]
    second_bracket = command_parameters.find(")")
    parameters_list = command_parameters[first_bracket + 1:second_bracket]
    equality_sign = command_parameters.find("=")
    formula = command_parameters[equality_sign:]
    function = create_function(name, parameters_list, formula)
    if function in item_list:
        raise ValueError("Mamba function already declares")
    else:
        return function


def add_function_ui(item_list, command_parameters, command_word=None):
    function = split_command_parameters(command_parameters, item_list)
    item_list.append(function)


def display_add_function_ui(item_list, command_parameters, command_word):
    okay = 0
    if command_word.find(' ') == -1:
        for i in range(0, len(item_list)):
            if command_parameters == get_function_name(item_list[i]):
                print(get_function_name(item_list[i]) + '(' + get_parameters_list(item_list[i]) + ')'
                      + get_formula(item_list[i]))
                okay = 1
    if okay == 0:
        print("There are no such mamba functions available")


def print_menu():
    print('\n')
    print("The following commands are possible:")
    print("add function_name(p1,p2,...,pn)=p1(+|-)p2(+|-)p3(+|-)...(+|-)pn")
    print("list function_name")
    print("exit")
    print('\n')


def start_command_ui():
    item_list = []
    command_dict = {'list': display_add_function_ui, 'add': add_function_ui}
    are_we_done_yet = False
    while not are_we_done_yet:
        print_menu()
        command = input("Command> ")
        command_word, command_params = split_command(command)
        if command_params == '' and command_word != 'exit':
            print("Bad command!")
        else:
            if command_word in command_dict:
                try:
                    command_dict[command_word](item_list, command_params, command_word)
                except ValueError as ve:
                    print(ve)
            elif 'exit' == command_word:
                are_we_done_yet = True
            else:
                print('Invalid command')


start_command_ui()
