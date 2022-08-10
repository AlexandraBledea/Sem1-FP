#
# Write the implementation for A3 in this file
#

#
# domain section is here (domain = numbers, transactions, expenses, etc.)
# getters / setters
# No print or input statements in this section
# Specification for all non-trivial functions (trivial usually means a one-liner)


import datetime


def get_day(transaction):  # we take separately the date of transaction
    return int(transaction['day'])


def get_amount(transaction):  # we take separately the amount of transaction
    return int(transaction['amount'])


def get_transaction_type(transaction):  # we take separately the transaction type: in or out
    return str(transaction['type_'])


def get_description(transaction):  # we take separately the description for transaction
    return str(transaction['description'])


def set_amount(transaction, value):  # we set in the dictionary only the amount of money if it's needed
    transaction['amount'] = value


def add_transaction(bank_transactions_list, transaction):  # we add a transaction to the list
    bank_transactions_list.append(transaction)


# Functionalities section (functions that implement required features)
# No print or input statements in this section
# Specification for all non-trivial functions (trivial usually means a one-liner)
# Each function does one thing only
# Functions communicate using input parameters and their return values


def split_command(command):  # we split the command in command_word and command_params
    """
    :param command: for example: 'add 100 out food'
    :return: tokens[0] = 'add' and tokens[1] = '100 out food'
    """
    tokens = command.strip().split(' ', 1)
    tokens[0] = tokens[0].strip().lower()
    return tokens[0], '' if len(tokens) == 1 else tokens[1].strip()


def create_transaction(day_date, amount_of_money, transaction_type, transaction_description):  # we create a transaction
    """
    :param day_date: for example : 20 , where the number should be between 1 and 31 inclusively
    :param amount_of_money: for example: 100
    :param transaction_type: in or out only, for example: out
    :param transaction_description: for example: shopping
    :return: {'day': 20, 'amount': 100, 'type_': out,
            'description': shopping}
    """
    types = ['in', 'out']
    day = int(day_date)
    if transaction_type not in types:
        raise ValueError('Invalid type')
    if day < 1 or day > 31:
        raise ValueError('Invalid date')
    return {'day': day, 'amount': amount_of_money, 'type_': transaction_type,
            'description': transaction_description}


def order_bank_transactions_list(bank_transactions_list):
    """
    :param bank_transactions_list: it contains the dictionaries from the list which are transactions
    :return: will return the dictionaries from the list in an ascending order by day
    """
    aux = 0
    for i in range(0, len(bank_transactions_list) - 1):
        for j in range(i + 1, len(bank_transactions_list)):
            if get_day(bank_transactions_list[i]) > get_day(bank_transactions_list[j]):
                aux = bank_transactions_list[i]
                bank_transactions_list[i] = bank_transactions_list[j]
                bank_transactions_list[j] = aux
    return bank_transactions_list


def remove_transaction_by_date(bank_transactions_list, transaction_date):
    """
    :param bank_transactions_list: it contains the dictionaries from the list which are transactions
    :param transaction_date: the date for which we want to remove all the transactions
    for example: we delete all the transactions made on the date of 10
    :return: it won't return anything, it will only remove the transactions from the list
    """
    transaction_date = int(transaction_date)
    i = 0
    while i < len(bank_transactions_list):
        s = bank_transactions_list[i]
        if get_day(s) == transaction_date:
            del bank_transactions_list[i]
        else:
            i = i + 1


def remove_transaction_by_type(bank_transactions_list, transaction_type):
    """
    :param bank_transactions_list: it contains the dictionaries from the list which are transactions
    :param transaction_type: represent the type for the transactions we will remove
    for example: we delete all the transactions with the type in
    :return:  it won't return anything, it will only remove the transactions from the list
    """
    i = 0
    while i < len(bank_transactions_list):
        s = bank_transactions_list[i]
        if get_transaction_type(s) == transaction_type:
            del bank_transactions_list[i]
        else:
            i = i + 1


