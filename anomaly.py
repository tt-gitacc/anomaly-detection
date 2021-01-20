import statistics
def get_col(A, i):
    return [float(row[i]) for row in A]
fp = open("C:/Users/tim_t/Downloads/mammal_sleep_1.txt","r")
#read the file into a matrix
lines = [line.rstrip().split("\t") for line in fp]

#get each column (attribute) in the matrix
for i in range (1, len(lines[0])):
    #extract all the attribute values into an array x
    x = get_col(lines, i)
    #mean
    themean = statistics.mean(x)
    #stdev
    thestd = statistics.stdev(x)
    #for each entry in x, check whether it is an anomaly, print anomalous values.
    for val in x:
        if  val > themean+(2*thestd) or val < themean - (2*thestd):
            print(str(val) + " is an anomalous value")

fp.close()
