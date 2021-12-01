def find_integers(num):
    results = []
    for i in range(0, num):
        temp = bin(i)[2:]
        temp.split()
        for j in range(0, len(temp)):
            print(temp[j])

find_integers(5)