def remove_transaction_between_two_days(tokens, bank_transactions_list):
    """
    :param tokens: represents the dates between we want to remove all the transactions
    for example: between day 2 and 10 all the transactions will be deleted, inclusively day 2 and 10
    :param bank_transactions_list: it contains the dictionaries from the list which are transactions
    :return: it won't return anything, it will only remove the transactions from the list if the condition is verified
    or will raise a Value error in the contrary case
    """
    token1 = int(tokens[0])
    token2 = int(tokens[2])
    if tokens[1] == 'to' and token1 < token2:
        i = 0
        while i < len(bank_transactions_list):
            s = bank_transactions_list[i]
            if token1 <= get_day(s) <= token2:
                del bank_transactions_list[i]
            else:
                i = i + 1
    else:
        raise ValueError('Unknown parameter')


def remove_transaction_according_to_type(bank_transactions_list, parameters):
    """
    :param bank_transactions_list: it contains the dictionaries from the list which are transactions
    :param parameters: it will be either in, or out, or a number between or in the last case it will be a bad command
    which will raise a ValueError
    :return: it won't return anything, it will call other functions in case a condition is verified or will either raise
    a ValueError
    """
    if parameters == 'in':
        remove_transaction_by_type(bank_transactions_list, parameters)
    elif parameters == 'out':
        remove_transaction_by_type(bank_transactions_list, parameters)
    elif 1 <= int(parameters) <= 31:
        remove_transaction_by_date(bank_transactions_list, parameters)
    else:
        raise ValueError('Bad command!')


def remove_transactions_by_criteria(bank_transactions_list, parameters):
    """
    :param bank_transactions_list: it contains the dictionaries from the list which are transactions
    :param parameters: for example it can be: 10 or 5 to 10 or in or out
    :return: it won't return anything, but will call other functions in case a condition is verified or otherwise it
    will raise a ValueError
    """
    if parameters.find(' ') == -1:
        remove_transaction_according_to_type(bank_transactions_list, parameters)
    else:
        tokens = parameters.split(' ')
        if len(tokens) > 3:
            raise ValueError('Too many parameters')
        else:
            remove_transaction_between_two_days(tokens, bank_transactions_list)


def check_if_replace_possible(day, transaction_type, transaction_description, amount_of_money, bank_transactions_list):
    """
    :param day: for example: 10
    :param transaction_type: for example: out
    :param transaction_description: for example: shopping
    :param amount_of_money: for example: 2000
    :param bank_transactions_list: it contains the dictionaries from the list which are transactions
    :return: It won't return anything, but if the conditions are verified it will replace the amount of money at the
    transaction with date: 10, type: out, and description: shopping with 2000
    """
    ok = 0
    day = int(day)
    if ok == 0:
        amount_of_money = int(amount_of_money)
        for i in range(0, len(bank_transactions_list)):
            s = bank_transactions_list[i]
            if get_day(s) == day and get_transaction_type(
                    s) == transaction_type and transaction_description == get_description(s):
                set_amount(s, str(amount_of_money))
                ok = 1
    else:
        raise ValueError('There is no such transaction')


def replace_a_specific_transaction(bank_transactions_list, parameters):
    """
    :param bank_transactions_list: it contains the dictionaries from the list which are transactions
    :param parameters: for example: 12 in salary with 2000
    :return: it won't return anything, but instead will call another function
    """
    tokens = parameters.split(' ')  # we split the parameters
    if len(tokens) != 5:
        raise ValueError('Invalid parameters count to create a transaction')
    day = int(tokens[0].strip())
    transaction_type = tokens[1].strip()
    transaction_description = tokens[2].strip()
    amount_of_money = int(tokens[4].strip())
    check_if_replace_possible(day, transaction_type, transaction_description, amount_of_money, bank_transactions_list)


