from framing.hdlc import create_frame
from receiver.hdlc_receiver import decode_frame
from channel.noise import introduce_error


data = "11101101111010001"
generator = "1101"

# Step 1: Create frame (sender)
frame = create_frame(data, generator)
print("HDLC Frame:", frame)

# Step 2: Decode frame (receiver)
decode_frame(frame, generator)

from framing.hdlc import create_frame
from receiver.hdlc_receiver import decode_frame
from channel.noise import introduce_error

data = "11101101111010001"
generator = "1101"

# Step 1: Create frame (sender)
frame = create_frame(data, generator)
print("HDLC Frame:", frame)

# Step 2: Simulate error
corrupted_frame = introduce_error(frame, 10)
print("Corrupted Frame:", corrupted_frame)

# Step 3: Decode corrupted frame
decode_frame(corrupted_frame, generator)