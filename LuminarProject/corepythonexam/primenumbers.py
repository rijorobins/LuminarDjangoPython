def prime(lower,upper):
    for numb in range(lower, upper + 1):
       if numb > 1:
            for i in range(2, numb):
                if (numb % i) == 0:
                    break
            else:
                print(numb)
lower=int(input("Enter lower limit"))
upper=int(input("Enter upper limit"))
prime(lower,upper)