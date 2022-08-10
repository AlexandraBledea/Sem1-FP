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
        sum_ = sum_ + coins[index] * solutions[index]
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


def backtracking(coins, final_sum, solutions):
    """
    With this function we compute using recursive backtracking the ways a sum can be decomposed using n coins of
    distinct values
    :param coins: represents the list with the values of the coins
    :param final_sum: the sum we need to reach
    :param solutions: represents the list with the number of times each coin appears in the sum
    :return: returns true if at least on solution exists or false if there is no solution existent
    """
    counter = 0  # We use this param to count if there was at least one call of the display function
    solutions.append(0)  # We increase the solutions list with one position
    for value in range(0, final_sum + 1):
        # We go through all the values which are possible to represent the number of times a number appeared in the sum
        solutions[-1] = value  # We place on the last position from the list the value
        if validate_sum(solutions, coins, final_sum):  # We validate the sum
            if is_solution(solutions, coins, final_sum):  # We check if we reached a solution
                display(solutions, coins)  # If we reached a solution we display in and increment the counter
                counter = counter + 1
            else:  # If we didn't find a solution we call again the function backtracking and g further
                backtracking(coins, final_sum, solutions[:])

    if counter == 0:  # Here we check if there was at least on call of the display function if not it returns false
        # Otherwise it returns True
        ok = False
    else:
        ok = True
    return ok


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
        ok = backtracking(coins, sum_, solutions)
        if not ok:
            print("No payment modality exists!")

    except ValueError as ve:
        print(ve)


main()
