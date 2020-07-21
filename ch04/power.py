def power(x,y):
    if y < 0:
        x,y = 1.0/x, -y
    result = 1
    while y:
        if y &1:
            result *= x
        x, y = x*x, y >> 1
    return result
if __name__ == "__main__":
    print(power(9,9))