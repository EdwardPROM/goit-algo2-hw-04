from trie import Trie

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list):
            raise TypeError(f"Illegal argument: strings = {strings} must be a list")
        
        if len(strings) == 0:
            return ""
        
        # Додаємо всі слова в Trie
        for s in strings:
            if not isinstance(s, str):
                raise TypeError(f"All elements in strings must be strings, got: {s}")
            self.put(s)

        prefix = ""
        current_node = self.root

        # Поки в нас один шлях вниз і вузол не є кінцем слова
        while current_node and len(current_node.children) == 1 and current_node.value is None:
            # Отримуємо єдиного нащадка
            char, next_node = next(iter(current_node.children.items()))
            prefix += char
            current_node = next_node
        
        return prefix

if __name__ == "__main__":
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    result = trie.find_longest_common_word(strings)
    print(f"✅ Тест 1: {result} (очікується 'fl')")
    assert result == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    result = trie.find_longest_common_word(strings)
    print(f"✅ Тест 2: {result} (очікується 'inters')")
    assert result == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    result = trie.find_longest_common_word(strings)
    print(f"✅ Тест 3: '{result}' (очікується '')")
    assert result == ""

    trie = LongestCommonWord()
    strings = []
    result = trie.find_longest_common_word(strings)
    print(f"✅ Тест 4: '{result}' (очікується '')")
    assert result == ""

    print("\n🏁 Усі тести пройдено успішно!")
