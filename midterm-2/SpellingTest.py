import sys


def spelling_test(s: str, l: list[str]) -> bool:

    used_words = [False for _ in range(len(l))]

    def spelling_test_helper(s: str, l: list[str]) -> bool:
        if not s:
            return True

        for i, word in enumerate(l):
            if used_words[i]:
                continue

            if s.startswith(word):
                used_words[i] = True
                s_slice = s[len(word):]

                if spelling_test_helper(s_slice, l):
                    return True

                used_words[i] = False

        return False

    return spelling_test_helper(s, l)


def main():
    s = input()
    lines = sys.stdin.readlines()

    print(spelling_test(s, [line.replace('\n', '') for line in lines]))


if __name__ == "__main__":
    main()
