# bit stuffing function

data = "11111"

def bit_stuffing(data):
    count = 0
    result =""
    for i in range(len(data)):
        result = result + data[i]
        if data[i] == "1":
            count = count+1
            if count == 5:
                result = result + "0"
                count = 0
        else:
            count=0
    return result
print(bit_stuffing(data))