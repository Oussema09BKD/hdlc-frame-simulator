from core.crc import compute_crc_remainder
from framing.bitstuffing import bit_stuffing


def create_frame(data,generator):
    data_with_crc = data + compute_crc_remainder(data,generator)
    stuffed = bit_stuffing(data_with_crc)

    flag = "01111110"
    frame = flag + stuffed + flag

    return frame


