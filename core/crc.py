data = "100100"
generator = "1101"

# XOR function
def xor(x, y):
    result = ""
    for i in range(len(x)):
        result += "0" if x[i] == y[i] else "1"
    return result
# Appending "L-1" bits to the original data block
def extended_data(data, generator):
    return data + "0" * (len(generator) - 1)

# Generating the remainder 
def compute_crc_remainder(data, generator):
    n = len(generator)
    
    new_data = extended_data(data, generator)
    window = new_data[:n]

    for i in range(len(data)):
        # Step 1: XOR
        if window[0] == "1":
            window = xor(window, generator)
        else:
            window = xor(window, "0" * n)
        
        # Step 2: shift + bring next bit
        if i + n < len(new_data):
            window = window[1:] + new_data[i + n]
        else:
            window = window[1:]
    
    return window

def final_crc_data_block(data, generator):
    return data + compute_crc_remainder(data, generator)


print("Extended:", extended_data(data, generator))
print("Remainder:", compute_crc_remainder(data, generator))
print("Final crc data block:", final_crc_data_block(data, generator))