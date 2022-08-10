"""
Functions that implement program features. They should call each other, or other functions from the domain
"""
import datetime
from src.domain.entity import get_day, get_amount, get_description, get_transaction_type, add_transaction, set_amount


def create_copy_of_list(source_list):
    """
    :param source_list: current transactions list
    :return: the copy of transactions list
    """
    new_list = []
    for i in range(0, len(source_list)):
        new_list.append(source_list[i])

    return new_list


def split_command(command):  # we split the command in command_word and command_params
    """
    :param command: for example: 'add 100 out food'
    :return: tokens[0] = 'add' and tokens[1] = '100 out food'
    """
    tokens = command.strip().split(' ', 1)
    tokens[0] = tokens[0].strip().lower()
    return tokens[0], '' if len(tokens) == 1 else tokens[1].strip().lower()


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
    :param bank_transactions_list: it contains the transactions
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
    :param bank_transactions_list: it contains the transactions
    :param transaction_date: the date for which we want to remove all the transactions
    for example: we delete all the transactions made on the date of 10
    :return: true if a change was made, false if otherwise
    """
    a_transaction_was_removed = False
    transaction_date = int(transaction_date)
    i = 0
    while i < len(bank_transactions_list):
        s = bank_transactions_list[i]
        if get_day(s) == transaction_date:
            del bank_transactions_list[i]
            a_transaction_was_removed = True
        else:
            i = i + 1
    return a_transaction_was_removed


def remove_transaction_by_type(bank_transactions_list, transaction_type):
    """
    :param bank_transactions_list: it contains the transactions
    :param transaction_type: represent the type for the transactions we will remove
    for example: we delete all the transactions with the type in
    :return: true if a change was made, false if otherwise
    """
    a_transaction_was_removed = False
    i = 0
    while i < len(bank_transactions_list):
        s = bank_transactions_list[i]
        if get_transaction_type(s) == transaction_type:
            del bank_transactions_list[i]
            a_transaction_was_removed = True
        else:
            i = i + 1
    return a_transaction_was_removed


def remove_transaction_between_two_days(tokens, bank_transactions_list):
    """
    :param tokens: represents the dates between we want to remove all the transactions
    for example: between day 2 and 10 all the transactions will be deleted, inclusively day 2 and 10
    :param bank_transactions_list: it contains the transactions
    :return: true if a change was made, false if otherwise
    """
    a_transaction_was_removed = False
    token1 = int(tokens[0])
    token2 = int(tokens[2])
    if tokens[1] == 'to' and token1 < token2:
        i = 0
        while i < len(bank_transactions_list):
            s = bank_transactions_list[i]
            if token1 <= get_day(s) <= token2:
                del bank_transactions_list[i]
                a_transaction_was_removed = True
            else:
                i = i + 1
    else:
        raise ValueError('Unknown parameter')
    return a_transaction_was_removed


def remove_transaction_according_to_type(bank_transactions_list, parameters):
    """
    :param bank_transactions_list: it contains the transactions
    :param parameters: it will be either in, or out, or a date between 1 and 31 or in the last case it will be a bad
    command which will raise a ValueError
    :return: true if a change was made, false if otherwise
    """
    if parameters == 'in' or parameters == 'out':
        return remove_transaction_by_type(bank_transactions_list, parameters)
    elif 1 <= int(parameters) <= 31:
        return remove_transaction_by_date(bank_transactions_list, parameters)
    else:
        raise ValueError('Bad command!')


def remove_transactions_by_criteria(bank_transactions_list, parameters):
    """
    :param bank_transactions_list: it contains the transactions
    :param parameters: for example it can be: 10   /    5 to 10   /   in   /   out
    :return: true if a change was made, false if otherwise
    """
    if parameters.find(' ') == -1:
        return remove_transaction_according_to_type(bank_transactions_list, parameters)
    else:
        tokens = parameters.split(' ')
        if len(tokens) > 3:
            raise ValueError('Too many parameters')
        else:
            return remove_transaction_between_two_days(tokens, bank_transactions_list)


def check_if_replace_possible_and_perform_the_replace_if_possible(day, transaction_type, transaction_description,
                                                                  amount_of_money, bank_transactions_list):
    """
    :param day: for example: 10
    :param transaction_type: for example: out
    :param transaction_description: for example: shopping
    :param amount_of_money: for example: 2000
    :param bank_transactions_list: it contains the transactions
    :return:It will return true if the conditions are verified and it will replace the amount of money at the
    transaction with date: 10, type: out, and description: shopping with 2000
    """

    day = int(day)
    the_amount_of_money_from_the_specified_transaction_was_replaced = False
    amount_of_money = str(amount_of_money)
    for i in range(0, len(bank_transactions_list)):
        s = bank_transactions_list[i]
        if get_day(s) == day and get_transaction_type(
                s) == transaction_type and transaction_description == get_description(s):
            del bank_transactions_list[i]
            transaction = create_transaction(day, amount_of_money, transaction_type, transaction_description)
            add_transaction(bank_transactions_list, transaction)
            the_amount_of_money_from_the_specified_transaction_was_replaced = True
    if not the_amount_of_money_from_the_specified_transaction_was_replaced:
        raise ValueError('Transaction not found')
    else:
        return True


def replace_a_specific_transaction(bank_transactions_list, parameters):
    """
    :param bank_transactions_list: it contains the transactions
    :param parameters: for example: 12 in salary with 2000
    :return: true if a change was made, false if otherwise
    """
    tokens = parameters.split(' ')  # we split the parameters
    if len(tokens) != 5:
        raise ValueError('Invalid parameters count to create a transaction')
    day = int(tokens[0].strip())
    transaction_type = tokens[1].strip()
    transaction_description = tokens[2].strip()
    amount_of_money = int(tokens[4].strip())
    return check_if_replace_possible_and_perform_the_replace_if_possible(day, transaction_type, transaction_description,
                                                                         amount_of_money, bank_transactions_list)


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
    return True


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
    return True


def total_of_transactions_until_that_day(bank_transactions_list, day_date):
    """
    In this function we calculate the amount of money spent and added to the account until a specified day
    :param bank_transactions_list: it contains the transactions
    :param day_date: the day until which we calculate the total amount of money for every transaction made until then
    :return: it will return the total amount and the date
    """
    total = 0
    day_date = int(day_date)
    for i in bank_transactions_list:
        if get_transaction_type(i) == 'in' and get_day(i) <= day_date:
            total = total + get_amount(i)
        elif get_transaction_type(i) == 'out' and get_day(i) <= day_date:
            total = total - get_amount(i)
    return total, day_date


def total_of_transactions_with_a_specific_type(bank_transaction_list, transaction_type):
    """
    In this function we calculate the total amount of money from in or from out transactions
    """
    total = 0
    for i in bank_transaction_list:
        if get_transaction_type(i) == transaction_type:
            total = total + get_amount(i)
    return total, transaction_type


def calculate_the_maximum_amount_of_a_transaction_from_a_specific_day(bank_transactions_list, token1, token2):
    """
    :param bank_transactions_list: it contains the transactions
    :param token1: type of transaction
    :param token2: day o transaction
    :return: it will return the maximum_amount if such a transactions exists, else it will return maximum_amount = 0
    """
    maximum_amount = 0
    token2 = int(token2)
    for i in bank_transactions_list:
        if get_transaction_type(i) == token1 and get_day(i) == token2 and get_amount(i) > maximum_amount:
            maximum_amount = get_amount(i)
    return maximum_amount


def remove_transactions_with_opposite_type_of_filter_command(bank_transactions_list, transaction_type):
    """
    :param bank_transactions_list: it contains the transactions
    :param transaction_type: if the filter command was filter in, the transaction type will be out and vice versa
    :return: it will return True if at least transaction was removed, or false it
    """
    a_transaction_was_removed = False
    i = 0
    while i < len(bank_transactions_list):
        s = bank_transactions_list[i]
        if get_transaction_type(s) == transaction_type:
            del bank_transactions_list[i]
            a_transaction_was_removed = True
        else:
            i = i + 1
    return a_transaction_was_removed


def filter_transaction_by_type_and_value(bank_transactions_list, token1, token2):
    """
    This functions for example if the token1 has the type 'in' and token2 has the amount 100, it will remove all the out
    transactions and will delete also the transactions with type in which have an amount bigger than the one specified,
    in this case 100
    :param bank_transactions_list: it contains the transactions
    :param token1: type of transactions which can be in or out
    :param token2: the amount of money
    :return: it will return true if at least a transaction was removed, and false if not
    """
    token2 = int(token2)
    if token1 == 'in':
        transaction_type = 'out'
    elif token1 == 'out':
        transaction_type = 'in'
    else:
        raise ValueError("Invalid type for filter command")
    a_transaction_was_removed = False
    i = 0
    while i < len(bank_transactions_list):
        s = bank_transactions_list[i]
        if get_transaction_type(s) == transaction_type or (
                get_amount(s) >= token2 and get_transaction_type(s) == token1):
            del bank_transactions_list[i]
            a_transaction_was_removed = True
        else:
            i = i + 1
    return a_transaction_was_removed


def filter_transactions_by_type(bank_transactions_list, parameters):
    """
    :param bank_transactions_list: it contains the transactions
    :param parameters: type of transactions, it can be only in or out
    :return: it will return true if a change was made or false if not
    """
    if parameters.find(' ') == -1:
        if parameters == 'in':
            transaction_type = 'out'
            return remove_transactions_with_opposite_type_of_filter_command(bank_transactions_list, transaction_type)
        elif parameters == 'out':
            transaction_type = 'in'
            return remove_transactions_with_opposite_type_of_filter_command(bank_transactions_list, transaction_type)
        else:
            raise ValueError("Invalid type for filter command")
    else:
        tokens = parameters.split()
        if len(tokens) > 2:
            raise ValueError("The number of parameters is invalid")
        else:
            return filter_transaction_by_type_and_value(bank_transactions_list, tokens[0], tokens[1])


"""
test functions
"""


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
    bank_transactions_list.append(create_transaction('1', '50', 'in', 'salary'))
    bank_transactions_list.append(create_transaction('2', '150', 'out', 'pizza'))
    bank_transactions_list.append(create_transaction('3', '40', 'in', 'make-up'))
    bank_transactions_list.append(create_transaction('4', '100', 'in', 'salary'))
    bank_transactions_list.append(create_transaction('10', '1000', 'in', 'salary'))
    bank_transactions_list.append(create_transaction('18', '400', 'out', 'food'))
    bank_transactions_list.append(create_transaction('19', '500', 'out', 'clothes'))
    bank_transactions_list.append(create_transaction('25', '40', 'out', 'nails'))
    bank_transactions_list.append(create_transaction('30', '100', 'in', 'babysitting'))
    bank_transactions_list.append(create_transaction('1', '500', 'in', 'hair'))


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


def test_init_filter_in_100(bank_transactions_list):
    bank_transactions_list.append(create_transaction('1', '50', 'in', 'salary'))
    bank_transactions_list.append(create_transaction('3', '40', 'in', 'make-up'))


def test_init_filter_out_100(bank_transactions_list):
    bank_transactions_list.append(create_transaction('25', '40', 'out', 'nails'))


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
    check_if_replace_possible_and_perform_the_replace_if_possible(date, type1, description, amount_of_money, lst)
    assert lst == lst2


def test_replace_a_specific_transaction():
    parameters = '1 in hair with 500'
    lst = []
    test_init2(lst)
    lst2 = []
    test_init_replace_transaction(lst2)
    replace_a_specific_transaction(lst, parameters)
    assert lst == lst2


def test_create_copy_of_list():
    lst = []
    test_init2(lst)
    assert lst == create_copy_of_list(lst)


def test_insert_transaction_to_list():
    parameters = '31 1000 out furniture'
    lst = []
    test_init2(lst)
    lst2 = []
    test_init_insert_transaction(lst2)
    insert_transaction_to_list(lst, parameters)
    assert lst == lst2


def test_total_of_transactions_until_that_day():
    lst = []
    date1 = 5
    test_init2(lst)
    total1 = 340
    total2, date2 = total_of_transactions_until_that_day(lst, date1)
    assert date1 == date2 and total1 == total2


def test_total_of_transactions_with_a_specific_type():
    lst = []
    test_init2(lst)
    type1 = 'in'
    total1 = 1590
    total2, type2 = total_of_transactions_with_a_specific_type(lst, type1)
    assert total1 == total2 and type1 == type2

    type3 = 'out'
    total3 = 1090
    total4, type4 = total_of_transactions_with_a_specific_type(lst, type3)
    assert total3 == total4 and type3 == type4


def test_calculate_the_maximum_amount_of_a_transaction_from_a_specific_day():
    lst = []
    test_init2(lst)
    type1 = 'in'
    maximum1 = 300
    date1 = 1
    assert calculate_the_maximum_amount_of_a_transaction_from_a_specific_day(lst, type1, date1) == maximum1

    type2 = 'out'
    maximum2 = 500
    date2 = 19
    assert calculate_the_maximum_amount_of_a_transaction_from_a_specific_day(lst, type2, date2) == maximum2

    type3 = 'in'
    maximum3 = 1000
    date3 = 30
    assert calculate_the_maximum_amount_of_a_transaction_from_a_specific_day(lst, type3, date3) != maximum3


def test_remove_transactions_with_opposite_type_of_filter_command():
    lst = []
    test_init2(lst)
    lst1 = []
    test_init_in_transactions(lst1)
    type1 = 'out'
    remove_transactions_with_opposite_type_of_filter_command(lst, type1)
    assert lst == lst1

    lst = []
    test_init2(lst)
    type2 = 'in'
    lst2 = []
    test_init_out_transactions(lst2)
    remove_transactions_with_opposite_type_of_filter_command(lst, type2)
    assert lst == lst2


def test_filter_transactions_by_type():
    lst = []
    test_init2(lst)
    lst1 = []
    test_init_in_transactions(lst1)
    parameters1 = 'in'
    filter_transactions_by_type(lst, parameters1)
    assert lst == lst1

    lst = []
    test_init2(lst)
    lst1 = []
    parameters2 = 'out'
    test_init_out_transactions(lst1)
    filter_transactions_by_type(lst, parameters2)
    assert lst == lst1

    lst = []
    test_init2(lst)
    lst1 = []
    parameters3 = 'in 100'
    test_init_filter_in_100(lst1)
    filter_transactions_by_type(lst, parameters3)
    assert lst == lst1

    lst = []
    test_init2(lst)
    lst1 = []
    parameters4 = 'out 100'
    test_init_filter_out_100(lst1)
    filter_transactions_by_type(lst, parameters4)
    assert lst == lst1


def test_filter_transaction_by_type_and_value():
    lst = []
    test_init2(lst)
    lst1 = []
    test_init_filter_out_100(lst1)
    type1 = 'out'
    amount1 = 100
    filter_transaction_by_type_and_value(lst, type1, amount1)
    assert lst == lst1

    lst = []
    test_init2(lst)
    lst1 = []
    test_init_filter_in_100(lst1)
    type2 = 'in'
    amount2 = 100
    filter_transaction_by_type_and_value(lst, type2, amount2)
    assert lst == lst1

    lst = []
    test_init2(lst)
    lst1 = []
    test_init_filter_out_100(lst1)
    type2 = 'in'
    amount2 = 100
    filter_transaction_by_type_and_value(lst, type2, amount2)
    assert lst != lst1

    lst = []
    test_init2(lst)
    lst1 = []
    test_init_filter_in_100(lst1)
    type1 = 'out'
    amount1 = 100
    filter_transaction_by_type_and_value(lst, type1, amount1)
    assert lst != lst1


def test_add_transaction_to_list():
    parameters = '1000 out furniture'
    lst = []
    test_init2(lst)
    lst2 = []
    test_init_add_transaction(lst2)
    add_transaction_to_list(lst, parameters)
    # assert lst == lst2
    # this test date set should be updated to the current day


def call_test_functions():
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
    test_create_copy_of_list()
    test_total_of_transactions_with_a_specific_type()
    test_total_of_transactions_until_that_day()
    test_calculate_the_maximum_amount_of_a_transaction_from_a_specific_day()
    test_remove_transactions_with_opposite_type_of_filter_command()
    test_filter_transactions_by_type()
    test_filter_transaction_by_type_and_value()


call_test_functions()
