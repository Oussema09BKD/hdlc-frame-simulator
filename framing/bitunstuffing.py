# bit unstuffing function

data = "111110"

def bit_unstuffing(data):
    count = 0
    result =""

    for bit in data:
        if bit == "1":
            result = result + bit
            count = count+1
        else:
            if count == 5:                
                count = 0
                continue
            else:
              result = result+ bit
            count=0
    return result
print(bit_unstuffing("111110"))      # "11111"
print(bit_unstuffing("1111101"))     # "111111"
print(bit_unstuffing("10111110"))    # "1011111"
print(bit_unstuffing("011111010"))   # "01111110"