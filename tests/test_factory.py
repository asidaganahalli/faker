import io
import re
import string
import sys
import unittest

from collections import OrderedDict

import pytest

from faker import Faker, Generator
from faker.factory import Factory
from faker.generator import random
from faker.utils import decorators, text


class FactoryTestCase(unittest.TestCase):

    def setUp(self):
        self.generator = Generator()

    def test_documentor(self):
        from faker.cli import print_doc
        output = io.StringIO()
        print_doc(output=output)
        print_doc('address', output=output)
        print_doc('faker.providers.person.it_IT', output=output)
        assert output.getvalue()

    def test_command(self):
        from faker.cli import Command
        orig_stdout = sys.stdout
        try:
            sys.stdout = io.StringIO()
            command = Command(['faker', 'address'])
            command.execute()
            assert sys.stdout.getvalue()
        finally:
            sys.stdout = orig_stdout

    def test_command_custom_provider(self):
        from faker.cli import Command
        orig_stdout = sys.stdout
        try:
            sys.stdout = io.StringIO()
            command = Command(['faker', 'foo', '-i', 'tests.mymodule.en_US'])
            command.execute()
            assert sys.stdout.getvalue()
        finally:
            sys.stdout = orig_stdout

    def test_cli_seed(self):
        from faker.cli import Command
        orig_stdout = sys.stdout
        try:
            sys.stdout = io.StringIO()
            base_args = ['faker', 'address']
            target_args = ['--seed', '967']
            commands = [Command(base_args + target_args), Command(base_args + target_args)]
            cli_output = [None] * 2
            for i in range(2):
                commands[i].execute()
                cli_output[i] = sys.stdout.getvalue()
            cli_output[1] = cli_output[1][len(cli_output[0]):]
            assert cli_output[0][:10] == cli_output[1][:10]
        finally:
            sys.stdout = orig_stdout

    def test_cli_seed_with_repeat(self):
        from faker.cli import Command
        orig_stdout = sys.stdout
        try:
            sys.stdout = io.StringIO()
            base_args = ['faker', 'address', '-r', '3']
            target_args = ['--seed', '967']
            commands = [Command(base_args + target_args), Command(base_args + target_args)]
            cli_output = [None] * 2
            for i in range(2):
                commands[i].execute()
                cli_output[i] = sys.stdout.getvalue()
            cli_output[1] = cli_output[1][len(cli_output[0]):]
            assert cli_output[0] == cli_output[1]
        finally:
            sys.stdout = orig_stdout

    def test_cli_verbosity(self):
        from faker.cli import Command
        orig_stdout = sys.stdout
        try:
            sys.stdout = io.StringIO()
            base_args = ['faker', 'address', '--seed', '769']
            target_args = ['-v']
            commands = [Command(base_args), Command(base_args + target_args)]
            cli_output = [None] * 2
            for i in range(2):
                commands[i].execute()
                cli_output[i] = sys.stdout.getvalue()
            simple_output, verbose_output = cli_output
            assert simple_output != verbose_output
        finally:
            sys.stdout = orig_stdout

    def test_slugify(self):
        slug = text.slugify("a'b/c")
        assert slug == 'abc'

        slug = text.slugify("àeìöú")
        assert slug == 'aeiou'

        slug = text.slugify("àeì.öú")
        assert slug == 'aeiou'

        slug = text.slugify("àeì.öú", allow_dots=True)
        assert slug == 'aei.ou'

        slug = text.slugify("àeì.öú", allow_unicode=True)
        assert slug == 'àeìöú'

        slug = text.slugify("àeì.öú", allow_unicode=True, allow_dots=True)
        assert slug == 'àeì.öú'

        @decorators.slugify
        def fn(s):
            return s

        slug = fn("a'b/c")
        assert slug == 'abc'

        @decorators.slugify_domain
        def fn(s):
            return s

        slug = fn("a'b/.c")
        assert slug == 'ab.c'

        @decorators.slugify_unicode
        def fn(s):
            return s

        slug = fn("a'b/.cé")
        assert slug == 'abcé'

    def test_random_element(self):
        from faker.providers import BaseProvider
        provider = BaseProvider(self.generator)

        choices = ('a', 'b', 'c', 'd')
        pick = provider.random_element(choices)
        assert pick in choices

        # dicts not allowed because they introduce dependency on PYTHONHASHSEED
        with self.assertRaises(ValueError):
            provider.random_element({})

        choices = OrderedDict([('a', 5), ('b', 2), ('c', 2), ('d', 1)])
        pick = provider.random_element(choices)
        self.assertTrue(pick in choices)

        choices = OrderedDict([('a', 0.5), ('b', 0.2), ('c', 0.2), ('d', 0.1)])
        pick = provider.random_element(choices)
        self.assertTrue(pick in choices)

    def test_binary(self):
        from faker.providers.misc import Provider
        provider = Provider(self.generator)

        for _ in range(999):
            length = random.randint(0, 2 ** 10)
            binary = provider.binary(length)

            assert isinstance(binary, (bytes, bytearray))
            assert len(binary) == length

        for _ in range(999):
            self.generator.seed(_)
            binary1 = provider.binary(_)
            self.generator.seed(_)
            binary2 = provider.binary(_)

            assert binary1 == binary2

    def test_language_code(self):
        from faker.providers.misc import Provider
        provider = Provider(self.generator)

        for _ in range(99):
            language_code = provider.language_code()
            assert isinstance(language_code, str)
            assert re.match(r'^[a-z]{2,3}$', language_code)

    def test_locale(self):
        from faker.providers.misc import Provider
        provider = Provider(self.generator)

        for _ in range(99):
            locale = provider.locale()
            assert re.match(r'^[a-z]{2,3}_[A-Z]{2}$', locale)

    def test_password(self):
        from faker.providers.misc import Provider
        provider = Provider(self.generator)

        def in_string(char, _str):
            return char in _str

        for _ in range(999):
            password = provider.password()

            assert any(in_string(char, password) for char in "!@#$%^&*()_+")
            assert any(in_string(char, password) for char in string.digits)
            assert any(in_string(char, password) for char in string.ascii_uppercase)
            assert any(in_string(char, password) for char in string.ascii_lowercase)

        with pytest.raises(AssertionError):
            provider.password(length=2)

    def test_prefix_suffix_always_string(self):
        # Locales known to contain `*_male` and `*_female`.
        for locale in ("bg_BG", "dk_DK", "en", "ru_RU", "tr_TR"):
            fake = Faker(locale=locale)
            for x in range(20):  # Probabilistic testing.
                self.assertIsInstance(fake.prefix(), str)
                self.assertIsInstance(fake.suffix(), str)

    def test_no_words_sentence(self):
        from faker.providers.lorem import Provider

        provider = Provider(self.generator)

        paragraph = provider.paragraph(0)
        assert paragraph == ''

    def test_words_valueerror(self):
        fake = Faker()
        with pytest.raises(ValueError):
            fake.text(max_nb_chars=4)

    def test_no_words_paragraph(self):
        from faker.providers.lorem import Provider

        provider = Provider(self.generator)

        sentence = provider.sentence(0)
        assert sentence == ''

    def test_ext_word_list(self):
        fake = Faker()

        my_word_list = [
            'danish',
            'cheesecake',
            'sugar',
            'Lollipop',
            'wafer',
            'Gummies',
            'Jelly',
            'pie',
        ]
        word = fake.word(ext_word_list=my_word_list)
        assert word in my_word_list

    def test_no_words(self):
        fake = Faker()

        words = fake.words(0)
        assert words == []

    def test_some_words(self):
        fake = Faker()

        num_words = 5
        words = fake.words(num_words)
        assert isinstance(words, list)
        assert len(words) == num_words

        for word in words:
            assert isinstance(word, str)
            assert re.match(r'^[a-z].*$', word)

    def test_words_ext_word_list(self):
        fake = Faker()

        my_word_list = [
            'danish',
            'cheesecake',
            'sugar',
            'Lollipop',
            'wafer',
            'Gummies',
            'Jelly',
            'pie',
        ]

        num_words = 5
        words = fake.words(5, ext_word_list=my_word_list)
        assert isinstance(words, list)
        assert len(words) == num_words

        for word in words:
            assert isinstance(word, str)
            assert word in my_word_list

    def test_words_ext_word_list_unique(self):
        fake = Faker()

        my_word_list = [
            'danish',
            'cheesecake',
            'sugar',
            'Lollipop',
            'wafer',
            'Gummies',
            'Jelly',
            'pie',
        ]

        num_words = 5
        words = fake.words(5, ext_word_list=my_word_list, unique=True)
        assert isinstance(words, list)
        assert len(words) == num_words

        checked_words = []
        for word in words:
            assert isinstance(word, str)
            assert word in my_word_list
            # Check that word is unique
            assert word not in checked_words
            checked_words.append(word)

    def test_unique_words(self):
        fake = Faker()

        num_words = 20
        words = fake.words(num_words, unique=True)
        assert isinstance(words, list)
        assert len(words) == num_words

        checked_words = []
        for word in words:
            assert isinstance(word, str)
            # Check that word is only letters. No numbers, symbols, etc
            assert re.match(r'^[a-zA-Z].*$', word)
            # Check that word list is unique
            assert word not in checked_words
            checked_words.append(word)

    def test_texts_count(self):
        fake = Faker()

        texts_count = 5
        assert texts_count == len(fake.texts(nb_texts=texts_count))

    def test_texts_chars_count(self):
        fake = Faker()

        chars_count = 5
        for faker_text in fake.texts(max_nb_chars=chars_count):
            assert chars_count >= len(faker_text)

    def test_texts_word_list(self):
        fake = Faker()

        word_list = [
            'test',
            'faker',
        ]
        for faker_text in fake.texts(ext_word_list=word_list):
            for word in word_list:
                assert word in faker_text.lower()

    def test_random_pystr_characters(self):
        from faker.providers.python import Provider
        provider = Provider(self.generator)

        characters = provider.pystr()
        assert len(characters) == 20
        characters = provider.pystr(max_chars=255)
        assert len(characters) == 255
        characters = provider.pystr(max_chars=0)
        assert characters == ''
        characters = provider.pystr(max_chars=-10)
        assert characters == ''
        characters = provider.pystr(min_chars=10, max_chars=255)
        assert (len(characters) >= 10)

    def test_random_pyfloat(self):
        from faker.providers.python import Provider
        provider = Provider(self.generator)

        assert 0 <= abs(provider.pyfloat(left_digits=1)) < 10
        assert 0 <= abs(provider.pyfloat(left_digits=0)) < 1
        x = abs(provider.pyfloat(right_digits=0))
        assert x - int(x) == 0
        with pytest.raises(ValueError):
            provider.pyfloat(left_digits=0, right_digits=0)

    def test_pyfloat_in_range(self):
        # tests for https://github.com/joke2k/faker/issues/994
        fake = Faker()

        for i in range(20):
            for min_value, max_value in [
                (0, 1),
                (-1, 1),
                (None, -5),
                (-5, None),
                (None, 5),
                (5, None),
            ]:
                fake.seed_instance(i)
                result = fake.pyfloat(min_value=min_value, max_value=max_value)
                if min_value is not None:
                    assert result >= min_value
                if max_value is not None:
                    assert result <= max_value

    def test_negative_pyfloat(self):
        # tests for https://github.com/joke2k/faker/issues/813
        fake = Faker()
        fake.seed_instance(32167)
        assert any(fake.pyfloat(left_digits=0, positive=False) < 0 for _ in range(100))
        assert any(fake.pydecimal(left_digits=0, positive=False) < 0 for _ in range(100))

    def test_pyfloat_empty_range_error(self):
        # tests for https://github.com/joke2k/faker/issues/1048
        fake = Faker()
        fake.seed_instance(8038)
        assert fake.pyfloat(max_value=9999) < 9999

    def test_pyfloat_same_min_max(self):
        # tests for https://github.com/joke2k/faker/issues/1048
        fake = Faker()
        with pytest.raises(ValueError):
            assert fake.pyfloat(min_value=9999, max_value=9999)

    def test_us_ssn_valid(self):
        from faker.providers.ssn.en_US import Provider

        provider = Provider(self.generator)
        for i in range(1000):
            ssn = provider.ssn()
            assert len(ssn) == 11
            assert ssn[0] != '9'
            assert ssn[0:3] != '666'
            assert ssn[0:3] != '000'
            assert ssn[4:6] != '00'
            assert ssn[7:11] != '0000'

    def test_nl_BE_ssn_valid(self):
        fake = Faker('nl_BE')

        for i in range(1000):
            ssn = fake.ssn()
            assert len(ssn) == 11
            gen_seq = ssn[6:9]
            gen_chksum = ssn[9:11]
            gen_seq_as_int = int(gen_seq)
            gen_chksum_as_int = int(gen_chksum)
            # Check that the sequence nr is between 1 inclusive and 998 inclusive
            assert gen_seq_as_int > 0
            assert gen_seq_as_int <= 998

            # validate checksum calculation
            # Since the century is not part of ssn, try both below and above year 2000
            ssn_below = int(ssn[0:9])
            chksum_below = 97 - (ssn_below % 97)
            ssn_above = ssn_below + 2000000000
            chksum_above = 97 - (ssn_above % 97)
            results = [chksum_above, chksum_below]
            assert gen_chksum_as_int in results

    def test_random_sample_unique(self):
        from faker.providers import BaseProvider
        provider = BaseProvider(self.generator)

        # Too many items requested
        with self.assertRaises(ValueError):
            provider.random_sample('abcde', 6)

        # Same length
        sample = provider.random_sample('abcd', 4)
        assert sorted(sample) == list('abcd')

        sample = provider.random_sample('abcde', 5)
        assert sorted(sample) == list('abcde')

        # Length = 3
        sample = provider.random_sample('abcde', 3)
        assert len(sample) == 3
        assert set(sample).issubset(set('abcde'))

        # Length = 1
        sample = provider.random_sample('abcde', 1)
        assert len(sample) == 1
        assert set(sample).issubset(set('abcde'))

        # Length = 0
        sample = provider.random_sample('abcde', 0)
        assert sample == []

    def test_random_number(self):
        from faker.providers import BaseProvider
        provider = BaseProvider(self.generator)

        number = provider.random_number(10, True)
        assert len(str(number)) == 10

        # Digits parameter < 0
        with self.assertRaises(ValueError):
            number = provider.random_number(-1, True)

        # Digits parameter < 1 with fix_len=True
        with self.assertRaises(ValueError):
            number = provider.random_number(0, True)

    def test_instance_seed_chain(self):
        factory = Factory.create()

        names = ['Real Name0', 'Real Name1', 'Real Name2', 'Real Name0', 'Real Name2']
        anonymized = [factory.seed_instance(name).name() for name in names]
        assert anonymized[0] == anonymized[3]
        assert anonymized[2] == anonymized[4]


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