def add_transaction_to_list(bank_transactions_list, parameters):
    """
    With this function we split the parameters and after that we add another transaction to the current day if the
    condition is verified
    """
    tokens = parameters.split(' ')
    if len(tokens) != 3:
        raise ValueError('Invalid parameters count to create transaction')

    day = datetime.datetime.now()
    exact_day = day.day
    day = int(exact_day)
    amount_of_money = str(tokens[0].strip())
    transaction_type = tokens[1].strip()
    transaction_description = tokens[2].strip()

    transaction = create_transaction(day, amount_of_money, transaction_type, transaction_description)

    add_transaction(bank_transactions_list, transaction)


def insert_transaction_to_list(bank_transactions_list, parameters):
    """
    With this function we split the parameters and after that we add another transaction to a specified day if the
    first condition is verified
    """
    tokens = parameters.split(' ')
    if len(tokens) != 4:
        raise ValueError('Invalid parameters count to create a transaction')

    day = int(tokens[0].strip())
    amount_of_money = str(tokens[1].strip())
    transaction_type = tokens[2].strip()
    transaction_description = tokens[3].strip()

    transaction = create_transaction(day, amount_of_money, transaction_type, transaction_description)

    add_transaction(bank_transactions_list, transaction)


def total_of_transactions_until_that_day(bank_transactions_list, day_date):
    """
    In this function we calculate the amount of money spent and added to the account until a specified day
    :param bank_transactions_list: it contains the dictionaries from the list which are transactions
    :param day_date: the day until which we calculate the total amount of money for every transaction made until then
    :return: it won't return anything
    """
    total = 0
    day_date = int(day_date)
    for i in bank_transactions_list:
        if get_transaction_type(i) == 'in' and get_day(i) <= day_date:
            total = total + get_amount(i)
        elif get_transaction_type(i) == 'out' and get_day(i) <= day_date:
            total = total - get_amount(i)
    return total, day_date


# UI section
# (all functions that have input or print statements, or that CALL functions with print / input are  here).
# Ideally, this section should not contain any calculations relevant to program functionalities

#  print('Hello A3')


def display_list_with_option_balance(token, bank_transactions_list):
    token = int(token)
    if 1 <= token <= 31:
        day_date = token
        print_total_of_transactions_until_that_day(bank_transactions_list, day_date)
    else:
        raise ValueError('Invalid date')


def display_list_with_option(tokens, bank_transactions_list):
    symbols = ['<', '>', '=']
    if tokens[0] in symbols:
        display_list_with_symbols(tokens[0], tokens[1], bank_transactions_list)
    elif tokens[0] == 'balance':
        display_list_with_option_balance(tokens[1], bank_transactions_list)
    else:
        raise ValueError('Unknown parameters')


def print_total_of_transactions_until_that_day(bank_transactions_list, day_date):
    total, day_date = total_of_transactions_until_that_day(bank_transactions_list, day_date)
    if total > 0:
        print("Congratulations! Until day ", day_date, "you saved ", total, " $. Keep up the great work!")
    elif total < 0:
        total *= (-1)
        print("Bad luck! Until day ", day_date, "you are on a loss of", total, " $. Next time be more careful")
    else:
        print("You didn't lose money, but you didn't save them too, because your balance is ", total)


def display_list_with_symbols(token1, token2, bank_transactions_list):
    """
    Display the list if the command is:
    list + one of the symbols + amount of money
    :param token1: symbols: >, <, =
    :param token2: amount of money
    :param bank_transactions_list: the list which contains the transactions
    :return:
    """
    token2 = int(token2)
    for i in bank_transactions_list:
        if token1 == '>' and get_amount(i) > token2:
            print_bank_transactions_list(i)
        elif token1 == '=' and get_amount(i) == token2:
            print_bank_transactions_list(i)
        elif token1 == '<' and get_amount(i) < token2:
            print_bank_transactions_list(i)


def print_transaction_list_type_in(bank_transactions_list):
    """
    Will check all the transactions with type 'in' and will call another function to print them
    """
    for i in bank_transactions_list:
        if get_transaction_type(i) == 'in':
            print_bank_transactions_list(i)


