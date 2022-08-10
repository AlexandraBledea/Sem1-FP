#
# Implement the program to solve the problem statement from the first set here
#
def cmmnr(n) :
    frecventa=[0]*10 #we implement an empty vector with 10 positions
    while n>0 :
        frecventa[n%10]=frecventa[n%10]+1 #we calculate how many times each digit appears
        n=n//10 #we cut the last digit
    okay=0
    m=0
    for i in range(1 , 10) : #we go through each digit
        for j in range(0 , frecventa[i]) : #with this for we display how many times each digit appears
            m=m*10 #we increase the number
            m=m+i #we add the next digit
            if frecventa[0]!=0 and okay==0 : #we check if in the number appears the digit 0 after we placed the first smallest digit
                for k in range(0,frecventa[0]) : #with this for we display how many times the digit 0 appears
                    m=m*10 #we increase the number
            okay=1
    return m


if __name__ == "__main__":
    print('m =',cmmnr(int(input('Read the number:'))))