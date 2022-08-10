#
# Implement the program to solve the problem statement from the second set here
#
def checkyear(y) : #with this function we are checking if it is a leap year or not
    ok=0
    if y%400==0 :
        ok=1
    if ok==0 :
        if y%4==0 and y%100!=0 :
            ok=1
    if ok==1 :
        return True
    else :
        return False


def daytype(d) : #with this function we display the suffixes for each day
    if d==1 :
        return 'st'
    elif d==2 :
        return 'nd'
    elif d==3 :
        return 'rd'
    elif d>=4 :
        return 'th'


def day(x, l, month) :
    d = 0
    m = 0
    ok = 0
    for i in range(0, 12):
         if x <= l[i] :
            d = x - l[i - 1]
            m=i-1
            ok = 1
            break
    if ok == 0 : #we take separately the case where the number is bigger than 334 and 335
        d = x - l[11]
        m = 11
    print(month[m],str(d) + daytype(d))


if __name__ == "__main__":
    y=int(input('Enter year '))
    date=int(input('Enter the date '))
    month=["January","February","March","April","May","June","July","August","September","October","November","December"] #i created a list for the months
    if checkyear(y) == False: #with this condition we call the function checkyear to see if we have a leap year or not, and if it is a leap year we create only one list which we will use
        l = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334] #the 1st of each month number from which we substract 1 so we could obtain the right date
    else :
        l = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335] #the list for the leap year
    day(date,l,month)