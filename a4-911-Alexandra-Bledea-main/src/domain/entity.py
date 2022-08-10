"""
Domain file includes code for entity management
entity = number, transaction, expense etc.
"""


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


