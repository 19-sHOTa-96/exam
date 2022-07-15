## EXERCISE-2
def bigger_Is_greater(w):
    ind1 = 0
    f = None

    while ind1 < len(w) -1:
        if w[ind1] < w[ind1+1]:
            f = ind1
        ind1 += 1

    ind2 = 0
    r = 0

    try:
        while ind2 < len(w):
            if w[ind2] > w[f]:
                r = ind2
            ind2 += 1

            w = list(w)
            w[f], w[r] = w[r], w[f]

            w = w[:f+1] + w[f+1:][::-1]
            
            result = "".join(w)
            return result

    except:
        return "no answer"

enter_words = input("Enter words: ").split(" ")
result = []

for word in enter_words:
    if word.isalpha():
        result.append(bigger_Is_greater(word))

print(" ".join(result))