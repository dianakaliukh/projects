def pair_counter(filename="text100.txt"):
    pairs = {"kd", "vq", "al"}
    with open(filename, encoding="utf-8") as f:
        for line in f:
            words = line.strip().split()
            count = 0
            for i in range(len(words)):
                w = words[i]
                # Пари всередині слова
                for j in range(len(w)-1):
                    pair = w[j:j+2]
                    if pair in pairs:
                        count += 1
                # Пара між словами (крім "k" в кінці і "d" на початку)
                if i + 1 < len(words):
                    last_char = words[i][-1]
                    first_char = words[i+1][0]
                    pair = last_char + first_char
                    if pair in pairs:
                        if not (last_char == 'у' and first_char == 'д'):
                            count += 1
            yield count

if __name__ == "__main__":
    total = 0
    for c in pair_counter():
        total += c
    print("Загальна кількість пар:", total)
