def LeibnizPI(n:int) -> float:
    numerator:float = 4.0
    denominator:float = 1.0
    operation:float = 1.0
    PI:float = 0.0
    for i in range(n):
        PI += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
    return PI
print(LeibnizPI(1000000))