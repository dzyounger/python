N = 10
numsum = 0
count = 0
print("please input 10 numbers:")
while count < N:
    number = float(input("Number "+str(count+1)+": "))
    numsum = numsum + number
    count = count + 1
average = numsum / N
print("N = {}, Sum = {}".format(N, numsum))
print("Average = {:.2f}".format(average))
