def encode_message(text):
    i = 0
    encode_string = ''
    while i <= len(text) - 1:
        count = 1
        ch = text[i]
        j = i
        while j < len(text) - 1:
            if text[j] == text[j + 1]:
                count += 1
                j += 1
            else:
                break
        encode_string += str(count) + ch
        i = j + 1
    return encode_string

def decode_message(message):
    i = 0
    decode = ''
    while i <= len(message) - 1:
        cnt = int(message[i])
        word = message[i + 1]
        for j in range(cnt):
            decode += word
        i += 2
    return decode

with open('take_input', 'r') as data_1, open('encode.txt', 'w+') as data_2:
    data_2.write(encode_message(data_1.read()))

with open('encode.txt', 'r') as data_2, open('decode.txt', 'w+') as data_3:
    data_3.write(decode_message(data_2.read()))

