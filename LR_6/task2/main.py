from trie import Trie

class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not strings or not all(isinstance(s, str) for s in strings):
            raise TypeError("Input must be a non-empty list of strings")

        # Додаємо всі слова в префіксне дерево
        for i, word in enumerate(strings):
            self.put(word, i)

        current = self.root
        common_prefix = []

        # Рухаємось по дереву поки є спільний шлях
        while len(current.children) == 1:
            char, next_node = next(iter(current.children.items()))
            common_prefix.append(char)
            current = next_node

            # Перевіряємо чи всі слова містять цей префікс
            if not all(word.startswith(''.join(common_prefix)) for word in strings):
                common_prefix.pop()
                break

        return ''.join(common_prefix)

if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
    
    