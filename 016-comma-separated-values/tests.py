import unittest
from comma_separated_values import parse_csv

# TESTING
programming_praxis_example = """1,abc,def ghi,jkl,unquoted character strings
2,"abc","def ghi","jkl",quoted character strings
3,123,456,789,numbers
4, abc,def , ghi ,strings with whitespace
5, "abc","def" , "ghi" ,quoted strings with whitespace
6, 123,456 , 789 ,numbers with whitespace
7,	123,456	,	789	,numbers with tabs for whitespace
8, -123, +456, 1E3,more numbers with whitespace
9,123 456,123"456, 123 456 ,strange numbers
10,abc",de"f,g"hi,embedded quotes
11,"abc\""","de""f","g""hi",quoted embedded quotes
12,"","" "",""x"",doubled quotes
13,"abc"def,abc"def","abc" "def",strange quotes
14,,"", ,empty fields
15,abc,"def
ghi",jkl,embedded newline
16,abc,"def",789,multiple types of fields"""


programming_praxis_solution = """1|abc|def ghi|jkl|unquoted character strings
2|abc|def ghi|jkl|quoted character strings
3|123|456|789|numbers
4| abc|def | ghi |strings with whitespace
5| "abc"|def | "ghi" |quoted strings with whitespace
6| 123|456 | 789 |numbers with whitespace
7|	123|456	|	789	|numbers with tabs for whitespace
8| -123| +456| 1E3|more numbers with whitespace
9|123 456|123"456| 123 456 |strange numbers
10|abc"|de"f|g"hi|embedded quotes
11|abc"|de"f|g"hi|quoted embedded quotes
12|| ""|x""|doubled quotes
13|abcdef|abc"def"|abc "def"|strange quotes
14||| |empty fields
15|abc|def
ghi|jkl|embedded newline
16|abc|def|789|multiple types of fields"""


class CommaSeparatedValuesTestCase(unittest.TestCase):

    def test_unquoted_character_strings(self):
        record = '1,abc,def ghi,jkl,unquoted character strings'
        result = [["1", "abc", "def ghi", "jkl", "unquoted character strings"]]
        self.assertEqual(parse_csv(record), result)

    def test_quoted_character_strings(self):
        record = '2,"abc","def ghi","jkl",quoted character strings'
        result = [["2", "abc", "def ghi", "jkl", "quoted character strings"]]
        self.assertEqual(parse_csv(record), result)

    def test_numbers(self):
        record = '3,123,456,789,numbers'
        result = [["3", "123", "456", "789", "numbers"]]
        self.assertEqual(parse_csv(record), result)

    def test_strings_with_whitespace(self):
        record = '4, abc,def , ghi ,strings with whitespace'
        result = [["4", " abc", "def ", " ghi ", "strings with whitespace"]]
        self.assertEqual(parse_csv(record), result)

    def test_quoted_strings_with_whitespace(self):
        record = '5, "abc","def" , "ghi" ,quoted strings with whitespace'
        result = [["5", " \"abc\"", "def ",
                   " \"ghi\" ", "quoted strings with whitespace"]]
        self.assertEqual(parse_csv(record), result)

    def test_numbers_with_whitespace(self):
        record = '6, 123,456 , 789 ,numbers with whitespace'
        result = [["6", " 123", "456 ", " 789 ", "numbers with whitespace"]]
        self.assertEqual(parse_csv(record), result)

    def test_numbers_with_tabs_for_whitespace(self):
        record = '7,	123,456	,\t789\t,numbers with tabs for whitespace'
        result = [["7", "	123", "456	",
                   "	789	", "numbers with tabs for whitespace"]]
        self.assertEqual(parse_csv(record), result)

    def test_more_numbers_with_whitespace(self):
        record = '8, -123, +456, 1E3,more numbers with whitespace'
        result = [["8", " -123", " +456", " 1E3",
                   "more numbers with whitespace"]]
        self.assertEqual(parse_csv(record), result)

    def test_strange_numbers(self):
        record = '9,123 456,123"456, 123 456 ,strange numbers'
        result = [["9", "123 456", "123\"456", " 123 456 ", "strange numbers"]]
        self.assertEqual(parse_csv(record), result)

    def test_embedded_quotes(self):
        record = '10,abc",de"f,g"hi,embedded quotes'
        result = [["10", "abc\"", "de\"f", "g\"hi", "embedded quotes"]]
        self.assertEqual(parse_csv(record), result)

    def test_quoted_embedded_quotes(self):
        record = '11,"abc""","de""f","g""hi",quoted embedded quotes'
        result = [["11", "abc\"", "de\"f", "g\"hi", "quoted embedded quotes"]]
        self.assertEqual(parse_csv(record), result)

    def test_doubled_quotes(self):
        record = '12,"","" "",""x"",doubled quotes'
        result = [["12", "", " \"\"", "x\"\"", "doubled quotes"]]
        self.assertEqual(parse_csv(record), result)

    def test_strange_quotes(self):
        record = '13,"abc"def,abc"def","abc" "def",strange quotes'
        result = [["13", "abcdef", "abc\"def\"",
                   "abc \"def\"", "strange quotes"]]
        self.assertEqual(parse_csv(record), result)

    def test_empty_fields(self):
        record = '14,,"", ,empty fields'
        result = [["14", "", "", " ", "empty fields"]]
        self.assertEqual(parse_csv(record), result)

    def test_embedded_newline(self):
        record = '15,abc,"def\nghi",jkl,embedded newline'
        result = [["15", "abc", "def\nghi", "jkl", "embedded newline"]]
        self.assertEqual(parse_csv(record), result)

    def test_multiple_types_of_fields(self):
        record = '16,abc,"def",789,multiple types of fields'
        result = [["16", "abc", "def", "789", "multiple types of fields"]]
        self.assertEqual(parse_csv(record), result)

    def test_programming_praxis(self):
        "Verify the provided CSV example."
        records = parse_csv(programming_praxis_example)
        pipe_separated = "\n".join("|".join(field for field in rec)
                                   for rec in records)
        self.assertEqual(programming_praxis_solution, pipe_separated)


if __name__ == '__main__':
    unittest.main(verbosity=2)
