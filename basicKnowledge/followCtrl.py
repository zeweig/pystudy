import random
def ifTest():
    print("Number play:")
    x = 0
    n = random.randint(0,100)
    count = 0
    while True:
        x = int(input("Please enter an integer 0<x<100: "))
        count+=1
        if x > n:
            print("Try a smaller number!")
        elif x < n:
            print("Try a larger number!")
        else:
            print("Congratulations!")
            print("You guessed %d times altogether!" % count)
            break


def forTest():
    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print(w, "len is:",len(w))

    for w in words[:]:  # Loop over a slice copy of the entire list.
        print(w, "len is:", len(w))
        if len(w)>10 :
            words.insert(0, "xxxxxxxxx")
    print(words)

    for i in range(5):
        print(i)

    for i in range(0, 10, 3):
        print(i)

    for i in range(len(words)):
        print(i, words[i])

    for n in range(2, 20):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else:
            print(n, 'is a prime number')

        for n in range(2, 20):
            for x in range(2, n):
                if n % x == 0:
                    print(n, 'equals', x, '*', n / x)
                    break
            print(n, 'is a prime number')

def testFollowCtrl():
    print("FollowCtrl test:")
    #ifTest()
    forTest()