def print_transaction_list_type_out(bank_transactions_list):
    """
    Will check all the transactions with type 'out' and will call another function to print them
    """
    for i in bank_transactions_list:
        if get_transaction_type(i) == 'out':
            print_bank_transactions_list(i)


def print_bank_transactions_list(transaction):
    """
    This function is printing the transactions
    """
    print("Day of transaction:", str(get_day(transaction)).rjust(2), " Amount of transaction: ",
          str(get_amount(transaction)).rjust(6), " Type of transaction: ",
          str(get_transaction_type(transaction)).rjust(3), " Description of the transaction: ",
          str(get_description(transaction)).rjust(10))


def display_complete_list(bank_transactions_list):
    """
    This function is calling another function to print the whole list of transactions
    """
    for transactions in bank_transactions_list:
        print_bank_transactions_list(transactions)


def display_list_according_to_type(bank_transactions_list, parameters):
    """
    With this function we check the type according to which we will call another function to print the list
    """
    if parameters == 'in':
        print_transaction_list_type_in(bank_transactions_list)
    elif parameters == 'out':
        print_transaction_list_type_out(bank_transactions_list)
    else:
        raise ValueError('Bad command!')


def display_list_ui(bank_transactions_list, parameters):
    """
    With this function we check which type of instruction was used for the command list, for example we can have:
    list, list in, list out, list balance 10, list >,<,= 10
    """
    if parameters == '':
        display_complete_list(bank_transactions_list)
    elif parameters.find(' ') == -1:
        display_list_according_to_type(bank_transactions_list, parameters)
    else:
        tokens = parameters.split(' ')
        if len(tokens) > 2:
            raise ValueError('Too many parameters')
        else:
            display_list_with_option(tokens, bank_transactions_list)


def print_help_function(bank_transactions_list=None, command_params=None):
    print('(A) Add transaction')
    print('add <value> <type> <description>')
    print('insert <day> <value> <type> <description>\n')

    print('(B) Modify transactions')
    print('remove <day>')
    print('remove <start day> to <end day>')
    print('remove <type>')
    print('replace <day> <type> <description> with <value>\n')

    print('(C) Display transactions having different properties')
    print('list')
    print('list <type>')
    print('list [ < | = | > ] <value>')
    print('list balance <day>\n')


def start_command_ui():
    bank_transactions_list = []
    test_init(bank_transactions_list)
    command_dict = {'list': display_list_ui, 'insert': insert_transaction_to_list, 'add': add_transaction_to_list,
                    'remove': remove_transactions_by_criteria, 'replace': replace_a_specific_transaction, 'help':
                    print_help_function}
    are_we_done_yet = False
    while not are_we_done_yet:
        order_bank_transactions_list(bank_transactions_list)
        command = input("Command> ")
        command_word, command_params = split_command(command)
        if command_word in command_dict:
            try:
                command_dict[command_word](bank_transactions_list, command_params)
            except ValueError as ve:
                print(ve)
        elif 'exit' == command_word:
            are_we_done_yet = True
        else:
            print('Invalid command')


# Test functions go here
#
# Test functions:
#   - no print / input
#   - great friends with assert


def test_init_in_transactions(bank_transactions_list):
    bank_transactions_list.append(create_transaction('1', '300', 'in', 'hair'))
    bank_transactions_list.append(create_transaction('1', '50', 'in', 'salary'))
    bank_transactions_list.append(create_transaction('3', '40', 'in', 'make-up'))
    bank_transactions_list.append(create_transaction('4', '100', 'in', 'salary'))
    bank_transactions_list.append(create_transaction('10', '1000', 'in', 'salary'))
    bank_transactions_list.append(create_transaction('30', '100', 'in', 'babysitting'))


