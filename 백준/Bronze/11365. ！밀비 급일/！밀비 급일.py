
while True:
    seq = input()
    if seq == "END":
        break
    list_seq = list(seq)
    reversed_seq = reversed(list_seq)
    print("".join(reversed_seq))