import math

class WordListAnalyzer:

    def get_frequency(self, word_list):

        letter_counts = {
            "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0,
            "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0,
            "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
        }

        for word in word_list:
            for letter in word:
                if letter in letter_counts:
                    letter_counts[letter] += 1

        sorted_letter_counts = sorted(
            letter_counts.items(),
            key=lambda item: item[1],
            reverse=True
        )

        return sorted_letter_counts

    def get_pattern(self, word, candidate):

        result = ["absent"] * 5
        candidate_letters = list(candidate)

        for i in range(5):
            if word[i] == candidate[i]:
                result[i] = "correct"
                candidate_letters[i] = None

        for i in range(5):
            if result[i] == "absent" and word[i] in candidate_letters:
                result[i] = "present"
                candidate_letters[candidate_letters.index(word[i])] = None

        return tuple(result)

    def alphabetical_next_word(self, word_list):
        return word_list[0]

    def greedy_next_word(self, word_list):

        sorted_letter_counts = self.get_frequency(word_list)

        scores = dict(sorted_letter_counts)
        word_scores = [0] * len(word_list)

        for index, word in enumerate(word_list):
            unique_letters = set(word)
            for letter in unique_letters:
                if letter in scores:
                    word_scores[index] += scores[letter]

        best_index = word_scores.index(max(word_scores))
        return word_list[best_index]

    def shannon_entropy_next_word(self, word_list):

        best_word = None
        best_entropy = -1
        for word in word_list:

            buckets = {}
            for candidate in word_list:
                pattern = self.get_pattern(word, candidate)
                buckets[pattern] = buckets.get(pattern, 0) + 1

            entropy = 0
            for count in buckets.values():
                p = count / len(word_list)
                entropy -= p * math.log2(p)

            if entropy > best_entropy:
                best_entropy = entropy
                best_word = word

        return best_word