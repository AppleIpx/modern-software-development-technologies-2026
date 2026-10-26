# Дополнительно: палиндром без обратного среза и сравнение с решением через [::-1].
# Правила те же, что в palindrome.py: регистр и обычные пробелы игнорируются.


def clean(text):
    return text.lower().replace(" ", "")


def is_palindrome_slice(text):
    cleaned = clean(text)
    return cleaned != "" and cleaned == cleaned[::-1]


def is_palindrome_loop(text):
    cleaned = clean(text)
    if cleaned == "":
        return False
    # Обходим половину длины очищенной строки.
    for index in range(len(cleaned) // 2):
        if cleaned[index] != cleaned[len(cleaned) - 1 - index]:
            return False
    return True


def main():
    samples = ["А роза упала на лапу Азора", "а    ", "     ", "Python", "А!", "abba", "abc", ""]
    for sample in samples:
        by_slice = is_palindrome_slice(sample)
        by_loop = is_palindrome_loop(sample)
        status = "совпали" if by_slice == by_loop else "РАСХОДЯТСЯ"
        print(f"{sample!r}: срез={by_slice}, цикл={by_loop} — {status}")


if __name__ == "__main__":
    main()
