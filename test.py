def analyze_input_length(user_input):
    modified_input = user_input.replace(" ", "")
    count = len(modified_input)
    print(f"Number of letters: {count}")

if __name__ == "__main__":
    user_input = input("Enter a sentence: ")
    analyze_input_length(user_input)

import unittest


class TestAnalyzeInputLength(unittest.TestCase):
    def test_only_letters(self):
        self.assertEqual(analyze_input_length("HelloWorld"), None)

    def test_letters_and_spaces(self):
        self.assertEqual(analyze_input_length("Hello World"), None)

    def test_empty_string(self):
        self.assertEqual(analyze_input_length(""), None)

    def test_only_spaces(self):
        self.assertEqual(analyze_input_length("     "), None)

    def test_special_characters_and_numbers(self):
        self.assertEqual(analyze_input_length("1234!@#$"), None)

if __name__ == "__main__":
    unittest.main()
