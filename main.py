from framing.hdlc import create_frame

data = "11101101111010001"
generator = "1101"

frame = create_frame(data, generator)
print("HDLC Frame:", frame)