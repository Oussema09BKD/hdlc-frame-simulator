from framing.bitunstuffing import bit_unstuffing
from core.crc import compute_crc_remainder

def decode_frame(frame,generator):
    payload = frame[8:-8]
    unstuffed = bit_unstuffing(payload)
    crc_length = len(generator) - 1
    data = unstuffed[:-crc_length]
    received_crc = unstuffed[-crc_length:]

    expected_crc = compute_crc_remainder(data,generator)

    if(expected_crc == received_crc):
        print("CRC VALID")
    else:
        print("CRC ERROR")
    print("Received data:",data)

    return data   