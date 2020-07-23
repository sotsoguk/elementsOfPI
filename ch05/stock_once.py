# EPI 
# Chapter 5: Arrays
# 5.6 Buy and Sell Stock once

def buy_sell_stock_once(a):
    if not a or len(a) < 2:
        return 0
    min_stock,max_stock, margin_stock = a[0],a[0], 0
    for i in range(1,len(a)):
        if a[i] >= a[i-1]:
            max_stock = max(a[i],max_stock)
            margin_stock = max(margin_stock,max_stock-min_stock)
        elif a[i] < min_stock:
            min_stock = a[i]
            max_stock = a[i]
            
    return margin_stock

def longest_same(a):
    if not a or len(a) < 1:
        return 0
    longest_sequence = 1
    
    curr_sequence = 1
    prev_digit = a[0]
    for i in range(1,len(a)):
        if a[i] == prev_digit:
            curr_sequence += 1
        else:
            longest_sequence = max(longest_sequence,curr_sequence)
            curr_sequence = 1
            prev_digit = a[i]
            
    
    
    return max(longest_sequence, curr_sequence)

if __name__ == "__main__":
    a = [310,315,275,295,260,270,290,230,219,250]
    b = [1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,3,3,5,5,5,5]
    print(buy_sell_stock_once(a))
    print(longest_same(b))