def test_init_out_transactions(bank_transactions_list):
    bank_transactions_list.append(create_transaction('2', '150', 'out', 'pizza'))
    bank_transactions_list.append(create_transaction('18', '400', 'out', 'food'))
    bank_transactions_list.append(create_transaction('19', '500', 'out', 'clothes'))
    bank_transactions_list.append(create_transaction('25', '40', 'out', 'nails'))


def test_init3(bank_transactions_list):
    bank_transactions_list.append(create_transaction('2', '150', 'out', 'pizza'))
    bank_transactions_list.append(create_transaction('3', '40', 'in', 'make-up'))
    bank_transactions_list.append(create_transaction('4', '100', 'in', 'salary'))
    bank_transactions_list.append(create_transaction('10', '1000', 'in', 'salary'))
    bank_transactions_list.append(create_transaction('18', '400', 'out', 'food'))
    bank_transactions_list.append(create_transaction('19', '500', 'out', 'clothes'))
    bank_transactions_list.append(create_transaction('25', '40', 'out', 'nails'))
    bank_transactions_list.append(create_transaction('30', '100', 'in', 'babysitting'))


def test_init_replace_transaction(bank_transactions_list):
    bank_transactions_list.append(create_transaction('1', '500', 'in', 'hair'))
    bank_transactions_list.append(create_transaction('1', '50', 'in', 'salary'))
    bank_transactions_list.append(create_transaction('2', '150', 'out', 'pizza'))
    bank_transactions_list.append(create_transaction('3', '40', 'in', 'make-up'))
    bank_transactions_list.append(create_transaction('4', '100', 'in', 'salary'))
    bank_transactions_list.append(create_transaction('10', '1000', 'in', 'salary'))
    bank_transactions_list.append(create_transaction('18', '400', 'out', 'food'))
    bank_transactions_list.append(create_transaction('19', '500', 'out', 'clothes'))
    bank_transactions_list.append(create_transaction('25', '40', 'out', 'nails'))
    bank_transactions_list.append(create_transaction('30', '100', 'in', 'babysitting'))


def test_init_transactions_between_two_dates(bank_transactions_list):
    bank_transactions_list.append(create_transaction('1', '300', 'in', 'hair'))
    bank_transactions_list.append(create_transaction('1', '50', 'in', 'salary'))
    bank_transactions_list.append(create_transaction('19', '500', 'out', 'clothes'))
    bank_transactions_list.append(create_transaction('25', '40', 'out', 'nails'))
    bank_transactions_list.append(create_transaction('30', '100', 'in', 'babysitting'))


def test_init_insert_transaction(bank_transactions_list):
    bank_transactions_list.append(create_transaction('1', '300', 'in', 'hair'))
    bank_transactions_list.append(create_transaction('1', '50', 'in', 'salary'))
    bank_transactions_list.append(create_transaction('2', '150', 'out', 'pizza'))
    bank_transactions_list.append(create_transaction('3', '40', 'in', 'make-up'))
    bank_transactions_list.append(create_transaction('4', '100', 'in', 'salary'))
    bank_transactions_list.append(create_transaction('10', '1000', 'in', 'salary'))
    bank_transactions_list.append(create_transaction('18', '400', 'out', 'food'))
    bank_transactions_list.append(create_transaction('19', '500', 'out', 'clothes'))
    bank_transactions_list.append(create_transaction('25', '40', 'out', 'nails'))
    bank_transactions_list.append(create_transaction('30', '100', 'in', 'babysitting'))
    bank_transactions_list.append(create_transaction('31', '1000', 'out', 'furniture'))


