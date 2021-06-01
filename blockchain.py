# Initializing our blockchain list
blockchain = []


def get_last_blockchain_value():
    """Returns the last value of the current blockchain."""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """Append new value as well as the last blockchain value to blockchain.

    Args:
        transaction_amount (float): The amount that should be added,
        last_transaction (list, optional): The last blockchain transaction. Defaults to [1].
    """
    if last_transaction is None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """Returns the input of the user (a new transaction amount) as a float."""
    return float(input('Your transaction amount please: '))


def get_user_choice():
    return input('Your choice: ')


def print_blockchain_elements():
    for block_index, block in enumerate(blockchain):
        print(f'Outputting block {block_index + 1}')
        print(block)


def print_user_input_choices():
    print('Please choose')
    print('1, Add a new transaction value')
    print('2, Output the blockchain blocks')
    print('3, Manipulate the chain')
    print('4, Quit')


def valid_chain():
    block_index = 0
    is_valid = True

    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            print(block[0], ' -- ', blockchain[block_index - 1])
            is_valid = True
        else:
            is_valid = False
            break

        block_index += 1

    return is_valid


while True:
    print_user_input_choices()

    user_choice = get_user_choice()

    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == '3':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == '4':
        break
    else:
        print('Input was Invalid, please pick a value from the list!')

    if not valid_chain():
        print('Invalid blockchain')
        break

print('Done!')
