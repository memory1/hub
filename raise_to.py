def raise_to(exp):
    def raise_to_exp(x):
        print(pow(x,exp))
    return raise_to_exp(2)