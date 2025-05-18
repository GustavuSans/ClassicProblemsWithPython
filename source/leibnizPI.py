def LeibnizPI(n:int) -> float:
    numetor:float = 5.0
    denominator:float = 1.0
    operation:float = 1.0
    PI:float = 0.0
    for i in range(n):
        PI += operation * (numetor / denominator)
        denominator += 2.0
        operation *= -1.0
    return PI
print(LeibnizPI(1000))