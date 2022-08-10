"""
This is the user interface module. These functions call functions from the domain and functions module.
"""
from src.functions.functions import total_of_transactions_until_that_day, insert_transaction_to_list, \
    replace_a_specific_transaction, remove_transactions_by_criteria, add_transaction_to_list, test_init, \
    order_bank_transactions_list, split_command, create_copy_of_list, total_of_transactions_with_a_specific_type,\
    calculate_the_maximum_amount_of_a_transaction_from_a_specific_day, filter_transactions_by_type
from src.domain.entity import get_amount, get_transaction_type, get_day, get_description


def display_the_maximum_for_a_transaction(bank_transactions_list, parameters):
    """
    :param bank_transactions_list:the list which contains transactions
    :param parameters: in this case will be for example: 'in 15' ot 'out 20'
    :return: it will return false, because it doesn't make any change
    """
    tokens = parameters.split(' ')
    if len(tokens) != 2:
        raise ValueError('Invalid parameters count')
    types = ['in', 'out']
    token1 = tokens[0]
    if token1 not in types:
        raise ValueError("Unknown type for transaction")
    token2 = int(tokens[1])
    if 1 > token2 or token2 > 31:
        raise ValueError("Unknown date for transaction")
    print_the_maximum_for_a_transaction(bank_transactions_list, token1, token2)


def print_the_maximum_for_a_transaction(bank_transactions_list, token1, token2):
    maximum_amount = calculate_the_maximum_amount_of_a_transaction_from_a_specific_day(bank_transactions_list, token1,
                                                                                       token2)
    if maximum_amount == 0:
        print("There is no such transaction")
    else:
        print("The maximum amount of money from day ", token2, " with the type of transaction ", token1, " is: ",
              maximum_amount)


def display_sum_of_transactions(bank_transactions_list, parameters):
    """
    :param bank_transactions_list:the list which contains transactions
    :param parameters: in this case will be for example: 'in" or 'out'
    :return: it will return false, because it doesn't make any change
    """
    if parameters.find(' ') == -1:
        print_total_sum_of_transactions_with_a_specific_type(bank_transactions_list, parameters)
    else:
        raise ValueError("Invalid number of parameters")
    return False


def print_total_sum_of_transactions_with_a_specific_type(bank_transactions_list, transaction_type):
    total, transaction_type = total_of_transactions_with_a_specific_type(bank_transactions_list, transaction_type)
    if transaction_type == 'in':
        print("The amount of all in transactions is: ", total)
    elif transaction_type == 'out':
        print("The amount of all out transactions is: ", total)
    else:
        print("Invalid transaction type")


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
    :return: it won't return anything but will display the transactions which fulfill the condition, for example it will
    display all transactions = 100 or > 30 and so on.
    """
    token2 = int(token2)
    for i in bank_transactions_list:
        if token1 == '>' and get_amount(i) > token2:
            print_bank_transaction(i)
        elif token1 == '=' and get_amount(i) == token2:
            print_bank_transaction(i)
        elif token1 == '<' and get_amount(i) < token2:
            print_bank_transaction(i)


def print_transaction_list_type_in(bank_transactions_list):
    """
    Will check all the transactions with type 'in' and will call another function to print them
    """
    for i in bank_transactions_list:
        if get_transaction_type(i) == 'in':
            print_bank_transaction(i)


def print_transaction_list_type_out(bank_transactions_list):
    """
    Will check all the transactions with type 'out' and will call another function to print them
    """
    for i in bank_transactions_list:
        if get_transaction_type(i) == 'out':
            print_bank_transaction(i)


def print_bank_transaction(transaction):
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
        print_bank_transaction(transactions)


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
    list, list in, list out, list balance 10, list >,<,= 10 and we call another function for each specific case
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
    return False


def print_help_function(bank_transactions_list=None, command_params=None):
    """
    It prints a help menu for the user by calling the command help
    """
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

    print('(D) Obtain different characteristics of the transactions')
    print('sum <type>')
    print('max <type> <day>\n')

    print('(E) Filter')
    print('filter <type>')
    print('filter <type> <value>\n')


def start_command_ui():
    bank_transactions_list = []
    test_init(bank_transactions_list)
    history_list = [create_copy_of_list(bank_transactions_list)]
    command_dict = {'list': display_list_ui, 'insert': insert_transaction_to_list, 'add': add_transaction_to_list,
                    'remove': remove_transactions_by_criteria, 'replace': replace_a_specific_transaction, 'help':
                    print_help_function, 'sum': display_sum_of_transactions, 'max':
                        display_the_maximum_for_a_transaction, 'filter': filter_transactions_by_type}
    are_we_done_yet = False
    while not are_we_done_yet:
        order_bank_transactions_list(bank_transactions_list)
        command = input("Command> ")
        command_word, command_params = split_command(command)
        if command_word in command_dict:
            try:
                if command_dict[command_word](bank_transactions_list, command_params):
                    history_list.append(create_copy_of_list(bank_transactions_list))
            except ValueError as ve:
                print(ve)
        elif 'exit' == command_word:
            are_we_done_yet = True
        elif 'undo' == command_word:
            if len(history_list) >= 2:  # we check if the history list has at least 2 list in it
                history_list.pop()  # we remove the last transaction list
                bank_transactions_list = create_copy_of_list(history_list[len(history_list)-1])
                # we update the current list with the correct values after using the command undo
            else:
                print("There are no operations to undo")
        else:
            print('Invalid command')
