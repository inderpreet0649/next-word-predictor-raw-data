def build_lookup(words, input_len=10, output_len=5):
    store = {}

    for i in range(len(words) - input_len - output_len + 1):
        x = " ".join(words[i:i+input_len])
        y = " ".join(words[i+input_len:i+input_len+output_len])
        store[x] = y

    return store
