def add(a,b):
    k, t_a, t_b, carry_in, result = 1, a,b,0,0
    while t_a or t_b:
        ak, bk = a &k, b&k
        carry_out = (ak & bk) | (ak & carry_in) | (bk & carry_in)
        result |= ak ^ bk ^ carry_in
        k, t_a, t_b, carry_in = k <<1, t_a >>1,t_b>>1,carry_out <<1
    
    return result | carry_in

def multiply(x,y):
    result = 0
    while y:
        if y&1:
            result = add(result,x)
        x,y = x<<1,y>>1
    return result
if __name__ == "__main__":
    # print(add(32,23))
    print(multiply(928,12))