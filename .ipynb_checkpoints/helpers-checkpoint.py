def get_words(txt):
    words = ''
    for sms in txt:
        sms = str(sms)
        tokens = sms.split()
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()
        words += ' '.join(tokens) + ''
    return words