import random
def zero_one_random():
    return random.randint(0,1)

def generate_uniform_random(a,b):
    if a == b:
        return a
    if a > b:
        a,b = b,a
    num_bits = 1

    while (1<<num_bits) < (b-a+2):
        num_bits+=1
    while True:
        result = 0
        for _ in range(num_bits):
            result = (result <<1) | zero_one_random()
        if result <= (b-a):
            break    
    return result + a

if __name__ == "__main__":
    # num = 1000
    # result = 0
    # for _ in range (num):
    #     result += zero_one_random()
    for _ in range(100):
        print(generate_uniform_random(-100,100))
    # print(result)