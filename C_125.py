def punctuation_removal(sentence: str):
    punctuation = ["'", ",", ".", "?"]
    sent_list = list(sentence)
    for i in punctuation:
        for j in sent_list:
            if i == j:
                sent_list.remove(j)
    return ''.join(sent_list)

print(punctuation_removal("Let's try, Mike."))
