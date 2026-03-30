def introduce_error(frame, position):
    frame = list(frame)

    if frame[position] == '1':
        frame[position] = '0'
    else:
        frame[position] = '1'

    return "".join(frame)