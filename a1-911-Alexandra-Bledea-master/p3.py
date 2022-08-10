#
# Implement the program to solve the problem statement from the third set here
#


def prime(n) :
    if n == 1 :
        return 1
    else :
         generator = 2 #generates the number, counting from 2 because the case when n is 1 is treated separately
         counter = 1 #if memorizing the number of prime factors found by far
         while True :
            div = 2
            copy = generator
            while copy > 1 and div * div <= copy :
                if copy % div == 0 : #we verify if the number div is a divisor of the current number
                    counter += 1
                    if counter == n : #we check if we reached the desired position
                        return div
                    while copy % div == 0 :
                        copy = copy // div
                div += 1

            if copy > 1 :
                counter += 1
                if counter == n:
                    return copy
            generator += 1



if __name__ == "__main__":
   n=int(input('Enter number'))
   print(prime(n))