def test_init_add_transaction(bank_transactions_list):
    bank_transactions_list.append(create_transaction('1', '300', 'in', 'hair'))
    bank_transactions_list.append(create_transaction('1', '50', 'in', 'salary'))
    bank_transactions_list.append(create_transaction('2', '150', 'out', 'pizza'))
    bank_transactions_list.append(create_transaction('3', '40', 'in', 'make-up'))
    bank_transactions_list.append(create_transaction('4', '100', 'in', 'salary'))
    bank_transactions_list.append(create_transaction('10', '1000', 'in', 'salary'))
    bank_transactions_list.append(create_transaction('18', '400', 'out', 'food'))
    bank_transactions_list.append(create_transaction('19', '500', 'out', 'clothes'))
    bank_transactions_list.append(create_transaction('25', '40', 'out', 'nails'))
    bank_transactions_list.append(create_transaction('30', '100', 'in', 'babysitting'))
    bank_transactions_list.append(create_transaction('20', '1000', 'out', 'furniture'))


def test_init2(bank_transactions_list):
    bank_transactions_list.append(create_transaction('1', '300', 'in', 'hair'))
    bank_transactions_list.append(create_transaction('1', '50', 'in', 'salary'))
    bank_transactions_list.append(create_transaction('2', '150', 'out', 'pizza'))
    bank_transactions_list.append(create_transaction('3', '40', 'in', 'make-up'))
    bank_transactions_list.append(create_transaction('4', '100', 'in', 'salary'))
    bank_transactions_list.append(create_transaction('10', '1000', 'in', 'salary'))
    bank_transactions_list.append(create_transaction('18', '400', 'out', 'food'))
    bank_transactions_list.append(create_transaction('19', '500', 'out', 'clothes'))
    bank_transactions_list.append(create_transaction('25', '40', 'out', 'nails'))
    bank_transactions_list.append(create_transaction('30', '100', 'in', 'babysitting'))


def test_init(bank_transactions_list):
    bank_transactions_list.append(create_transaction('4', '100', 'in', 'salary'))
    bank_transactions_list.append(create_transaction('2', '150', 'out', 'pizza'))
    bank_transactions_list.append(create_transaction('1', '300', 'in', 'hair'))
    bank_transactions_list.append(create_transaction('3', '40', 'in', 'make-up'))
    bank_transactions_list.append(create_transaction('1', '50', 'in', 'salary'))
    bank_transactions_list.append(create_transaction('18', '400', 'out', 'food'))
    bank_transactions_list.append(create_transaction('25', '40', 'out', 'nails'))
    bank_transactions_list.append(create_transaction('10', '1000', 'in', 'salary'))
    bank_transactions_list.append(create_transaction('30', '100', 'in', 'babysitting'))
    bank_transactions_list.append(create_transaction('19', '500', 'out', 'clothes'))

    # use this function to add the 10 required items
    # use it to set up test data


def test_order_bank_transactions_list():
    lst = []
    test_init(lst)
    lst2 = []
    test_init2(lst2)
    assert order_bank_transactions_list(lst) == lst2
    # assert order_bank_transactions_list(lst) != lst2


def test_split_command():
    cmd = '    aDd 10   2000   in    salary  '
    cmd_word, cmd_params = split_command(cmd)
    assert cmd_word == 'add'
    assert cmd_params == '10   2000   in    salary'

    cmd = 'eXit'
    cmd_word, cmd_params = split_command(cmd)
    assert cmd_word == 'exit'
    assert cmd_params == ''  # blank str for command with no params


def test_create_transaction():
    assert create_transaction(31, 2000, 'out', 'food') == {'day': 31, 'amount': 2000, 'type_': 'out',
                                                           'description': 'food'}
    # create_transaction(31, 2000, 'outt', 'shopping')
    # create_transaction(32, 2000, 'out', 'shopping')
    # create_transaction(1, 'dagsa', 'in, food)


def test_remove_transaction_by_date():
    # for an existing date
    lst = []
    test_init2(lst)
    lst3 = []
    test_init3(lst3)
    date = 1
    remove_transaction_by_date(lst, date)
    assert lst == lst3

    # if there is no such date
    lst = []
    test_init(lst)
    lst2 = []
    test_init(lst2)
    date2 = 6
    remove_transaction_by_date(lst, date2)
    assert lst == lst2


