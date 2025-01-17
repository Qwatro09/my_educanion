def all_variants(text):
    let = len(text)

    for i in range(let):
        yield text[i]

    for next_let in range(2, let + 1):
        for start in range(let - next_let + 1):
            yield text[start:(start + next_let)]


a = all_variants("abcde")
for i in a:
    print(i)
