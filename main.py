from framing.hdlc import create_frame
from receiver.hdlc_receiver import decode_frame

data = "11101101111010001"
generator = "1101"

# Step 1: Create frame (sender)
frame = create_frame(data, generator)
print("HDLC Frame:", frame)

# Step 2: Decode frame (receiver)
decode_frame(frame, generator)