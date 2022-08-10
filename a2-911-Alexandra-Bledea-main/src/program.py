#
# Write the implementation for A2 in this file
#


#
# All non-UI functions go here
#
import math


def create_complex(real_part, imaginary_part):  # we place the values of the complex number in the dictionary
    return {'real': real_part, 'imaginary': imaginary_part}


def get_real_part(complex_number):  # we take separately only the real part
    return int(complex_number['real'])


def get_imaginary_part(complex_number):  # we take separately only the imaginary part
    return int(complex_number['imaginary'])


def compare_complex_numbers(z1, z2):  # in this function we compare to complex numbers
    # it returns true if both numbers are equal and false otherwise
    return get_real_part(z1) == get_real_part(z2) and get_imaginary_part(z1) == get_imaginary_part(z2)


def longest_sequence_of_3_distinct_values(complex_list):
    max_length_of_the_sequence = 0
    start_of_max_sequence = None
    for start_position in range(0, len(complex_list)):  # we make the comparison for every complex number
        a = 0  # we initialize every variable with 0
        b = 0
        c = 0
        i = start_position
        while i < len(complex_list):
            number = complex_list[i]  # we stock in the variable the value o the complex number
            if a == 0:  # we check if in a is no value, same for b and c
                a = number
            elif compare_complex_numbers(number, a):
                # we check if the current number has the same value as the initial one
                pass
            elif b == 0:
                b = number
            elif compare_complex_numbers(number, b):
                pass
            elif c == 0:
                c = number
            elif compare_complex_numbers(number, c):
                pass
            else:
                break  # it means we found the 4th distinct number
            i += 1
        final_position = i # we mark the final position
        length = final_position - start_position + 1
        if length > max_length_of_the_sequence:  # we check if the current length is bigger then the last one we saved
            max_length_of_the_sequence = length  # the current length
            start_of_max_sequence = start_position
    return start_of_max_sequence, max_length_of_the_sequence  # we return the length and the position of that sequence


def modulus_complex_number(complex_number):  # we calculate the module of a real number with the formula: sqrt(a^2+b^2)
    double_real = get_real_part(complex_number)*get_real_part(complex_number)
    double_imaginary = get_imaginary_part(complex_number)*get_imaginary_part(complex_number)
    modulus = math.sqrt(double_real + double_imaginary)
    return modulus


def difference_modulus(z1, z2):  # we calculate the difference between them
    return int(modulus_complex_number(z1) - modulus_complex_number(z2))


def check_prime(z1, z2):  # we check if the difference is prime number or not
    number = difference_modulus(z1, z2)
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    div = 3
    while div * div <= number:
        if number % div == 0:
            return False
        div += 1
    return True


def longest_sequence_of_prime_difference_modulus(complex_list):
    start_position = None
    final_position = None
    max_length = -1
    for i in range(0, len(complex_list)):
        for j in range(i+1, len(complex_list)):
            if check_prime(complex_list[j-1], complex_list[j]):
                if j-i+1 > max_length:
                    max_length = j-i+1
                    start_position = i
                    final_position = j
            else:
                break
    return start_position, final_position, max_length


#
# UI functions are here (everything with print / input, or calls a function with print / input)
#


def print_the_longest_sequence_of_prime_difference_modulus(complex_list):
    start_position, final_position, length = longest_sequence_of_prime_difference_modulus(complex_list)
    # we put in a list the two values we obtained
    if length > 1:
        for i in range(start_position, final_position+1):
            print_complex_number(complex_list[i])
    else:
        print('The difference between the modulus of consecutive numbers is not a prime number')


def print_complex_number(complex_number):  # with this function we print the complex number using the form z = a + bi
    if get_imaginary_part(complex_number) < 0:
        sign = '-'
        print(str(get_real_part(complex_number)).rjust(3) + ' ' + sign + '' +
              str(abs(get_imaginary_part(complex_number))).rjust(3) + 'i')
    elif get_imaginary_part(complex_number) > 0:
        sign = '+'
        print(str(get_real_part(complex_number)).rjust(3) + ' ' + sign + '' +
              str(abs(get_imaginary_part(complex_number))).rjust(3) + 'i')
    elif get_imaginary_part(complex_number) == 0:
        print(str(get_real_part(complex_number)).rjust(3))


def print_the_longest_sequence_of_3_distinct_values(complex_list):
    lst = longest_sequence_of_3_distinct_values(complex_list)  # we put in a list the two values we obtained
    start_position = lst[0]
    length = lst[1]
    i = start_position
    while length > 1:
        length -= 1
        print_complex_number(complex_list[i])
        i += 1


def read_complex():  # with this function we read new complex numbers
    real = int(input('Real part = '))
    imaginary = int(input('Imaginary part = '))
    return create_complex(real, imaginary)


def read_a_list_of_complex_numbers(complex_list):
    the_number_of_numbers = int(input('Enter how many numbers do you want to add:'))
    count_when_to_stop = 0
    while count_when_to_stop < the_number_of_numbers:
        add_complex_number_to_list(complex_list)
        count_when_to_stop += 1


def add_complex_number_to_list(complex_list):
    complex_list.append(read_complex())


def display_list(complex_list):  # with this function we display the list of complex numbers
    for complex_numbers in complex_list:
        print_complex_number(complex_numbers)


def print_menu():
    print('\n1. Add a complex number to the list')
    print('2. Display the entire list of complex numbers')
    print('3. Display a sequence which contains at most 3 distinct values')
    print('4. Display if the difference between the modulus of consecutive numbers is a prime number. ')
    print('0. Exit the application.')


def start():
    complex_list = []  # we create a list for the complex numbers
    init_values(complex_list)

    command_dict = {'2': display_list, '1': read_a_list_of_complex_numbers, '3':
                    print_the_longest_sequence_of_3_distinct_values,
                    '4': print_the_longest_sequence_of_prime_difference_modulus}
    are_we_done_yet = False
    n = 0
    while not are_we_done_yet:
        print('\nMENU')
        print_menu()
        command = input('\nWhat would you like to do? Enter command: \n')
        if command == '0':
            are_we_done_yet = True
        elif command not in command_dict:
            print('Invalid command!')
        else:
            x = command_dict[command]
            x(complex_list)


def init_values(complex_list):  # with this function we implement the 10 complex numbers we were asked
    complex_list.append(create_complex(1, 0))
    complex_list.append(create_complex(-9, 0))
    complex_list.append(create_complex(6, 8))
    complex_list.append(create_complex(-3, 4))
    complex_list.append(create_complex(2, 0))
    complex_list.append(create_complex(1, 0))
    complex_list.append(create_complex(-9, 0))
    complex_list.append(create_complex(-9, -3))
    complex_list.append(create_complex(-9, -3))
    complex_list.append(create_complex(-9, -3))
    complex_list.append(create_complex(-9, -3))
    complex_list.append(create_complex(-9, 0))
    complex_list.append(create_complex(-6, 8))
    complex_list.append(create_complex(-2, 23))
    complex_list.append(create_complex(-4, 3))
    complex_list.append(create_complex(10, 13))


start()