def test_remove_transaction_by_type():
    # for type in
    lst = []
    test_init2(lst)
    lst4 = []
    test_init_out_transactions(lst4)
    type1 = 'in'
    remove_transaction_by_type(lst, type1)
    assert lst == lst4

    # for type out
    lst = []
    test_init2(lst)
    lst2 = []
    test_init_in_transactions(lst2)
    type2 = 'out'
    remove_transaction_by_type(lst, type2)
    assert lst == lst2


def test_remove_transactions_between_two_dates():
    lst = []
    test_init2(lst)
    lst2 = []
    test_init_transactions_between_two_dates(lst2)
    dates = [2, 'to', 18]
    remove_transaction_between_two_days(dates, lst)
    assert lst == lst2


def test_remove_transaction_according_to_type():
    lst = []
    test_init2(lst)
    lst2 = []
    test_init_out_transactions(lst2)
    parameter1 = 'in'
    remove_transaction_according_to_type(lst, parameter1)
    assert lst == lst2

    lst = []
    test_init2(lst)
    lst3 = []
    test_init_in_transactions(lst3)
    parameter2 = 'out'
    remove_transaction_according_to_type(lst, parameter2)
    assert lst == lst3

    lst = []
    test_init2(lst)
    lst4 = []
    test_init3(lst4)
    parameter3 = 1
    remove_transaction_according_to_type(lst, parameter3)
    assert lst == lst4


def test_remove_transactions_by_criteria():
    lst = []
    test_init2(lst)
    lst2 = []
    test_init_out_transactions(lst2)
    parameter1 = 'in'
    remove_transactions_by_criteria(lst, parameter1)
    assert lst == lst2

    lst = []
    test_init2(lst)
    lst3 = []
    test_init_in_transactions(lst3)
    parameter2 = 'out'
    remove_transactions_by_criteria(lst, parameter2)
    assert lst == lst3

    lst = []
    test_init2(lst)
    lst4 = []
    test_init3(lst4)
    parameter3 = '1'
    remove_transactions_by_criteria(lst, parameter3)
    assert lst == lst4

    lst = []
    test_init2(lst)
    lst5 = []
    test_init_transactions_between_two_dates(lst5)
    parameter4 = '2 to 18'
    remove_transactions_by_criteria(lst, parameter4)
    assert lst == lst5


def test_check_if_replace_possible():

    date = 1
    amount_of_money = 500
    type1 = 'in'
    description = 'hair'
    lst = []
    test_init2(lst)
    lst2 = []
    test_init_replace_transaction(lst2)
    check_if_replace_possible(date, type1, description, amount_of_money, lst)
    assert lst == lst2


def test_replace_a_specific_transaction():
    parameters = '1 in hair with 500'
    lst = []
    test_init2(lst)
    lst2 = []
    test_init_replace_transaction(lst2)
    replace_a_specific_transaction(lst, parameters)
    assert lst == lst2


def test_insert_transaction_to_list():
    parameters = '31 1000 out furniture'
    lst = []
    test_init2(lst)
    lst2 = []
    test_init_insert_transaction(lst2)
    insert_transaction_to_list(lst, parameters)
    assert lst == lst2


test_insert_transaction_to_list()


def test_add_transaction_to_list():
    parameters = '1000 out furniture'
    lst = []
    test_init2(lst)
    lst2 = []
    test_init_add_transaction(lst2)
    add_transaction_to_list(lst, parameters)
    # assert lst == lst2
    # this test date set should be updated to the current day


# test_add_transaction_to_list()
test_order_bank_transactions_list()
test_split_command()
test_create_transaction()
test_remove_transaction_by_date()
test_remove_transaction_by_type()
test_remove_transactions_between_two_dates()
test_remove_transaction_according_to_type()
test_remove_transactions_by_criteria()
test_check_if_replace_possible()
test_replace_a_specific_transaction()
test_insert_transaction_to_list()

start_command_ui()
