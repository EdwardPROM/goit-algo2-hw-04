from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            raise TypeError(f"Illegal argument: pattern = {pattern} must be a string")

        count = 0
        for word in self.keys():
            if word.endswith(pattern):
                count += 1
        return count

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise TypeError(f"Illegal argument: prefix = {prefix} must be a string")

        return len(self.keys_with_prefix(prefix)) > 0

# =========================
#        ТЕСТИ
# =========================
if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]

    for i, word in enumerate(words):
        trie.put(word, i)

    print("\n===============================")
    print("🔎 Перевірка суфіксів:")
    print("===============================\n")

    suffix_tests = [
        ("e", 1),
        ("ion", 1),
        ("a", 1),
        ("at", 1),
        ("zzz", 0)
    ]

    for suffix, expected in suffix_tests:
        result = trie.count_words_with_suffix(suffix)
        status = "✅" if result == expected else "❌"
        print(f"{status} Суфікс '{suffix}': знайдено {result}, очікувалося {expected}")

    print("\n===============================")
    print("🔎 Перевірка префіксів:")
    print("===============================\n")

    prefix_tests = [
        ("app", True),
        ("bat", False),
        ("ban", True),
        ("ca", True),
        ("dog", False)
    ]

    for prefix, expected in prefix_tests:
        result = trie.has_prefix(prefix)
        status = "✅" if result == expected else "❌"
        print(f"{status} Префікс '{prefix}': {result}, очікувалося {expected}")
