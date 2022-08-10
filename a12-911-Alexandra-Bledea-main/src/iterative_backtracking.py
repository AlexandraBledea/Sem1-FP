

def is_solution(solutions, coins, final_sum):
    """
    With this function firstly we compute the sum we have until that moment
     and after that we check if we reached the final sum
    :param solutions: represents the list with the number of times each coin appears in the sum
    :param coins: represents the list with the values of the coins
    :param final_sum: the sum we need to reach
    :return: it return true if the final sum was reached, or false otherwise
    """
    sum_ = 0
    for index in range(0, len(solutions)):
        sum_ = sum_ + coins[index] * solutions[index]
    if sum_ == final_sum:
        return True
    return False


def validate_sum(solutions, coins, final_sum):
    """
    With this function we first check if the list with the number of times each coin appears is created properly
    Then we compute the sum we have until that moment and after that check if the sum we obtain is a valid one, in
    this case, if the sum is not greater then the one we need to reach
    :param solutions: represents the list with the number of times each coin appears in the sum
    :param coins: represents the list with the values of the coins
    :param final_sum: the sum we need to reach
    :return: it returns false if the list with the number of times each coin appeared was not created properly
    or if the sum we have until that moment is not valid, otherwise it returns true
    """
    if len(solutions) > len(coins):
        return False
    sum_ = 0
    for index in range(0, len(solutions)):
        sum_ = sum_ + coins[index]*solutions[index]
        if sum_ > final_sum:
            return False
    return True


def display(solutions, coins):
    """
    With this function we display the solutions
    :param solutions: represents the list with the number of times each coin appears in the sum
    :param coins: represents the list with the values of the coins
    :return:it doesn't return anything
    """
    for index in range(0, len(solutions)):
        if solutions[index] != 0:
            print(str(solutions[index]) + '*' + str(coins[index]), end=" ")
    print()


def get_successor(solutions, final_sum, index):
    """
    With this function first we check if the value from the position index in the list solutions reached the value of
    the final sum, if so it returns False
    If not, it means we can increase the value from that index, which is actually done in this case
    :param solutions:  represents the list with the number of times each coin appears in the sum
    :param final_sum: the sum we need to reach
    :param index: represents the position of the coin in the vector coins and in this case it represents the position
    of the number of times that coin appeared in the sum, which is in the list solution
    :return: it returns false if the value from the list solutions at position index reached the final sum if not
    it returns true
    """
    if solutions[index] == final_sum:
        return False
    solutions[index] = solutions[index] + 1
    return True


def backtracking(coins, final_sum, solutions):
    """
    With this function we compute using iterative backtracking the ways a sum can be decomposed using n coins of
    distinct values
    :param coins: represents the list with the values of the coins
    :param final_sum: the sum we need to reach
    :param solutions: represents the list with the number of times each coin appears in the sum
    :return: returns true if at least on solution exists or false if there is no solution existent
    """

    counter = 0  # We use this param to count if there was at least one call of the display function
    index = 0  # We use this index to go through the solutions list and compute the solutions
    solutions.append(-1)  # We increase the solution list with one position which is incremented with -1
    while index >= 0:  # When the index will be smaller than 0 the backtracking process will end
        successor = True  # We initialize first the successor param as being True
        is_valid = False  # We initialize first the is_valid param as being False
        while successor and not is_valid:
            successor = get_successor(solutions, final_sum, index)  # We update the truth value of the param successor
            if successor:  # We check if there exists a successor
                is_valid = validate_sum(solutions, coins, final_sum)  # We update the truth value of the param is_valid
        if successor:  # If there exists a successor we check if we reached one of the solutions
            if is_solution(solutions, coins, final_sum):  # If we reached a solution we display it and inc counter
                display(solutions, coins)
                counter = counter + 1
            else:
                index = index + 1  # If we didn't reach a solution we move on with the index by incrementing it
                solutions.append(-1)  # We increase the solution list with one position which is incremented with -1
        else:
            index = index - 1  # If there is no successor then we go backwards
            solutions.pop()  # We pop out the last element from the list solutions

    if counter == 0:  # At the end of the backtracking we check if there existed at least one solution
        # If there was no solution we print the following message
        print("No payment modality exists")


def main():

    solutions = []
    coins = []
    try:
        print("Enter the sum: ")
        sum_ = int(input())
        print("Enter the number of coins: ")
        number_of_coins = int(input())
        print("Enter the values of the coins:")
        for i in range(number_of_coins):
            coin = int(input())
            coins.append(coin)
        coins.sort(reverse=False)  # We sort the list of coins in ascending order

        print()
        backtracking(coins, sum_, solutions)

    except ValueError as ve:
        print(ve)


main()
