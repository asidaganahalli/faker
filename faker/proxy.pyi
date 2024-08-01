import datetime

from collections import OrderedDict
from decimal import Decimal
from enum import Enum
from json import encoder
from typing import (
    Any,
    Callable,
    Collection,
    Dict,
    Iterable,
    Iterator,
    List,
    Literal,
    Optional,
    Sequence,
    Set,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)
from uuid import UUID

from faker.generator import Generator
from faker.providers import T
from faker.providers.python import TEnum
from faker.typing import *

class Faker:
    def address(self) -> str:
        """
        :example: '791 Crist Parks, Sashabury, IL 86039-9874'
        """
        ...
    def administrative_unit(self) -> str: ...
    def bothify(self, text: str = ..., letters: str = ...) -> str:
        """
        Generate a string with each placeholder in ``text`` replaced according to the following rules:

        - Number signs ('#') are replaced with a random digit (0 to 9).
        - Question marks ('?') are replaced with a random character from ``letters``.

        By default, ``letters`` contains all ASCII letters, uppercase and lowercase.

        Under the hood, this method uses :meth:`numerify() <faker.providers.BaseProvider.numerify>` and
        and :meth:`lexify() <faker.providers.BaseProvider.lexify>` to generate random values for number
        signs and question marks respectively.

        :sample: letters='ABCDE'
        :sample: text='Product Number: ????-########'
        :sample: text='Product Number: ????-########', letters='ABCDE'
        """
        ...
    def building_number(self) -> str:
        """
        :example: '791'
        """
        ...
    def city(self) -> str:
        """
        :example: 'Sashabury'
        """
        ...
    def city_prefix(self) -> str: ...
    def city_suffix(self) -> str:
        """
        :example: 'town'
        """
        ...
    def country(self) -> str: ...
    def country_code(self, representation: str = ...) -> str: ...
    def current_country(self) -> str: ...
    def current_country_code(self) -> str: ...
    def hexify(self, text: str = ..., upper: bool = ...) -> str:
        """
        Generate a string with each circumflex ('^') in ``text``
        replaced with a random hexadecimal character.

        By default, ``upper`` is set to False. If set to ``True``, output
        will be formatted using uppercase hexadecimal characters.

        :sample: text='MAC Address: ^^:^^:^^:^^:^^:^^'
        :sample: text='MAC Address: ^^:^^:^^:^^:^^:^^', upper=True
        """
        ...
    def language_code(self) -> str:
        """
        Generate a random i18n language code (e.g. en).
        """
        ...
    def lexify(self, text: str = ..., letters: str = ...) -> str:
        """
        Generate a string with each question mark ('?') in ``text``
        replaced with a random character from ``letters``.

        By default, ``letters`` contains all ASCII letters, uppercase and lowercase.

        :sample: text='Random Identifier: ??????????'
        :sample: text='Random Identifier: ??????????', letters='ABCDE'
        """
        ...
    def locale(self) -> str:
        """
        Generate a random underscored i18n locale code (e.g. en_US).
        """
        ...
    def military_apo(self) -> str:
        """
        :example: 'PSC 5394 Box 3492
        """
        ...
    def military_dpo(self) -> str:
        """
        :example: 'Unit 3333 Box 9342'
        """
        ...
    def military_ship(self) -> str:
        """
        :example: 'USS'
        """
        ...
    def military_state(self) -> str:
        """
        :example: 'APO'
        """
        ...
    def numerify(self, text: str = ...) -> str:
        """
        Generate a string with each placeholder in ``text`` replaced according
        to the following rules:

        - Number signs ('#') are replaced with a random digit (0 to 9).
        - Percent signs ('%') are replaced with a random non-zero digit (1 to 9).
        - Dollar signs ('$') are replaced with a random digit above two (2 to 9).
        - Exclamation marks ('!') are replaced with a random digit or an empty string.
        - At symbols ('@') are replaced with a random non-zero digit or an empty string.

        Under the hood, this method uses :meth:`random_digit() <faker.providers.BaseProvider.random_digit>`,
        :meth:`random_digit_not_null() <faker.providers.BaseProvider.random_digit_not_null>`,
        :meth:`random_digit_or_empty() <faker.providers.BaseProvider.random_digit_or_empty>`,
        and :meth:`random_digit_not_null_or_empty() <faker.providers.BaseProvider.random_digit_not_null_or_empty>`
        to generate the random values.

        :sample: text='Intel Core i%-%%##K vs AMD Ryzen % %%##X'
        :sample: text='!!! !!@ !@! !@@ @!! @!@ @@! @@@'
        """
        ...
    def postalcode(self) -> str: ...
    def postalcode_in_state(self, state_abbr: Optional[str] = ...) -> str: ...
    def postalcode_plus4(self) -> str: ...
    def postcode(self) -> str:
        """
        :example: 86039-9874
        """
        ...
    def postcode_in_state(self, state_abbr: Optional[str] = ...) -> str:
        """
        :returns: A random postcode within the provided state abbreviation

        :param state_abbr: A state abbreviation
        """
        ...
    def random_choices(
        self, elements: Union[Collection[str], Collection[T], OrderedDict[T, float]] = ..., length: Optional[int] = ...
    ) -> Sequence[T]:
        """
        Generate a list of objects randomly sampled from ``elements`` with replacement.

        For information on the ``elements`` and ``length`` arguments, please refer to
        :meth:`random_elements() <faker.providers.BaseProvider.random_elements>` which
        is used under the hood with the ``unique`` argument explicitly set to ``False``.

        :sample: elements=('a', 'b', 'c', 'd')
        :sample: elements=('a', 'b', 'c', 'd'), length=10
        :sample: elements=OrderedDict([
                     ("a", 0.45),
                     ("b", 0.35),
                     ("c", 0.15),
                     ("d", 0.05),
                 ])
        :sample: elements=OrderedDict([
                     ("a", 0.45),
                     ("b", 0.35),
                     ("c", 0.15),
                     ("d", 0.05),
                 ]), length=20
        """
        ...
    def random_digit(self) -> int:
        """
        Generate a random digit (0 to 9).
        """
        ...
    def random_digit_above_two(self) -> int:
        """
        Generate a random digit above value two (2 to 9).
        """
        ...
    def random_digit_not_null(self) -> int:
        """
        Generate a random non-zero digit (1 to 9).
        """
        ...
    def random_digit_not_null_or_empty(self) -> Union[int, str]:
        """
        Generate a random non-zero digit (1 to 9) or an empty string.

        This method will return an empty string 50% of the time,
        and each digit has a 1/18 chance of being generated.
        """
        ...
    def random_digit_or_empty(self) -> Union[int, str]:
        """
        Generate a random digit (0 to 9) or an empty string.

        This method will return an empty string 50% of the time,
        and each digit has a 1/20 chance of being generated.
        """
        ...
    def random_element(self, elements: Union[Collection[str], Collection[T], OrderedDict[T, float]] = ...) -> T:
        """
        Generate a randomly sampled object from ``elements``.

        For information on the ``elements`` argument, please refer to
        :meth:`random_elements() <faker.providers.BaseProvider.random_elements>` which
        is used under the hood with the ``unique`` argument set to ``False`` and the
        ``length`` argument set to ``1``.

        :sample: elements=('a', 'b', 'c', 'd')
        :sample size=10: elements=OrderedDict([
                     ("a", 0.45),
                     ("b", 0.35),
                     ("c", 0.15),
                     ("d", 0.05),
                 ])
        """
        ...
    def random_elements(
        self,
        elements: Union[Collection[str], Collection[T], OrderedDict[T, float]] = ...,
        length: Optional[int] = ...,
        unique: bool = ...,
        use_weighting: Optional[bool] = ...,
    ) -> Sequence[T]:
        """
        Generate a list of randomly sampled objects from ``elements``.

        Set ``unique`` to ``False`` for random sampling with replacement, and set ``unique`` to
        ``True`` for random sampling without replacement.

        If ``length`` is set to ``None`` or is omitted, ``length`` will be set to a random
        integer from 1 to the size of ``elements``.

        The value of ``length`` cannot be greater than the number of objects
        in ``elements`` if ``unique`` is set to ``True``.

        The value of ``elements`` can be any sequence type (``list``, ``tuple``, ``set``,
        ``string``, etc) or an ``OrderedDict`` type. If it is the latter, the keys will be
        used as the objects for sampling, and the values will be used as weighted probabilities
        if ``unique`` is set to ``False``. For example:

        .. code-block:: python

            # Random sampling with replacement
            fake.random_elements(
                elements=OrderedDict([
                    ("variable_1", 0.5),        # Generates "variable_1" 50% of the time
                    ("variable_2", 0.2),        # Generates "variable_2" 20% of the time
                    ("variable_3", 0.2),        # Generates "variable_3" 20% of the time
                    ("variable_4": 0.1),        # Generates "variable_4" 10% of the time
                ]), unique=False
            )

            # Random sampling without replacement (defaults to uniform distribution)
            fake.random_elements(
                elements=OrderedDict([
                    ("variable_1", 0.5),
                    ("variable_2", 0.2),
                    ("variable_3", 0.2),
                    ("variable_4": 0.1),
                ]), unique=True
            )

        :sample: elements=('a', 'b', 'c', 'd'), unique=False
        :sample: elements=('a', 'b', 'c', 'd'), unique=True
        :sample: elements=('a', 'b', 'c', 'd'), length=10, unique=False
        :sample: elements=('a', 'b', 'c', 'd'), length=4, unique=True
        :sample: elements=OrderedDict([
                        ("a", 0.45),
                        ("b", 0.35),
                       ("c", 0.15),
                       ("d", 0.05),
                   ]), length=20, unique=False
        :sample: elements=OrderedDict([
                       ("a", 0.45),
                       ("b", 0.35),
                       ("c", 0.15),
                       ("d", 0.05),
                   ]), unique=True
        """
        ...
    def random_int(self, min: int = ..., max: int = ..., step: int = ...) -> int:
        """
        Generate a random integer between two integers ``min`` and ``max`` inclusive
        while observing the provided ``step`` value.

        This method is functionally equivalent to randomly sampling an integer
        from the sequence ``range(min, max + 1, step)``.

        :sample: min=0, max=15
        :sample: min=0, max=15, step=3
        """
        ...
    def random_letter(self) -> str:
        """
        Generate a random ASCII letter (a-z and A-Z).
        """
        ...
    def random_letters(self, length: int = ...) -> Sequence[str]:
        """
        Generate a list of random ASCII letters (a-z and A-Z) of the specified ``length``.

        :sample: length=10
        """
        ...
    def random_lowercase_letter(self) -> str:
        """
        Generate a random lowercase ASCII letter (a-z).
        """
        ...
    def random_number(self, digits: Optional[int] = ..., fix_len: bool = ...) -> int:
        """
        Generate a random integer according to the following rules:

        - If ``digits`` is ``None`` (default), its value will be set to a random
          integer from 1 to 9.
        - If ``fix_len`` is ``False`` (default), all integers that do not exceed
          the number of ``digits`` can be generated.
        - If ``fix_len`` is ``True``, only integers with the exact number of
          ``digits`` can be generated.

        :sample: fix_len=False
        :sample: fix_len=True
        :sample: digits=3
        :sample: digits=3, fix_len=False
        :sample: digits=3, fix_len=True
        """
        ...
    def random_sample(
        self, elements: Union[Collection[str], Collection[T], OrderedDict[T, float]] = ..., length: Optional[int] = ...
    ) -> Sequence[T]:
        """
        Generate a list of objects randomly sampled from ``elements`` without replacement.

        For information on the ``elements`` and ``length`` arguments, please refer to
        :meth:`random_elements() <faker.providers.BaseProvider.random_elements>` which
        is used under the hood with the ``unique`` argument explicitly set to ``True``.

        :sample: elements=('a', 'b', 'c', 'd', 'e', 'f')
        :sample: elements=('a', 'b', 'c', 'd', 'e', 'f'), length=3
        """
        ...
    def random_uppercase_letter(self) -> str:
        """
        Generate a random uppercase ASCII letter (A-Z).
        """
        ...
    def randomize_nb_elements(
        self, number: int = ..., le: bool = ..., ge: bool = ..., min: Optional[int] = ..., max: Optional[int] = ...
    ) -> int:
        """
        Generate a random integer near ``number`` according to the following rules:

        - If ``le`` is ``False`` (default), allow generation up to 140% of ``number``.
          If ``True``, upper bound generation is capped at 100%.
        - If ``ge`` is ``False`` (default), allow generation down to 60% of ``number``.
          If ``True``, lower bound generation is capped at 100%.
        - If a numerical value for ``min`` is provided, generated values less than ``min``
          will be clamped at ``min``.
        - If a numerical value for ``max`` is provided, generated values greater than
          ``max`` will be clamped at ``max``.
        - If both ``le`` and ``ge`` are ``True``, the value of ``number`` will automatically
          be returned, regardless of the values supplied for ``min`` and ``max``.

        :sample: number=100
        :sample: number=100, ge=True
        :sample: number=100, ge=True, min=120
        :sample: number=100, le=True
        :sample: number=100, le=True, max=80
        :sample: number=79, le=True, ge=True, min=80
        """
        ...
    def secondary_address(self) -> str: ...
    def state(self) -> str: ...
    def state_abbr(self, include_territories: bool = ..., include_freely_associated_states: bool = ...) -> str:
        """
        :returns: A random two-letter USPS postal code

        By default, the resulting code may abbreviate any of the fifty states,
        five US territories, or three freely-associating sovereign states.

        :param include_territories: If True, territories will be included.
            If False, US territories will be excluded.
        :param include_freely_associated_states: If True, freely-associated states will be included.
            If False, sovereign states in free association with the US will be excluded.
        """
        ...
    def street_address(self) -> str:
        """
        :example: '791 Crist Parks'
        """
        ...
    def street_name(self) -> str:
        """
        :example: 'Crist Parks'
        """
        ...
    def street_suffix(self) -> str:
        """
        :example: 'Avenue'
        """
        ...
    def zipcode(self) -> str: ...
    def zipcode_in_state(self, state_abbr: Optional[str] = ...) -> str: ...
    def zipcode_plus4(self) -> str: ...
    def license_plate(self) -> str:
        """
        Generate a license plate.
        """
        ...
    def vin(self) -> str:
        """
        Generate vin number.
        """
        ...
    def aba(self) -> str:
        """
        Generate an ABA routing transit number.
        """
        ...
    def bank_country(self) -> str:
        """
        Generate the bank provider's ISO 3166-1 alpha-2 country code.
        """
        ...
    def bban(self) -> str:
        """
        Generate a Basic Bank Account Number (BBAN).
        """
        ...
    def iban(self) -> str:
        """
        Generate an International Bank Account Number (IBAN).
        """
        ...
    def swift(self, length: Optional[int] = ..., primary: bool = ..., use_dataset: bool = ...) -> str:
        """
        Generate a SWIFT code.

        SWIFT codes, reading from left to right, are composed of a 4 alphabet
        character bank code, a 2 alphabet character country code, a 2
        alphanumeric location code, and an optional 3 alphanumeric branch code.
        This means SWIFT codes can only have 8 or 11 characters, so the value of
        ``length`` can only be ``None`` or the integers ``8`` or ``11``. If the
        value is ``None``, then a value of ``8`` or ``11`` will randomly be
        assigned.

        Because all 8-digit SWIFT codes already refer to the primary branch or
        office, the ``primary`` argument only has an effect if the value of
        ``length`` is ``11``. If ``primary`` is ``True`` and ``length`` is
        ``11``, the 11-digit SWIFT codes generated will always end in ``'XXX'``
        to denote that they belong to primary branches/offices.

        For extra authenticity, localized providers may opt to include SWIFT
        bank codes, location codes, and branch codes used in their respective
        locales. If ``use_dataset`` is ``True``, this method will generate SWIFT
        codes based on those locale-specific codes if included. If those codes
        were not included, then it will behave as if ``use_dataset`` were
        ``False``, and in that mode, all those codes will just be randomly
        generated as per the specification.

        :sample:
        :sample: length=8
        :sample: length=8, use_dataset=True
        :sample: length=11
        :sample: length=11, primary=True
        :sample: length=11, use_dataset=True
        :sample: length=11, primary=True, use_dataset=True
        """
        ...
    def swift11(self, primary: bool = ..., use_dataset: bool = ...) -> str:
        """
        Generate an 11-digit SWIFT code.

        This method uses |swift| under the hood with the ``length`` argument set
        to ``11``. If ``primary`` is set to ``True``, the SWIFT code will always
        end with ``'XXX'``. All 11-digit SWIFT codes use this convention to
        refer to the primary branch/office.

        :sample:
        :sample: use_dataset=True
        """
        ...
    def swift8(self, use_dataset: bool = ...) -> str:
        """
        Generate an 8-digit SWIFT code.

        This method uses |swift| under the hood with the ``length`` argument set
        to ``8`` and with the ``primary`` argument omitted. All 8-digit SWIFT
        codes already refer to the primary branch/office.

        :sample:
        :sample: use_dataset=True
        """
        ...
    def ean(self, length: int = ..., prefixes: Tuple[Union[int, str, Tuple[Union[int, str], ...]], ...] = ...) -> str:
        """
        Generate an EAN barcode of the specified ``length``.

        The value of ``length`` can only be ``8`` or ``13`` (default) which will
        create an EAN-8 or an EAN-13 barcode respectively.

        If a value for ``prefixes`` is specified, the result will begin with one
        of the sequences in ``prefixes``.

        :sample: length=13
        :sample: length=8
        :sample: prefixes=('00',)
        :sample: prefixes=('45', '49')
        """
        ...
    def ean13(
        self,
        prefixes: Tuple[Union[int, str, Tuple[Union[int, str], ...]], ...] = ...,
        leading_zero: Optional[bool] = ...,
    ) -> str:
        """
        Generate an EAN-13 barcode.

        If ``leading_zero`` is ``True``, the leftmost digit of the barcode will
        be set to ``0``. If ``False``, the leftmost digit cannot be ``0``. If
        ``None`` (default), the leftmost digit can be any digit.

        If a value for ``prefixes`` is specified, the result will begin with one
        of the sequences in ``prefixes`` and will ignore ``leading_zero``.

        This method uses the standard barcode provider's |ean13| under the
        hood with the ``prefixes`` argument set to the correct value to attain
        the behavior described above.

        .. note::
           EAN-13 barcode that starts with a zero can be converted to UPC-A
           by dropping the leading zero. This may cause problems with readers
           that treat all of these code as UPC-A codes and drop the first digit
           when reading it.

           You can set the argument ``prefixes`` ( or ``leading_zero`` for
           convenience) explicitly to avoid or to force the generated barcode to
           start with a zero. You can also generate actual UPC-A barcode with
           |EnUsBarcodeProvider.upc_a|.

        :sample:
        :sample: leading_zero=False
        :sample: leading_zero=True
        :sample: prefixes=('00',)
        :sample: prefixes=('45', '49')
        """
        ...
    def ean8(self, prefixes: Tuple[Union[int, str, Tuple[Union[int, str], ...]], ...] = ...) -> str:
        """
        Generate an EAN-8 barcode.

        This method uses |ean| under the hood with the ``length`` argument
        explicitly set to ``8``.

        If a value for ``prefixes`` is specified, the result will begin with one
        of the sequences in ``prefixes``.

        :sample:
        :sample: prefixes=('00',)
        :sample: prefixes=('45', '49')
        """
        ...
    def localized_ean(self, length: int = ...) -> str:
        """
        Generate a localized EAN barcode of the specified ``length``.

        The value of ``length`` can only be ``8`` or ``13`` (default) which will
        create an EAN-8 or an EAN-13 barcode respectively.

        This method uses the standard barcode provider's |ean| under the hood
        with the ``prefixes`` argument explicitly set to ``local_prefixes`` of
        a localized barcode provider implementation.

        :sample:
        :sample: length=13
        :sample: length=8
        """
        ...
    def localized_ean13(self) -> str:
        """
        Generate a localized EAN-13 barcode.

        This method uses |localized_ean| under the hood with the ``length``
        argument explicitly set to ``13``.
        """
        ...
    def localized_ean8(self) -> str:
        """
        Generate a localized EAN-8 barcode.

        This method uses |localized_ean| under the hood with the ``length``
        argument explicitly set to ``8``.
        """
        ...
    def upc_a(
        self, upc_ae_mode: bool = ..., base: Optional[str] = ..., number_system_digit: Optional[int] = ...
    ) -> str:
        """
        Generate a 12-digit UPC-A barcode.

        The value of ``upc_ae_mode`` controls how barcodes will be generated. If
        ``False`` (default), barcodes are not guaranteed to have a UPC-E
        equivalent. In this mode, the method uses |EnUsBarcodeProvider.ean13|
        under the hood, and the values of ``base`` and ``number_system_digit``
        will be ignored.

        If ``upc_ae_mode`` is ``True``, the resulting barcodes are guaranteed to
        have a UPC-E equivalent, and the values of ``base`` and
        ``number_system_digit`` will be used to control what is generated.

        Under this mode, ``base`` is expected to have a 6-digit string value. If
        any other value is supplied, a random 6-digit string will be used
        instead. As for ``number_system_digit``, the expected value is a ``0``
        or a ``1``. If any other value is provided, this method will randomly
        choose from the two.

        .. important::
           When ``upc_ae_mode`` is enabled, you might encounter instances where
           different values of ``base`` (e.g. ``'120003'`` and ``'120004'``)
           produce the same UPC-A barcode. This is normal, and the reason lies
           within the whole conversion process. To learn more about this and
           what ``base`` and ``number_system_digit`` actually represent, please
           refer to |EnUsBarcodeProvider.upc_e|.

        :sample:
        :sample: upc_ae_mode=True, number_system_digit=0
        :sample: upc_ae_mode=True, number_system_digit=1
        :sample: upc_ae_mode=True, base='123456', number_system_digit=0
        :sample: upc_ae_mode=True, base='120003', number_system_digit=0
        :sample: upc_ae_mode=True, base='120004', number_system_digit=0
        """
        ...
    def upc_e(self, base: Optional[str] = ..., number_system_digit: Optional[int] = ..., safe_mode: bool = ...) -> str:
        """
        Generate an 8-digit UPC-E barcode.

        UPC-E barcodes can be expressed in 6, 7, or 8-digit formats, but this
        method uses the 8 digit format, since it is trivial to convert to the
        other two formats. The first digit (starting from the left) is
        controlled by ``number_system_digit``, and it can only be a ``0`` or a
        ``1``. The last digit is the check digit that is inherited from the
        UPC-E barcode's UPC-A equivalent. The middle six digits are collectively
        referred to as the ``base`` (for a lack of a better term).

        On that note, this method uses ``base`` and ``number_system_digit`` to
        first generate a UPC-A barcode for the check digit, and what happens
        next depends on the value of ``safe_mode``. The argument ``safe_mode``
        exists, because there are some UPC-E values that share the same UPC-A
        equivalent. For example, any UPC-E barcode of the form ``abc0000d``,
        ``abc0003d``, and ``abc0004d`` share the same UPC-A value
        ``abc00000000d``, but that UPC-A value will only convert to ``abc0000d``
        because of (a) how UPC-E is just a zero-suppressed version of UPC-A and
        (b) the rules around the conversion.

        If ``safe_mode`` is ``True`` (default), this method performs another set
        of conversions to guarantee that the UPC-E barcodes generated can be
        converted to UPC-A, and that UPC-A barcode can be converted back to the
        original UPC-E barcode. Using the example above, even if the bases
        ``120003`` or ``120004`` are used, the resulting UPC-E barcode will
        always use the base ``120000``.

        If ``safe_mode`` is ``False``, then the ``number_system_digit``,
        ``base``, and the computed check digit will just be concatenated
        together to produce the UPC-E barcode, and attempting to convert the
        barcode to UPC-A and back again to UPC-E will exhibit the behavior
        described above.

        :sample:
        :sample: base='123456'
        :sample: base='123456', number_system_digit=0
        :sample: base='123456', number_system_digit=1
        :sample: base='120000', number_system_digit=0
        :sample: base='120003', number_system_digit=0
        :sample: base='120004', number_system_digit=0
        :sample: base='120000', number_system_digit=0, safe_mode=False
        :sample: base='120003', number_system_digit=0, safe_mode=False
        :sample: base='120004', number_system_digit=0, safe_mode=False
        """
        ...
    def color(
        self,
        hue: Union[str, float, int, Sequence[int], None] = ...,
        luminosity: Optional[str] = ...,
        color_format: str = ...,
    ) -> str:
        """
        Generate a color in a human-friendly way.

        Under the hood, this method first creates a color represented in the HSV
        color model and then converts it to the desired ``color_format``. The
        argument ``hue`` controls the H value according to the following
        rules:

        - If the value is a number from ``0`` to ``360``, it will serve as the H
          value of the generated color.
        - If the value is a tuple/list of 2 numbers from 0 to 360, the color's H
          value will be randomly selected from that range.
        - If the value is a valid string, the color's H value will be randomly
          selected from the H range corresponding to the supplied string. Valid
          values are ``'monochrome'``, ``'red'``, ``'orange'``, ``'yellow'``,
          ``'green'``, ``'blue'``, ``'purple'``, and ``'pink'``.

        The argument ``luminosity`` influences both S and V values and is
        partially affected by ``hue`` as well. The finer details of this
        relationship are somewhat involved, so please refer to the source code
        instead if you wish to dig deeper. To keep the interface simple, this
        argument either can be omitted or can accept the following string
        values:``'bright'``, ``'dark'``, ``'light'``, or ``'random'``.

        The argument ``color_format`` controls in which color model the color is
        represented. Valid values are ``'hsv'``, ``'hsl'``, ``'rgb'``, or
        ``'hex'`` (default).

        :sample: hue='red'
        :sample: luminosity='light'
        :sample: hue=(100, 200), color_format='rgb'
        :sample: hue='orange', luminosity='bright'
        :sample: hue=135, luminosity='dark', color_format='hsv'
        :sample: hue=(300, 20), luminosity='random', color_format='hsl'
        """
        ...
    def color_hsl(
        self, hue: Union[str, float, int, Sequence[int], None] = ..., luminosity: Optional[str] = ...
    ) -> Tuple[int, int, int]:
        """
        Generate a HSL color tuple in a human-friendly way.
        """
        ...
    def color_hsv(
        self, hue: Union[str, float, int, Sequence[int], None] = ..., luminosity: Optional[str] = ...
    ) -> Tuple[int, int, int]:
        """
        Generate a HSV color tuple in a human-friendly way.
        """
        ...
    def color_name(self) -> str:
        """
        Generate a color name.
        """
        ...
    def color_rgb(
        self, hue: Union[str, float, int, Sequence[int], None] = ..., luminosity: Optional[str] = ...
    ) -> Tuple[int, int, int]:
        """
        Generate a RGB color tuple of integers in a human-friendly way.
        """
        ...
    def color_rgb_float(
        self, hue: Union[str, float, int, Sequence[int], None] = ..., luminosity: Optional[str] = ...
    ) -> Tuple[float, float, float]:
        """
        Generate a RGB color tuple of floats in a human-friendly way.
        """
        ...
    def hex_color(self) -> str:
        """
        Generate a color formatted as a hex triplet.
        """
        ...
    def rgb_color(self) -> str:
        """
        Generate a color formatted as a comma-separated RGB value.
        """
        ...
    def rgb_css_color(self) -> str:
        """
        Generate a color formatted as a CSS rgb() function.
        """
        ...
    def safe_color_name(self) -> str:
        """
        Generate a web-safe color name.
        """
        ...
    def safe_hex_color(self) -> str:
        """
        Generate a web-safe color formatted as a hex triplet.
        """
        ...
    def bs(self) -> str:
        """
        :example: 'integrate extensible convergence'
        """
        ...
    def catch_phrase(self) -> str:
        """
        :example: 'Robust full-range hub'
        """
        ...
    def company(self) -> str:
        """
        :example: 'Acme Ltd'
        """
        ...
    def company_suffix(self) -> str:
        """
        :example: 'Ltd'
        """
        ...
    def credit_card_expire(
        self,
        start: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int] = ...,
        end: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int] = ...,
        date_format: str = ...,
    ) -> str:
        """
        Generate a credit card expiry date.

        This method uses |date_time_between| under the hood to generate the
        expiry date, so the ``start`` and ``end`` arguments work in the same way
        here as it would in that method. For the actual formatting of the expiry
        date, |strftime| is used and ``date_format`` is simply passed
        to that method.
        """
        ...
    def credit_card_full(self, card_type: Optional[CardType] = ...) -> str:
        """
        Generate a set of credit card details.
        """
        ...
    def credit_card_number(self, card_type: Optional[CardType] = ...) -> str:
        """
        Generate a valid credit card number.
        """
        ...
    def credit_card_provider(self, card_type: Optional[CardType] = ...) -> str:
        """
        Generate a credit card provider name.
        """
        ...
    def credit_card_security_code(self, card_type: Optional[CardType] = ...) -> str:
        """
        Generate a credit card security code.
        """
        ...
    def cryptocurrency(self) -> Tuple[str, str]: ...
    def cryptocurrency_code(self) -> str: ...
    def cryptocurrency_name(self) -> str: ...
    def currency(self) -> Tuple[str, str]: ...
    def currency_code(self) -> str: ...
    def currency_name(self) -> str: ...
    def currency_symbol(self, code: Optional[str] = ...) -> str:
        """
        :example: $
        """
        ...
    def pricetag(self) -> str: ...
    def am_pm(self) -> str: ...
    def century(self) -> str:
        """
        :example: 'XVII'
        """
        ...
    def date(
        self,
        pattern: str = ...,
        end_datetime: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int, None] = ...,
    ) -> str:
        """
        Get a date string between January 1, 1970 and now.

        :param pattern: Format of the date (year-month-day by default)
        :example: '2008-11-27'
        :return: Date
        """
        ...
    def date_between(
        self,
        start_date: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int] = ...,
        end_date: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int] = ...,
    ) -> datetime.date:
        """
        Get a Date object based on a random date between two given dates.
        Accepts date strings that can be recognized by strtotime().

        :param start_date: Defaults to 30 years ago
        :param end_date: Defaults to "today"
        :example: Date('1999-02-02')
        :return: Date
        """
        ...
    def date_between_dates(
        self,
        date_start: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int, None] = ...,
        date_end: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int, None] = ...,
    ) -> datetime.date:
        """
        Takes two Date objects and returns a random date between the two given dates.
        Accepts Date or datetime objects

        :param date_start: Date
        :param date_end: Date
        :return: Date
        """
        ...
    def date_object(self, end_datetime: Optional[datetime.datetime] = ...) -> datetime.date:
        """
        Get a date object between January 1, 1970 and now

        :example: datetime.date(2016, 9, 20)
        """
        ...
    def date_of_birth(
        self, tzinfo: Optional[datetime.tzinfo] = ..., minimum_age: int = ..., maximum_age: int = ...
    ) -> datetime.date:
        """
        Generate a random date of birth represented as a Date object,
        constrained by optional miminimum_age and maximum_age
        parameters.

        :param tzinfo: Defaults to None.
        :param minimum_age: Defaults to 0.
        :param maximum_age: Defaults to 115.

        :example: Date('1979-02-02')
        :return: Date
        """
        ...
    def date_this_century(self, before_today: bool = ..., after_today: bool = ...) -> datetime.date:
        """
        Gets a Date object for the current century.

        :param before_today: include days in current century before today
        :param after_today: include days in current century after today
        :example: Date('2012-04-04')
        :return: Date
        """
        ...
    def date_this_decade(self, before_today: bool = ..., after_today: bool = ...) -> datetime.date:
        """
        Gets a Date object for the decade year.

        :param before_today: include days in current decade before today
        :param after_today: include days in current decade after today
        :example: Date('2012-04-04')
        :return: Date
        """
        ...
    def date_this_month(self, before_today: bool = ..., after_today: bool = ...) -> datetime.date:
        """
        Gets a Date object for the current month.

        :param before_today: include days in current month before today
        :param after_today: include days in current month after today
        :example: dtdate('2012-04-04')
        :return: dtdate
        """
        ...
    def date_this_year(self, before_today: bool = ..., after_today: bool = ...) -> datetime.date:
        """
        Gets a Date object for the current year.

        :param before_today: include days in current year before today
        :param after_today: include days in current year after today
        :example: Date('2012-04-04')
        :return: Date
        """
        ...
    def date_time(
        self,
        tzinfo: Optional[datetime.tzinfo] = ...,
        end_datetime: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int, None] = ...,
    ) -> datetime.datetime:
        """
        Get a datetime object for a date between January 1, 1970 and now

        :param tzinfo: timezone, instance of datetime.tzinfo subclass
        :example: datetime('2005-08-16 20:39:21')
        :return: datetime
        """
        ...
    def date_time_ad(
        self,
        tzinfo: Optional[datetime.tzinfo] = ...,
        end_datetime: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int, None] = ...,
        start_datetime: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int, None] = ...,
    ) -> datetime.datetime:
        """
        Get a datetime object for a date between January 1, 001 and now

        :param tzinfo: timezone, instance of datetime.tzinfo subclass
        :example: datetime('1265-03-22 21:15:52')
        :return: datetime
        """
        ...
    def date_time_between(
        self,
        start_date: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int] = ...,
        end_date: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int] = ...,
        tzinfo: Optional[datetime.tzinfo] = ...,
    ) -> datetime.datetime:
        """
        Get a datetime object based on a random date between two given dates.
        Accepts date strings that can be recognized by strtotime().

        :param start_date: Defaults to 30 years ago
        :param end_date: Defaults to "now"
        :param tzinfo: timezone, instance of datetime.tzinfo subclass
        :example: datetime('1999-02-02 11:42:52')
        :return: datetime
        """
        ...
    def date_time_between_dates(
        self,
        datetime_start: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int, None] = ...,
        datetime_end: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int, None] = ...,
        tzinfo: Optional[datetime.tzinfo] = ...,
    ) -> datetime.datetime:
        """
        Takes two datetime objects and returns a random datetime between the two
        given datetimes.
        Accepts datetime objects.

        :param datetime_start: datetime
        :param datetime_end: datetime
        :param tzinfo: timezone, instance of datetime.tzinfo subclass
        :example: datetime('1999-02-02 11:42:52')
        :return: datetime
        """
        ...
    def date_time_this_century(
        self, before_now: bool = ..., after_now: bool = ..., tzinfo: Optional[datetime.tzinfo] = ...
    ) -> datetime.datetime:
        """
        Gets a datetime object for the current century.

        :param before_now: include days in current century before today
        :param after_now: include days in current century after today
        :param tzinfo: timezone, instance of datetime.tzinfo subclass
        :example: datetime('2012-04-04 11:02:02')
        :return: datetime
        """
        ...
    def date_time_this_decade(
        self, before_now: bool = ..., after_now: bool = ..., tzinfo: Optional[datetime.tzinfo] = ...
    ) -> datetime.datetime:
        """
        Gets a datetime object for the decade year.

        :param before_now: include days in current decade before today
        :param after_now: include days in current decade after today
        :param tzinfo: timezone, instance of datetime.tzinfo subclass
        :example: datetime('2012-04-04 11:02:02')
        :return: datetime
        """
        ...
    def date_time_this_month(
        self, before_now: bool = ..., after_now: bool = ..., tzinfo: Optional[datetime.tzinfo] = ...
    ) -> datetime.datetime:
        """
        Gets a datetime object for the current month.

        :param before_now: include days in current month before today
        :param after_now: include days in current month after today
        :param tzinfo: timezone, instance of datetime.tzinfo subclass
        :example: datetime('2012-04-04 11:02:02')
        :return: datetime
        """
        ...
    def date_time_this_year(
        self, before_now: bool = ..., after_now: bool = ..., tzinfo: Optional[datetime.tzinfo] = ...
    ) -> datetime.datetime:
        """
        Gets a datetime object for the current year.

        :param before_now: include days in current year before today
        :param after_now: include days in current year after today
        :param tzinfo: timezone, instance of datetime.tzinfo subclass
        :example: datetime('2012-04-04 11:02:02')
        :return: datetime
        """
        ...
    def day_of_month(self) -> str: ...
    def day_of_week(self) -> str: ...
    def future_date(
        self,
        end_date: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int] = ...,
        tzinfo: Optional[datetime.tzinfo] = ...,
    ) -> datetime.date:
        """
        Get a Date object based on a random date between 1 day from now and a
        given date.
        Accepts date strings that can be recognized by strtotime().

        :param end_date: Defaults to "+30d"
        :param tzinfo: timezone, instance of datetime.tzinfo subclass
        :example: dtdate('2030-01-01')
        :return: dtdate
        """
        ...
    def future_datetime(
        self,
        end_date: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int] = ...,
        tzinfo: Optional[datetime.tzinfo] = ...,
    ) -> datetime.datetime:
        """
        Get a datetime object based on a random date between 1 second form now
        and a given date.
        Accepts date strings that can be recognized by strtotime().

        :param end_date: Defaults to "+30d"
        :param tzinfo: timezone, instance of datetime.tzinfo subclass
        :example: datetime('1999-02-02 11:42:52')
        :return: datetime
        """
        ...
    def iso8601(
        self,
        tzinfo: Optional[datetime.tzinfo] = ...,
        end_datetime: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int, None] = ...,
        sep: str = ...,
        timespec: str = ...,
    ) -> str:
        """
        Get a timestamp in ISO 8601 format (or one of its profiles).

        :param tzinfo: timezone, instance of datetime.tzinfo subclass
        :param sep: separator between date and time, defaults to 'T'
        :param timespec: format specifier for the time part, defaults to 'auto' - see datetime.isoformat() documentation
        :example: '2003-10-21T16:05:52+0000'
        """
        ...
    def month(self) -> str: ...
    def month_name(self) -> str: ...
    def past_date(
        self,
        start_date: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int] = ...,
        tzinfo: Optional[datetime.tzinfo] = ...,
    ) -> datetime.date:
        """
        Get a Date object based on a random date between a given date and 1 day
        ago.
        Accepts date strings that can be recognized by strtotime().

        :param start_date: Defaults to "-30d"
        :param tzinfo: timezone, instance of datetime.tzinfo subclass
        :example: dtdate('1999-02-02')
        :return: dtdate
        """
        ...
    def past_datetime(
        self,
        start_date: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int] = ...,
        tzinfo: Optional[datetime.tzinfo] = ...,
    ) -> datetime.datetime:
        """
        Get a datetime object based on a random date between a given date and 1
        second ago.
        Accepts date strings that can be recognized by strtotime().

        :param start_date: Defaults to "-30d"
        :param tzinfo: timezone, instance of datetime.tzinfo subclass
        :example: datetime('1999-02-02 11:42:52')
        :return: datetime
        """
        ...
    def pytimezone(self, *args: Any, **kwargs: Any) -> Optional[datetime.tzinfo]:
        """
        Generate a random timezone (see `faker.timezone` for any args)
        and return as a python object usable as a `tzinfo` to `datetime`
        or other fakers.

        :example: faker.pytimezone()
        :return: dateutil.tz.tz.tzfile
        """
        ...
    def time(
        self,
        pattern: str = ...,
        end_datetime: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int, None] = ...,
    ) -> str:
        """
        Get a time string (24h format by default)

        :param pattern: format
        :example: '15:02:34'
        """
        ...
    def time_delta(
        self, end_datetime: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int, None] = ...
    ) -> datetime.timedelta:
        """
        Get a timedelta object
        """
        ...
    def time_object(
        self, end_datetime: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int, None] = ...
    ) -> datetime.time:
        """
        Get a time object

        :example: datetime.time(15, 56, 56, 772876)
        """
        ...
    def time_series(
        self,
        start_date: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int] = ...,
        end_date: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int] = ...,
        precision: Optional[float] = ...,
        distrib: Optional[Callable[[datetime.datetime], float]] = ...,
        tzinfo: Optional[datetime.tzinfo] = ...,
    ) -> Iterator[Tuple[datetime.datetime, Any]]:
        """
        Returns a generator yielding tuples of ``(<datetime>, <value>)``.

        The data points will start at ``start_date``, and be at every time interval specified by
        ``precision``.
        ``distrib`` is a callable that accepts ``<datetime>`` and returns ``<value>``
        """
        ...
    def timezone(self) -> str: ...
    def unix_time(
        self,
        end_datetime: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int, None] = ...,
        start_datetime: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int, None] = ...,
    ) -> float:
        """
        Get a timestamp between January 1, 1970 and now, unless passed
        explicit start_datetime or end_datetime values.

        On Windows, the decimal part is always 0.

        :example: 1061306726.6
        """
        ...
    def year(self) -> str: ...
    def emoji(self) -> str:
        """
        :example: '😉'
        """
        ...
    def file_extension(self, category: Optional[str] = ...) -> str:
        """
        Generate a file extension under the specified ``category``.

        If ``category`` is ``None``, a random category will be used. The list of
        valid categories include: ``'audio'``, ``'image'``, ``'office'``,
        ``'text'``, and ``'video'``.

        :sample:
        :sample: category='image'
        """
        ...
    def file_name(self, category: Optional[str] = ..., extension: Optional[str] = ...) -> str:
        """
        Generate a random file name with extension.

        If ``extension`` is ``None``, a random extension will be created
        under the hood using |file_extension| with the specified
        ``category``. If a value for ``extension`` is provided, the
        value will be used instead, and ``category`` will be ignored.
        The actual name part itself is generated using |word|. If
        extension is an empty string then no extension will be added,
        and file_name will be the same as |word|.

        :sample: size=10
        :sample: category='audio'
        :sample: extension='abcdef'
        :sample: category='audio', extension='abcdef'
        :sample: extension=''
        """
        ...
    def file_path(
        self,
        depth: int = ...,
        category: Optional[str] = ...,
        extension: Union[str, Sequence[str], None] = ...,
        absolute: Optional[bool] = ...,
        file_system_rule: Literal["linux", "windows"] = ...,
    ) -> str:
        """
        Generate an pathname to a file.

        This method uses |file_name| under the hood to generate the file
        name itself, and ``depth`` controls the depth of the directory
        path, and |word| is used under the hood to generate the
        different directory names.

        If ``absolute`` is ``True`` (default), the generated path starts
        with ``/`` and is absolute. Otherwise, the generated path is
        relative.

        If used, ``extension`` can be either a string, forcing that
        extension, a sequence of strings (one will be picked at random),
        or an empty sequence (the path will have no extension). Default
        behaviour is the same as |file_name|

        if ``file_system`` is set (default="linux"), the generated path uses
        specified file system path standard, the list of valid file systems include:
        ``'windows'``, ``'linux'``.

        :sample: size=10
        :sample: depth=3
        :sample: depth=5, category='video'
        :sample: depth=5, category='video', extension='abcdef'
        :sample: extension=[]
        :sample: extension=''
        :sample: extension=["a", "bc", "def"]
        :sample: depth=5, category='video', extension='abcdef', file_system='windows'
        """
        ...
    def mime_type(self, category: Optional[str] = ...) -> str:
        """
        Generate a mime type under the specified ``category``.

        If ``category`` is ``None``, a random category will be used. The list of
        valid categories include ``'application'``, ``'audio'``, ``'image'``,
        ``'message'``, ``'model'``, ``'multipart'``, ``'text'``, and
        ``'video'``.

        :sample:
        :sample: category='application'
        """
        ...
    def unix_device(self, prefix: Optional[str] = ...) -> str:
        """
        Generate a Unix device file name.

        If ``prefix`` is ``None``, a random prefix will be used. The list of
        valid prefixes include: ``'sd'``, ``'vd'``, and ``'xvd'``.

        :sample:
        :sample: prefix='mmcblk'
        """
        ...
    def unix_partition(self, prefix: Optional[str] = ...) -> str:
        """
        Generate a Unix partition name.

        This method uses |unix_device| under the hood to create a device file
        name with the specified ``prefix``.

        :sample:
        :sample: prefix='mmcblk'
        """
        ...
    def coordinate(self, center: Optional[float] = ..., radius: Union[float, int] = ...) -> Decimal:
        """
        Optionally center the coord and pick a point within radius.
        """
        ...
    def latitude(self) -> Decimal: ...
    def latlng(self) -> Tuple[Decimal, Decimal]: ...
    def local_latlng(self, country_code: str = ..., coords_only: bool = ...) -> Optional[Tuple[str, ...]]:
        """
        Returns a location known to exist on land in a country specified by `country_code`.
        Defaults to 'en_US'. See the `land_coords` list for available locations/countries.
        """
        ...
    def location_on_land(self, coords_only: bool = ...) -> Tuple[str, ...]:
        """
        Returns a random tuple specifying a coordinate set guaranteed to exist on land.
        Format is `(latitude, longitude, place name, two-letter country code, timezone)`
        Pass `coords_only` to return coordinates without metadata.
        """
        ...
    def longitude(self) -> Decimal: ...
    def ascii_company_email(self) -> str: ...
    def ascii_email(self) -> str: ...
    def ascii_free_email(self) -> str: ...
    def ascii_safe_email(self) -> str: ...
    def company_email(self) -> str: ...
    def dga(
        self,
        year: Optional[int] = ...,
        month: Optional[int] = ...,
        day: Optional[int] = ...,
        tld: Optional[str] = ...,
        length: Optional[int] = ...,
    ) -> str:
        """
        Generates a domain name by given date
        https://en.wikipedia.org/wiki/Domain_generation_algorithm

        :type year: int
        :type month: int
        :type day: int
        :type tld: str
        :type length: int
        :rtype: str
        """
        ...
    def domain_name(self, levels: int = ...) -> str:
        """
        Produce an Internet domain name with the specified number of
        subdomain levels.

        >>> domain_name()
        nichols-phillips.com
        >>> domain_name(2)
        williamson-hopkins.jackson.com
        """
        ...
    def domain_word(self) -> str: ...
    def email(self, safe: bool = ..., domain: Optional[str] = ...) -> str: ...
    def free_email(self) -> str: ...
    def free_email_domain(self) -> str: ...
    def hostname(self, levels: int = ...) -> str:
        """
        Produce a hostname with specified number of subdomain levels.

        >>> hostname()
        db-01.nichols-phillips.com
        >>> hostname(0)
        laptop-56
        >>> hostname(2)
        web-12.williamson-hopkins.jackson.com
        """
        ...
    def http_method(self) -> str:
        """
        Returns random HTTP method
        https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods

        :rtype: str
        """
        ...
    def http_status_code(self, include_unassigned: bool = ...) -> int:
        """
        Returns random HTTP status code
        https://www.rfc-editor.org/rfc/rfc9110#name-status-codes
        :param include_unassigned: Whether to include status codes which have
            not yet been assigned or are unused

        :return: a random three digit status code
        :rtype: int

        :example: 404
        """
        ...
    def iana_id(self) -> str:
        """
        Returns IANA Registrar ID
        https://www.iana.org/assignments/registrar-ids/registrar-ids.xhtml

        :rtype: str
        """
        ...
    def image_url(
        self, width: Optional[int] = ..., height: Optional[int] = ..., placeholder_url: Optional[str] = ...
    ) -> str:
        """
        Returns URL to placeholder image
        Example: http://placehold.it/640x480

        :param width: Optional image width
        :param height: Optional image height
        :param placeholder_url: Optional template string of image URLs from custom
            placeholder service. String must contain ``{width}`` and ``{height}``
            placeholders, eg: ``https:/example.com/{width}/{height}``.
        :rtype: str
        """
        ...
    def ipv4(self, network: bool = ..., address_class: Optional[str] = ..., private: Optional[str] = ...) -> str:
        """
        Returns a random IPv4 address or network with a valid CIDR.

        :param network: Network address
        :param address_class: IPv4 address class (a, b, or c)
        :param private: Public or private
        :returns: IPv4
        """
        ...
    def ipv4_network_class(self) -> str:
        """
        Returns a IPv4 network class 'a', 'b' or 'c'.

        :returns: IPv4 network class
        """
        ...
    def ipv4_private(self, network: bool = ..., address_class: Optional[str] = ...) -> str:
        """
        Returns a private IPv4.

        :param network: Network address
        :param address_class: IPv4 address class (a, b, or c)
        :returns: Private IPv4
        """
        ...
    def ipv4_public(self, network: bool = ..., address_class: Optional[str] = ...) -> str:
        """
        Returns a public IPv4 excluding private blocks.

        :param network: Network address
        :param address_class: IPv4 address class (a, b, or c)
        :returns: Public IPv4
        """
        ...
    def ipv6(self, network: bool = ...) -> str:
        """
        Produce a random IPv6 address or network with a valid CIDR
        """
        ...
    def mac_address(self, multicast: bool = ...) -> str:
        """
        Returns a random MAC address.

        :param multicast: Multicast address
        :returns: MAC Address
        """
        ...
    def nic_handle(self, suffix: str = ...) -> str:
        """
        Returns NIC Handle ID
        https://www.apnic.net/manage-ip/using-whois/guide/person/

        :rtype: str
        """
        ...
    def nic_handles(self, count: int = ..., suffix: str = ...) -> List[str]:
        """
        Returns NIC Handle ID list

        :rtype: list[str]
        """
        ...
    def port_number(self, is_system: bool = ..., is_user: bool = ..., is_dynamic: bool = ...) -> int:
        """
        Returns a network port number
        https://tools.ietf.org/html/rfc6335

        :param is_system: System or well-known ports
        :param is_user: User or registered ports
        :param is_dynamic: Dynamic / private / ephemeral ports
        :rtype: int
        """
        ...
    def ripe_id(self) -> str:
        """
        Returns RIPE Organization ID
        https://www.ripe.net/manage-ips-and-asns/db/support/organisation-object-in-the-ripe-database

        :rtype: str
        """
        ...
    def safe_domain_name(self) -> str: ...
    def safe_email(self) -> str: ...
    def slug(self, value: Optional[str] = ...) -> str:
        """
        Django algorithm
        """
        ...
    def tld(self) -> str: ...
    def uri(self, schemes: Optional[List[str]] = ..., deep: Optional[int] = ...) -> str:
        """
        :param schemes: a list of strings to use as schemes, one will chosen randomly.
            If None, it will generate http and https uris.
            Passing an empty list will result in schemeless uri generation like "://domain.com/index.html".
        :param deep: an integer specifying how many path components the URI should have..
        :return: a random url string.
        """
        ...
    def uri_extension(self) -> str: ...
    def uri_page(self) -> str: ...
    def uri_path(self, deep: Optional[int] = ...) -> str: ...
    def url(self, schemes: Optional[List[str]] = ...) -> str:
        """
        :param schemes: a list of strings to use as schemes, one will chosen randomly.
            If None, it will generate http and https urls.
            Passing an empty list will result in schemeless url generation like "://domain.com".
        :return: a random url string.
        """
        ...
    def user_name(self) -> str: ...
    def isbn10(self, separator: str = ...) -> str: ...
    def isbn13(self, separator: str = ...) -> str: ...
    def job(self) -> str: ...
    def get_words_list(
        self, part_of_speech: Optional[str] = ..., ext_word_list: Optional[Sequence[str]] = ...
    ) -> List[str]:
        """
        Get list of words.

        ``ext_word_list`` is a parameter that allows the user to provide a list
        of words to be used instead of the built-in word list. If ``ext_word_list``
        is provided, then the value of ``part_of_speech`` is ignored.

        ``part_of_speech`` is a parameter that defines to what part of speech
        the returned word belongs. If ``ext_word_list`` is not ``None``, then
        ``part_of_speech`` is ignored. If the value of ``part_of_speech`` does
        not correspond to an existent part of speech according to the set locale,
        then an exception is raised.

        :sample: part_of_speech="abc", ext_word_list=['abc', 'def', 'ghi', 'jkl']
        :sample: part_of_speech="abc"
        :sample: ext_word_list=['abc', 'def', 'ghi', 'jkl']

        .. warning::
            Depending on the length of a locale provider's built-in word list or
            on the length of ``ext_word_list`` if provided, a large ``nb`` can
            exhaust said lists if ``unique`` is ``True``, raising an exception.
        """
        ...
    def paragraph(
        self, nb_sentences: int = ..., variable_nb_sentences: bool = ..., ext_word_list: Optional[Sequence[str]] = ...
    ) -> str:
        """
        Generate a paragraph.

        The ``nb_sentences`` argument controls how many sentences the paragraph
        will contain, and setting ``variable_nb_sentences`` to ``False`` will
        generate the exact amount, while setting it to ``True`` (default) will
        generate a random amount (+/-40%, minimum of 1) using
        |randomize_nb_elements|.

        Under the hood, |sentences| is used to generate the sentences, so the
        argument ``ext_word_list`` works in the same way here as it would in
        that method.

        :sample: nb_sentences=5
        :sample: nb_sentences=5, variable_nb_sentences=False
        :sample: nb_sentences=5, ext_word_list=['abc', 'def', 'ghi', 'jkl']
        :sample: nb_sentences=5, variable_nb_sentences=False,
                 ext_word_list=['abc', 'def', 'ghi', 'jkl']
        """
        ...
    def paragraphs(self, nb: int = ..., ext_word_list: Optional[Sequence[str]] = ...) -> List[str]:
        """
        Generate a list of paragraphs.

        This method uses |paragraph| under the hood to generate paragraphs, and
        the ``nb`` argument controls exactly how many sentences the list will
        contain. The ``ext_word_list`` argument works in exactly the same way
        as well.

        :sample: nb=5
        :sample: nb=5, ext_word_list=['abc', 'def', 'ghi', 'jkl']
        """
        ...
    def sentence(
        self, nb_words: int = ..., variable_nb_words: bool = ..., ext_word_list: Optional[Sequence[str]] = ...
    ) -> str:
        """
        Generate a sentence.

        The ``nb_words`` argument controls how many words the sentence will
        contain, and setting ``variable_nb_words`` to ``False`` will generate
        the exact amount, while setting it to ``True`` (default) will generate
        a random amount (+/-40%, minimum of 1) using |randomize_nb_elements|.

        Under the hood, |words| is used to generate the words, so the argument
        ``ext_word_list`` works in the same way here as it would in that method.

        :sample: nb_words=10
        :sample: nb_words=10, variable_nb_words=False
        :sample: nb_words=10, ext_word_list=['abc', 'def', 'ghi', 'jkl']
        :sample: nb_words=10, variable_nb_words=True,
                 ext_word_list=['abc', 'def', 'ghi', 'jkl']
        """
        ...
    def sentences(self, nb: int = ..., ext_word_list: Optional[Sequence[str]] = ...) -> List[str]:
        """
        Generate a list of sentences.

        This method uses |sentence| under the hood to generate sentences, and
        the ``nb`` argument controls exactly how many sentences the list will
        contain. The ``ext_word_list`` argument works in exactly the same way
        as well.

        :sample:
        :sample: nb=5
        :sample: nb=5, ext_word_list=['abc', 'def', 'ghi', 'jkl']
        """
        ...
    def text(self, max_nb_chars: int = ..., ext_word_list: Optional[Sequence[str]] = ...) -> str:
        """
        Generate a text string.

        The ``max_nb_chars`` argument controls the approximate number of
        characters the text string will have, and depending on its value, this
        method may use either |words|, |sentences|, or |paragraphs| for text
        generation. The ``ext_word_list`` argument works in exactly the same way
        it would in any of those methods.

        :sample: max_nb_chars=20
        :sample: max_nb_chars=80
        :sample: max_nb_chars=160
        :sample: ext_word_list=['abc', 'def', 'ghi', 'jkl']
        """
        ...
    def texts(
        self, nb_texts: int = ..., max_nb_chars: int = ..., ext_word_list: Optional[Sequence[str]] = ...
    ) -> List[str]:
        """
        Generate a list of text strings.

        The ``nb_texts`` argument controls how many text strings the list will
        contain, and this method uses |text| under the hood for text generation,
        so the two remaining arguments, ``max_nb_chars`` and ``ext_word_list``
        will work in exactly the same way as well.

        :sample: nb_texts=5
        :sample: nb_texts=5, max_nb_chars=50
        :sample: nb_texts=5, max_nb_chars=50,
                 ext_word_list=['abc', 'def', 'ghi', 'jkl']
        """
        ...
    def word(self, part_of_speech: Optional[str] = ..., ext_word_list: Optional[Sequence[str]] = ...) -> str:
        """
        Generate a word.

        This method uses |words| under the hood with the ``nb`` argument set to
        ``1`` to generate the result.

        :sample:
        :sample: ext_word_list=['abc', 'def', 'ghi', 'jkl']
        """
        ...
    def words(self, nb: int = ..., ext_word_list: Optional[List[str]] = ..., unique: bool = ...) -> List[str]:
        """
        Generate a tuple of words.

        The ``nb`` argument controls the number of words in the resulting list,
        and if ``ext_word_list`` is provided, words from that list will be used
        instead of those from the locale provider's built-in word list.

        if ``word_list`` is not provided, the method will use a default value of None,
        which will result in the method calling the ``get_words_list`` method to get the
        word list. If ``word_list`` is provided, the method will use the provided list.

        If ``unique`` is ``True``, this method will return a list containing
        unique words. Under the hood, |random_sample| will be used for sampling
        without replacement. If ``unique`` is ``False``, |random_choices| is
        used instead, and the list returned may contain duplicates.

        :sample:
        :sample: nb=5
        :sample: nb=5, ext_word_list=['abc', 'def', 'ghi', 'jkl']
        :sample: nb=4, ext_word_list=['abc', 'def', 'ghi', 'jkl'], unique=True
        """
        ...
    def binary(self, length: int = ...) -> bytes:
        """
        Generate a random binary blob of ``length`` bytes.

        If this faker instance has been seeded, performance will be signficiantly reduced, to conform
        to the seeding.

        :sample: length=64
        """
        ...
    def boolean(self, chance_of_getting_true: int = ...) -> bool:
        """
        Generate a random boolean value based on ``chance_of_getting_true``.

        :sample: chance_of_getting_true=25
        :sample: chance_of_getting_true=50
        :sample: chance_of_getting_true=75
        """
        ...
    def csv(
        self,
        header: Optional[Sequence[str]] = ...,
        data_columns: Tuple[str, str] = ...,
        num_rows: int = ...,
        include_row_ids: bool = ...,
    ) -> str:
        """
        Generate random comma-separated values.

        For more information on the different arguments of this method, please refer to
        :meth:`dsv() <faker.providers.misc.Provider.dsv>` which is used under the hood.

        :sample: data_columns=('{{name}}', '{{address}}'), num_rows=10, include_row_ids=False
        :sample: header=('Name', 'Address', 'Favorite Color'),
                data_columns=('{{name}}', '{{address}}', '{{safe_color_name}}'),
                num_rows=10, include_row_ids=True
        """
        ...
    def dsv(
        self,
        dialect: str = ...,
        header: Optional[Sequence[str]] = ...,
        data_columns: Tuple[str, str] = ...,
        num_rows: int = ...,
        include_row_ids: bool = ...,
        **fmtparams: Any
    ) -> str:
        """
        Generate random delimiter-separated values.

        This method's behavior share some similarities with ``csv.writer``. The ``dialect`` and
        ``**fmtparams`` arguments are the same arguments expected by ``csv.writer`` to control its
        behavior, and instead of expecting a file-like object to where output will be written, the
        output is controlled by additional keyword arguments and is returned as a string.

        The ``dialect`` argument defaults to ``'faker-csv'`` which is the name of a ``csv.excel``
        subclass with full quoting enabled.

        The ``header`` argument expects a list or a tuple of strings that will serve as the header row
        if supplied. The ``data_columns`` argument expects a list or a tuple of string tokens, and these
        string tokens will be passed to  :meth:`pystr_format() <faker.providers.python.Provider.pystr_format>`
        for data generation. Argument Groups are used to pass arguments to the provider methods.
        Both ``header`` and ``data_columns`` must be of the same length.

        Example:
            fake.set_arguments('top_half', {'min_value': 50, 'max_value': 100})
            fake.dsv(data_columns=('{{ name }}', '{{ pyint:top_half }}'))

        The ``num_rows`` argument controls how many rows of data to generate, and the ``include_row_ids``
        argument may be set to ``True`` to include a sequential row ID column.

        :sample: dialect='excel', data_columns=('{{name}}', '{{address}}')
        :sample: dialect='excel-tab', data_columns=('{{name}}', '{{address}}'), include_row_ids=True
        :sample: data_columns=('{{name}}', '{{address}}'), num_rows=5, delimiter='$'
        """
        ...
    def fixed_width(self, data_columns: Optional[list] = ..., num_rows: int = ..., align: str = ...) -> str:
        """
        Generate random fixed width values.

        Using a list of tuple records that is passed as ``data_columns``, that
        defines the structure that will be generated. Arguments within the
        record are provider specific, and should be a dictionary that will be
        passed to the provider method.

        Data Column List format
            [('field width', 'definition', {'arguments'})]

        The definition can be 'provider', 'provider:argument_group', tokenized
        'string {{ provider:argument_group }}' that is passed to the python
        provider method pystr_format() for generation, or a fixed '@word'.
        Using Lists, Tuples, and Dicts as a definition for structure.

        Argument Groups can be used to pass arguments to the provider methods,
        but will override the arguments supplied in the tuple record.

        Example:
            fake.set_arguments('top_half', {'min_value': 50, 'max_value': 100})
            fake.fixed_width(data_columns=[(20, 'name'), (3, 'pyint:top_half')])

        :param data_columns: specification for the data structure
        :type data_columns: list
        :param num_rows: number of rows the generator will yield
        :type num_rows: int
        :param align: positioning of the value. (left, middle, right)
        :type align: str
        :return: Serialized Fixed Width data
        :rtype: str

        :sample: data_columns=[(20, 'name'), (3, 'pyint', {'min_value': 50,
                'max_value': 100})], align='right', num_rows=2
        """
        ...
    def image(
        self,
        size: Tuple[int, int] = ...,
        image_format: str = ...,
        hue: Union[int, Sequence[int], str, None] = ...,
        luminosity: Optional[str] = ...,
    ) -> bytes:
        """
        Generate an image and draw a random polygon on it using the Python Image Library.
        Without it installed, this provider won't be functional. Returns the bytes representing
        the image in a given format.

        The argument ``size`` must be a 2-tuple containing (width, height) in pixels. Defaults to 256x256.

        The argument ``image_format`` can be any valid format to the underlying library like ``'tiff'``,
        ``'jpeg'``, ``'pdf'`` or ``'png'`` (default). Note that some formats need present system libraries
        prior to building the Python Image Library.
        Refer to https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html for details.

        The arguments ``hue`` and ``luminosity`` are the same as in the color provider and are simply forwarded to
        it to generate both the background and the shape colors. Therefore, you can ask for a "dark blue" image, etc.

        :sample: size=(2, 2), hue='purple', luminosity='bright', image_format='pdf'
        :sample: size=(16, 16), hue=[90,270], image_format='ico'
        """
        ...
    def json(
        self,
        data_columns: Optional[List] = ...,
        num_rows: int = ...,
        indent: Optional[int] = ...,
        cls: Optional[Type[encoder.JSONEncoder]] = ...,
    ) -> str:
        """
        Generate random JSON structure values.

        Using a dictionary or list of records that is passed as ``data_columns``,
        define the structure that is used to build JSON structures.  For complex
        data structures it is recommended to use the dictionary format.

        Data Column Dictionary format:
            {'key name': 'definition'}

        The definition can be 'provider', 'provider:argument_group', tokenized
        'string {{ provider:argument_group }}' that is passed to the python
        provider method pystr_format() for generation, or a fixed '@word'.
        Using Lists, Tuples, and Dicts as a definition for structure.

        Example:
            fake.set_arguments('top_half', {'min_value': 50, 'max_value': 100})
            fake.json(data_columns={'Name': 'name', 'Score': 'pyint:top_half'})

        Data Column List format:
            [('key name', 'definition', {'arguments'})]

        With the list format the definition can be a list of records, to create
        a list within the structure data.  For literal entries within the list,
        set the 'field_name' to None.

        :param data_columns: specification for the data structure
        :type data_columns: dict
        :param num_rows: number of rows the returned
        :type num_rows: int
        :param indent: number of spaces to indent the fields
        :type indent: int
        :param cls: optional json encoder to use for non-standard objects such as datetimes
        :type cls: json.JSONEncoder
        :return: Serialized JSON data
        :rtype: str

        :sample: data_columns={'Spec': '@1.0.1', 'ID': 'pyint',
                'Details': {'Name': 'name', 'Address': 'address'}}, num_rows=2
        :sample: data_columns={'Candidates': ['name', 'name', 'name']},
                num_rows=1
        :sample: data_columns=[('Name', 'name'), ('Points', 'pyint',
                {'min_value': 50, 'max_value': 100})], num_rows=1
        """
        ...
    def json_bytes(
        self,
        data_columns: Optional[List] = ...,
        num_rows: int = ...,
        indent: Optional[int] = ...,
        cls: Optional[Type[encoder.JSONEncoder]] = ...,
    ) -> bytes:
        """
        Generate random JSON structure and return as bytes.

        For more information on the different arguments of this method, refer to
        :meth:`json() <faker.providers.misc.Provider.json>` which is used under the hood.
        """
        ...
    @overload
    def md5(self, raw_output: Literal[True]) -> bytes:
        """
        Generate a random MD5 hash.

        If ``raw_output`` is ``False`` (default), a hexadecimal string representation of the MD5 hash
        will be returned. If ``True``, a ``bytes`` object representation will be returned instead.

        :sample: raw_output=False
        :sample: raw_output=True
        """
        ...
    @overload
    def md5(self, raw_output: Literal[False]) -> str:
        """
        Generate a random MD5 hash.

        If ``raw_output`` is ``False`` (default), a hexadecimal string representation of the MD5 hash
        will be returned. If ``True``, a ``bytes`` object representation will be returned instead.

        :sample: raw_output=False
        :sample: raw_output=True
        """
        ...
    def null_boolean(self) -> Optional[bool]:
        """
        Generate ``None``, ``True``, or ``False``, each with equal probability.
        """
        ...
    def password(
        self,
        length: int = ...,
        special_chars: bool = ...,
        digits: bool = ...,
        upper_case: bool = ...,
        lower_case: bool = ...,
    ) -> str:
        """
        Generate a random password of the specified ``length``.

        The arguments ``special_chars``, ``digits``, ``upper_case``, and ``lower_case`` control
        what category of characters will appear in the generated password. If set to ``True``
        (default), at least one character from the corresponding category is guaranteed to appear.
        Special characters are characters from ``!@#$%^&*()_+``, digits are characters from
        ``0123456789``, and uppercase and lowercase characters are characters from the ASCII set of
        letters.

        :sample: length=12
        :sample: length=40, special_chars=False, upper_case=False
        """
        ...
    def psv(
        self,
        header: Optional[Sequence[str]] = ...,
        data_columns: Tuple[str, str] = ...,
        num_rows: int = ...,
        include_row_ids: bool = ...,
    ) -> str:
        """
        Generate random pipe-separated values.

        For more information on the different arguments of this method, please refer to
        :meth:`dsv() <faker.providers.misc.Provider.dsv>` which is used under the hood.

        :sample: data_columns=('{{name}}', '{{address}}'), num_rows=10, include_row_ids=False
        :sample: header=('Name', 'Address', 'Favorite Color'),
                data_columns=('{{name}}', '{{address}}', '{{safe_color_name}}'),
                num_rows=10, include_row_ids=True
        """
        ...
    @overload
    def sha1(self, raw_output: Literal[True]) -> bytes:
        """
        Generate a random SHA-1 hash.

        If ``raw_output`` is ``False`` (default), a hexadecimal string representation of the SHA-1 hash
        will be returned. If ``True``, a ``bytes`` object representation will be returned instead.

        :sample: raw_output=False
        :sample: raw_output=True
        """
        ...
    @overload
    def sha1(self, raw_output: Literal[False]) -> str:
        """
        Generate a random SHA-1 hash.

        If ``raw_output`` is ``False`` (default), a hexadecimal string representation of the SHA-1 hash
        will be returned. If ``True``, a ``bytes`` object representation will be returned instead.

        :sample: raw_output=False
        :sample: raw_output=True
        """
        ...
    @overload
    def sha256(self, raw_output: Literal[True]) -> bytes:
        """
        Generate a random SHA-256 hash.

        If ``raw_output`` is ``False`` (default), a hexadecimal string representation of the SHA-256 hash
        will be returned. If ``True``, a ``bytes`` object representation will be returned instead.

        :sample: raw_output=False
        :sample: raw_output=True
        """
        ...
    @overload
    def sha256(self, raw_output: Literal[False]) -> str:
        """
        Generate a random SHA-256 hash.

        If ``raw_output`` is ``False`` (default), a hexadecimal string representation of the SHA-256 hash
        will be returned. If ``True``, a ``bytes`` object representation will be returned instead.

        :sample: raw_output=False
        :sample: raw_output=True
        """
        ...
    def tar(
        self,
        uncompressed_size: int = ...,
        num_files: int = ...,
        min_file_size: int = ...,
        compression: Optional[str] = ...,
    ) -> bytes:
        """
        Generate a bytes object containing a random valid tar file.

        The number and sizes of files contained inside the resulting archive can be controlled
        using the following arguments:

        - ``uncompressed_size`` - the total size of files before compression, 16 KiB by default
        - ``num_files`` - the number of files archived in resulting zip file, 1 by default
        - ``min_file_size`` - the minimum size of each file before compression, 4 KiB by default

        No compression is used by default, but setting ``compression`` to one of the values listed
        below will use the corresponding compression type.

        - ``'bzip2'`` or ``'bz2'`` for BZIP2
        - ``'lzma'`` or ``'xz'`` for LZMA
        - ``'gzip'`` or ``'gz'`` for GZIP

        :sample: uncompressed_size=256, num_files=4, min_file_size=32
        :sample: uncompressed_size=256, num_files=32, min_file_size=4, compression='bz2'
        """
        ...
    def tsv(
        self,
        header: Optional[Sequence[str]] = ...,
        data_columns: Tuple[str, str] = ...,
        num_rows: int = ...,
        include_row_ids: bool = ...,
    ) -> str:
        """
        Generate random tab-separated values.

        For more information on the different arguments of this method, please refer to
        :meth:`dsv() <faker.providers.misc.Provider.dsv>` which is used under the hood.

        :sample: data_columns=('{{name}}', '{{address}}'), num_rows=10, include_row_ids=False
        :sample: header=('Name', 'Address', 'Favorite Color'),
                data_columns=('{{name}}', '{{address}}', '{{safe_color_name}}'),
                num_rows=10, include_row_ids=True
        """
        ...
    def uuid4(
        self, cast_to: Union[Callable[[UUID], str], Callable[[UUID], bytes], None] = ...
    ) -> Union[bytes, str, UUID]:
        """
        Generate a random UUID4 object and cast it to another type if specified using a callable ``cast_to``.

        By default, ``cast_to`` is set to ``str``.

        May be called with ``cast_to=None`` to return a full-fledged ``UUID``.

        :sample:
        :sample: cast_to=None
        """
        ...
    def xml(
        self,
        nb_elements: int = ...,
        variable_nb_elements: bool = ...,
        value_types: Union[List[Type], Tuple[Type, ...], None] = ...,
        allowed_types: Union[List[Type], Tuple[Type, ...], None] = ...,
    ) -> str:
        """
        Returns some XML.

        :nb_elements: number of elements for dictionary
        :variable_nb_elements: is use variable number of elements for dictionary
        :value_types: type of dictionary values

        Note: this provider required xmltodict library installed
        """
        ...
    def zip(
        self,
        uncompressed_size: int = ...,
        num_files: int = ...,
        min_file_size: int = ...,
        compression: Optional[str] = ...,
    ) -> bytes:
        """
        Generate a bytes object containing a random valid zip archive file.

        The number and sizes of files contained inside the resulting archive can be controlled
        using the following arguments:

        - ``uncompressed_size`` - the total size of files before compression, 16 KiB by default
        - ``num_files`` - the number of files archived in resulting zip file, 1 by default
        - ``min_file_size`` - the minimum size of each file before compression, 4 KiB by default

        No compression is used by default, but setting ``compression`` to one of the values listed
        below will use the corresponding compression type.

        - ``'bzip2'`` or ``'bz2'`` for BZIP2
        - ``'lzma'`` or ``'xz'`` for LZMA
        - ``'deflate'``, ``'gzip'``, or ``'gz'`` for GZIP

        :sample: uncompressed_size=256, num_files=4, min_file_size=32
        :sample: uncompressed_size=256, num_files=32, min_file_size=4, compression='bz2'
        """
        ...
    def passport_dates(self, birthday: datetime.date = ...) -> Tuple[str, str, str]:
        """
        Generates a formatted date of birth, issue, and expiration dates.
        issue and expiration dates are conditioned to fall within U.S. standards of 5 and 10 year expirations


        The ``birthday`` argument is a datetime.date object representing a date of birth.

        Sources:

        -https://travel.state.gov/content/travel/en/passports/passport-help/faqs.html
        """
        ...
    def passport_dob(self) -> datetime.date:
        """
        Generate a datetime date of birth.
        """
        ...
    def passport_full(self) -> str:
        """
        Generates a formatted sting with US Passport information
        """
        ...
    def passport_gender(self, seed: int = ...) -> str:
        """
        Generates a string representing the gender displayed on a passport

        Sources:

        - https://williamsinstitute.law.ucla.edu/publications/x-gender-markers-passports/
        """
        ...
    def passport_number(self) -> str:
        """
        Generate a passport number by replacing tokens to be alphanumeric
        """
        ...
    def passport_owner(self, gender: str = ...) -> Tuple[str, str]:
        """
        Generate a given_name and surname for a passport owner
        The ``gender`` argument is the gender marker of a passport owner, which is a one character string
        that is either male, female, or non-binary.
        """
        ...
    def first_name(self) -> str: ...
    def first_name_female(self) -> str: ...
    def first_name_male(self) -> str: ...
    def first_name_nonbinary(self) -> str: ...
    def language_name(self) -> str:
        """
        Generate a random i18n language name (e.g. English).
        """
        ...
    def last_name(self) -> str: ...
    def last_name_female(self) -> str: ...
    def last_name_male(self) -> str: ...
    def last_name_nonbinary(self) -> str: ...
    def name(self) -> str:
        """
        :example: 'John Doe'
        """
        ...
    def name_female(self) -> str: ...
    def name_male(self) -> str: ...
    def name_nonbinary(self) -> str: ...
    def prefix(self) -> str: ...
    def prefix_female(self) -> str: ...
    def prefix_male(self) -> str: ...
    def prefix_nonbinary(self) -> str: ...
    def suffix(self) -> str: ...
    def suffix_female(self) -> str: ...
    def suffix_male(self) -> str: ...
    def suffix_nonbinary(self) -> str: ...
    def basic_phone_number(self) -> str: ...
    def country_calling_code(self) -> str: ...
    def msisdn(self) -> str:
        """
        https://en.wikipedia.org/wiki/MSISDN
        """
        ...
    def phone_number(self) -> str: ...
    def profile(
        self, fields: Optional[List[str]] = ..., sex: Optional[Literal["M", "F"]] = ...
    ) -> Dict[str, Union[str, Tuple[Decimal, Decimal], List[str], datetime.date]]:
        """
        Generates a complete profile.
        If "fields" is not empty, only the fields in the list will be returned
        """
        ...
    def simple_profile(
        self, sex: Optional[Literal["M", "F"]] = ...
    ) -> Dict[str, Union[str, datetime.date, Literal["M", "F"]]]:
        """
        Generates a basic profile with personal informations
        """
        ...
    def enum(self, enum_cls: Type[TEnum]) -> TEnum:
        """
        Returns a random enum of the provided input `Enum` type.

        :param enum_cls: The `Enum` type to produce the value for.
        :returns: A randomly selected enum value.
        """
        ...
    def pybool(self, truth_probability: int = ...) -> bool:
        """
        Generates a random boolean, optionally biased towards `True` or `False`.

        :truth_probability: Probability of generating a `True` value. Must be between `0` and `100` inclusive'.
        :return: Random boolean.
        :raises ValueError: If invalid `truth_probability` is provided.
        """
        ...
    def pydecimal(
        self,
        left_digits: Optional[int] = ...,
        right_digits: Optional[int] = ...,
        positive: bool = ...,
        min_value: Union[float, int, None] = ...,
        max_value: Union[float, int, None] = ...,
    ) -> Decimal: ...
    def pydict(
        self,
        nb_elements: int = ...,
        variable_nb_elements: bool = ...,
        value_types: Union[List[Type], Tuple[Type, ...], None] = ...,
        allowed_types: Union[List[Type], Tuple[Type, ...], None] = ...,
    ) -> Dict[Any, Any]:
        """
        Returns a dictionary.

        :nb_elements: number of elements for dictionary
        :variable_nb_elements: is use variable number of elements for dictionary
        :value_types: type of dictionary values
        """
        ...
    def pyfloat(
        self,
        left_digits: Optional[int] = ...,
        right_digits: Optional[int] = ...,
        positive: Optional[bool] = ...,
        min_value: Union[float, int, None] = ...,
        max_value: Union[float, int, None] = ...,
    ) -> float: ...
    def pyint(self, min_value: int = ..., max_value: int = ..., step: int = ...) -> int: ...
    def pyiterable(
        self,
        nb_elements: int = ...,
        variable_nb_elements: bool = ...,
        value_types: Union[List[Type], Tuple[Type, ...], None] = ...,
        allowed_types: Union[List[Type], Tuple[Type, ...], None] = ...,
    ) -> Iterable[Any]: ...
    def pylist(
        self,
        nb_elements: int = ...,
        variable_nb_elements: bool = ...,
        value_types: Union[List[Type], Tuple[Type, ...], None] = ...,
        allowed_types: Union[List[Type], Tuple[Type, ...], None] = ...,
    ) -> List[Any]: ...
    def pyobject(
        self, object_type: Optional[Type[Union[bool, str, float, int, tuple, set, list, Iterable, dict]]] = ...
    ) -> Union[bool, str, float, int, tuple, set, list, Iterable, dict, None]:
        """
        Generates a random object passing the type desired.

        :object_type: the type of the object to generate.
        :return: the random object generated.
        :raises ValueError: if the object type passed is not supported
        """
        ...
    def pyset(
        self,
        nb_elements: int = ...,
        variable_nb_elements: bool = ...,
        value_types: Union[List[Type], Tuple[Type, ...], None] = ...,
        allowed_types: Union[List[Type], Tuple[Type, ...], None] = ...,
    ) -> Set[Any]: ...
    def pystr(self, min_chars: Optional[int] = ..., max_chars: int = ..., prefix: str = ..., suffix: str = ...) -> str:
        """
        Generates a random string of upper and lowercase letters.

        :param min_chars: minimum length of the random part.
        :param max_chars: maximum length of the random part.
        :param prefix: an optional prefix to prepend to the random string.
        :param suffix: an optional suffix to append to the random string.
        :return: Random of random length between min and max characters.
        """
        ...
    def pystr_format(self, string_format: str = ..., letters: str = ...) -> str: ...
    def pystruct(
        self,
        count: int = ...,
        value_types: Union[List[Type], Tuple[Type, ...], None] = ...,
        allowed_types: Union[List[Type], Tuple[Type, ...], None] = ...,
    ) -> Tuple[List, Dict, Dict]: ...
    def pytuple(
        self,
        nb_elements: int = ...,
        variable_nb_elements: bool = ...,
        value_types: Union[List[Type], Tuple[Type, ...], None] = ...,
        allowed_types: Union[List[Type], Tuple[Type, ...], None] = ...,
    ) -> Tuple[Any, ...]: ...
    def sbn9(self, separator: str = ...) -> str: ...
    def ein(self) -> str:
        """
        Generate a random United States Employer Identification Number (EIN).

        An United States An Employer Identification Number (EIN) is
        also known as a Federal Tax Identification Number, and is
        used to identify a business entity. EINs follow a format of a
        two-digit prefix followed by a hyphen and a seven-digit sequence:
        ##-######

        https://www.irs.gov/businesses/small-businesses-self-employed/employer-id-numbers
        """
        ...
    def invalid_ssn(self) -> str:
        """
        Generate a random invalid United States Social Security Identification Number (SSN).

        Invalid SSNs have the following characteristics:
        Cannot begin with the number 9
        Cannot begin with 666 in positions 1 - 3
        Cannot begin with 000 in positions 1 - 3
        Cannot contain 00 in positions 4 - 5
        Cannot contain 0000 in positions 6 - 9

        https://www.ssa.gov/kc/SSAFactSheet--IssuingSSNs.pdf

        Additionally, return an invalid SSN that is NOT a valid ITIN by excluding certain ITIN related "group" values
        """
        ...
    def itin(self) -> str:
        """
        Generate a random United States Individual Taxpayer Identification Number (ITIN).

        An United States Individual Taxpayer Identification Number
        (ITIN) is a tax processing number issued by the Internal
        Revenue Service. It is a nine-digit number that always begins
        with the number 9 and has a range of 70-88 in the fourth and
        fifth digit. Effective April 12, 2011, the range was extended
        to include 900-70-0000 through 999-88-9999, 900-90-0000
        through 999-92-9999 and 900-94-0000 through 999-99-9999.
        https://www.irs.gov/individuals/international-taxpayers/general-itin-information
        """
        ...
    def ssn(self, taxpayer_identification_number_type: str = ...) -> str:
        """
        Generate a random United States Taxpayer Identification Number of the specified type.

        If no type is specified, a US SSN is returned.
        """
        ...
    def android_platform_token(self) -> str:
        """
        Generate an Android platform token used in user agent strings.
        """
        ...
    def chrome(self, version_from: int = ..., version_to: int = ..., build_from: int = ..., build_to: int = ...) -> str:
        """
        Generate a Chrome web browser user agent string.
        """
        ...
    def firefox(self) -> str:
        """
        Generate a Mozilla Firefox web browser user agent string.
        """
        ...
    def internet_explorer(self) -> str:
        """
        Generate an IE web browser user agent string.
        """
        ...
    def ios_platform_token(self) -> str:
        """
        Generate an iOS platform token used in user agent strings.
        """
        ...
    def linux_platform_token(self) -> str:
        """
        Generate a Linux platform token used in user agent strings.
        """
        ...
    def linux_processor(self) -> str:
        """
        Generate a Linux processor token used in user agent strings.
        """
        ...
    def mac_platform_token(self) -> str:
        """
        Generate a MacOS platform token used in user agent strings.
        """
        ...
    def mac_processor(self) -> str:
        """
        Generate a MacOS processor token used in user agent strings.
        """
        ...
    def opera(self) -> str:
        """
        Generate an Opera web browser user agent string.
        """
        ...
    def safari(self) -> str:
        """
        Generate a Safari web browser user agent string.
        """
        ...
    def user_agent(self) -> str:
        """
        Generate a random web browser user agent string.
        """
        ...
    def windows_platform_token(self) -> str:
        """
        Generate a Windows platform token used in user agent strings.
        """
        ...
    def area_code(self) -> str: ...
    def cellphone_number(self) -> str: ...
    def cellphone_provider_code(self) -> str: ...
    def service_phone_number(self) -> str: ...
    def telephone_number(self) -> str: ...
    def telephone_provider_code(self) -> str: ...
    def toll_number(self) -> str: ...
    def initials(self) -> str:
        """
        Generate an initial number for license plates.
        """
        ...
    def operator_id(self) -> str: ...
    def district(self) -> str:
        """
        Generate a district code for license plates.
        """
        ...
    def provider_code(self) -> str: ...
    def license_plate_ar(self) -> str:
        """
        Generate a license plate in Arabic characters.

        This method first generates a license plate in Latin/Western characters
        using |license_plate_en|, and the result is translated internally to
        generate the Arabic counterpart which serves as this method's return
        value.
        """
        ...
    def license_plate_en(self) -> str:
        """
        Generate a license plate in Latin/Western characters.
        """
        ...
    def district_suffix(self) -> str:
        """
        :example: 'r.'
        """
        ...
    def house_number(self) -> str:
        """
        :example: 'm. 49'
        """
        ...
    def settlement(self) -> str:
        """
        :example: 'Horadiz'
        """
        ...
    def settlement_suffix(self) -> str:
        """
        :example: 'qəs.'
        """
        ...
    def street(self) -> str:
        """
        :example: 'A.AĞAYEV'
        """
        ...
    def village(self) -> str:
        """
        :example: 'Didivar'
        """
        ...
    def village_suffix(self) -> str:
        """
        :example: 'k.'
        """
        ...
    def bank(self) -> str:
        """
        Generate a bank name.
        """
        ...
    def large_company(self) -> str:
        """
        :example: 'SOCAR'
        """
        ...
    def last_name_unique_to_female(self) -> str: ...
    def last_name_unique_to_male(self) -> str: ...
    def last_name_unisex(self) -> str: ...
    def landline_number(self) -> str: ...
    def start_digit(self) -> str: ...
    def vat_id(self) -> str:
        """
        http://ec.europa.eu/taxation_customs/vies/faq.html#item_11
        :return: A random Bulgarian VAT ID
        """
        ...
    def area_name(self) -> str:
        """
        :example: 'উজির'
        """
        ...
    def building_name(self) -> str:
        """
        :example: 'বাড়ী নং'
        """
        ...
    def town(self) -> str:
        """
        :example: 'নবাব'
        """
        ...
    def city_name(self) -> str:
        """
        :example: 'ঢাকা মেট্রো'
        """
        ...
    def vehicle_category_letter(self) -> str:
        """
        :example: 'ব'
        """
        ...
    def vehicle_category_number(self) -> str:
        """
        :example: '১১'
        """
        ...
    def vehicle_serial_number(self) -> str:
        """
        Generate a 4 digits vehicle serial number.
        :example: '৫৪৩২'
        """
        ...
    def first_name_female_common(self) -> str:
        """
        Return religiously unbiased female first name.
        :example: 'অর্পিতা'
        """
        ...
    def first_name_female_hinduism(self) -> str:
        """
        Return Hindu religion based female first name.
        :example: 'দূর্গা'
        """
        ...
    def first_name_female_islamic(self) -> str:
        """
        Return Islam religion based female first name.
        :example: 'মেহজাবিন'
        """
        ...
    def first_name_male_common(self) -> str:
        """
        Return religiously unbiased male first name.
        :example: 'প্রিতম'
        """
        ...
    def first_name_male_hinduism(self) -> str:
        """
        Return Hindu religion based male first name.
        :example: 'অশোক'
        """
        ...
    def first_name_male_islamic(self) -> str:
        """
        Return Islam religion based male first name.
        :example: 'ইকবাল'
        """
        ...
    def last_name_common(self) -> str:
        """
        Return religiously and gender unbiased last name.
        :example: 'চৌধুরী'
        """
        ...
    def last_name_female_islamic(self) -> str:
        """
        Return Islam religion based female last name.
        :example: 'খাতুন'
        """
        ...
    def last_name_hinduism(self) -> str:
        """
        Return gender unbiased Hindu religion based last name.
        :example: 'দত্ত'
        """
        ...
    def last_name_islamic(self) -> str:
        """
        Return gender unbiased Islam religion based last name.
        :example: 'আলি'
        """
        ...
    def city_with_postcode(self) -> str: ...
    def street_suffix_long(self) -> str: ...
    def street_suffix_short(self) -> str: ...
    def birth_number(self) -> str:
        """
        Birth Number (Czech/Slovak: rodné číslo (RČ))
        https://en.wikipedia.org/wiki/National_identification_number#Czech_Republic_and_Slovakia
        """
        ...
    def dk_street_name(self) -> str:
        """
        This returns the name of a street, without any suffix.
        """
        ...
    def local_latitude(self) -> Decimal: ...
    def local_longitude(self) -> Decimal: ...
    def canton(self) -> Tuple[str, str]:
        """
        Randomly returns a swiss canton ('Abbreviated', 'Name').
        :example ('ZH', 'Zürich')
        """
        ...
    def canton_code(self) -> str:
        """
        Randomly returns a Swiss canton code.
        :example 'ZH'
        """
        ...
    def canton_name(self) -> str:
        """
        Randomly returns a Swiss canton name.
        :example 'Zürich'
        """
        ...
    def line_address(self) -> str: ...
    def region(self) -> str: ...
    def street_prefix(self) -> str: ...
    def street_prefix_long(self) -> str: ...
    def street_prefix_short(self) -> str: ...
    def police_id(self) -> str:
        """
        Generates random Greek identity card (aka police-issued identification card) numbers
        :return: a random Greek identity card number
        """
        ...
    def tin(self) -> str:
        """
        Generates random Greek personal TINs
        :return: a random Greek personal TIN
        """
        ...
    def postal_code_letter(self) -> str:
        """
        Returns a random letter from the list of allowable
        letters in a canadian postal code
        """
        ...
    def postalcode_in_province(self, province_abbr: Optional[str] = ...) -> str: ...
    def postcode_in_province(self, province_abbr: Optional[str] = ...) -> str:
        """
        Returns a random postcode within the provided province abbreviation
        """
        ...
    def province(self) -> str: ...
    def province_abbr(self) -> str: ...
    def county(self) -> str: ...
    def aadhaar_id(self) -> str:
        """
        Aadhaar is a 12 digit person identifier generated for residents of
        India.
        Details: https://en.wikipedia.org/wiki/Aadhaar
        Official Website: https://uidai.gov.in/my-aadhaar/about-your-aadhaar.html
        """
        ...
    def rd_number(self) -> str: ...
    def te_reo_ending(self) -> str: ...
    def te_reo_first(self) -> str: ...
    def te_reo_part(self) -> str: ...
    def building_name_suffix(self) -> str: ...
    def building_unit_number(self) -> str: ...
    def floor_number(self) -> str: ...
    def floor_unit_number(self) -> str: ...
    def luzon_province(self) -> str: ...
    def luzon_province_address(self) -> str: ...
    def luzon_province_postcode(self) -> str: ...
    def metro_manila_address(self) -> str: ...
    def metro_manila_lgu(self) -> str: ...
    def metro_manila_postcode(self) -> str: ...
    def mindanao_province(self) -> str: ...
    def mindanao_province_address(self) -> str: ...
    def mindanao_province_postcode(self) -> str: ...
    def ordinal_floor_number(self) -> str: ...
    def ordinal_street_number(self) -> str: ...
    def partitioned_building_number(self) -> str: ...
    def province_lgu(self) -> str: ...
    def standalone_building_number(self) -> str: ...
    def subdivision_block_number(self) -> str: ...
    def subdivision_lot_number(self) -> str: ...
    def subdivision_name(self) -> str: ...
    def subdivision_name_suffix(self) -> str: ...
    def subdivision_unit_number(self) -> str: ...
    def visayas_province(self) -> str: ...
    def visayas_province_address(self) -> str: ...
    def visayas_province_postcode(self) -> str: ...
    def automobile_license_plate(self) -> str:
        """
        Generate an automobile license plate.

        .. note::
           Cars, SUVs, vans, trucks, and other 4-wheeled civilian vehicles are
           considered automobiles for this purpose.
        """
        ...
    def motorcycle_license_plate(self) -> str:
        """
        Generate a motorcycle license plate.

        .. note::
           Motorcycles and any improvised vehicle with a motorcycle as its base
           are issued motorcycle license plates.
        """
        ...
    def protocol_license_plate(self) -> str:
        """
        Generate a protocol license plate.

        .. note::
           High ranking government officials are entitled to use low numbered
           protocol license plates.
        """
        ...
    def company_type(self) -> str: ...
    def random_company_acronym(self) -> str: ...
    def random_company_adjective(self) -> str: ...
    def random_company_noun_chain(self) -> str: ...
    def random_company_product(self) -> str: ...
    def english_paragraph(self, nb_sentences: int = ..., variable_nb_sentences: bool = ...) -> str:
        """
        Generate a paragraph in English.

        :sample: nb_sentences=5
        :sample: nb_sentences=5, variable_nb_sentences=False
        """
        ...
    def english_paragraphs(self, nb: int = ...) -> List[str]:
        """
        Generate a list of paragraphs in English.

        :sample: nb=5
        """
        ...
    def english_sentence(self, nb_words: int = ..., variable_nb_words: bool = ...) -> str:
        """
        Generate a sentence in English.

        :sample: nb_words=10
        :sample: nb_words=10, variable_nb_words=False
        """
        ...
    def english_sentences(self, nb: int = ...) -> List[str]:
        """
        Generate a list of sentences in English.

        :sample: nb=5
        """
        ...
    def english_text(self, max_nb_chars: int = ...) -> str:
        """
        Generate a text string in English.

        :sample: max_nb_chars=20
        :sample: max_nb_chars=80
        :sample: max_nb_chars=160
        """
        ...
    def english_texts(self, nb_texts: int = ..., max_nb_chars: int = ...) -> List[str]:
        """
        Generate a list of text strings in English.

        :sample: nb_texts=5
        :sample: nb_texts=5, max_nb_chars=50
        """
        ...
    def english_word(self) -> str:
        """
        Generate an English word.
        """
        ...
    def english_words(self, nb: int = ..., unique: bool = ...) -> List[str]:
        """
        Generate a list of English words.

        :sample: nb=5
        :sample: nb=5, unique=True
        """
        ...
    def gemstone_name(self) -> str: ...
    def mountain_name(self) -> str: ...
    def plant_name(self) -> str: ...
    def random_object_name(self) -> str: ...
    def space_object_name(self) -> str: ...
    def area2_landline_number(self) -> str: ...
    def bayantel_area2_landline_number(self) -> str: ...
    def bayantel_landline_identifier(self) -> str: ...
    def globe_area2_landline_number(self) -> str: ...
    def globe_mobile_number(self) -> str: ...
    def globe_mobile_number_prefix(self) -> str: ...
    def misc_area2_landline_number(self) -> str: ...
    def misc_landline_identifier(self) -> str: ...
    def mobile_number(self) -> str: ...
    def non_area2_landline_area_code(self) -> str: ...
    def non_area2_landline_number(self) -> str: ...
    def pldt_area2_landline_number(self) -> str: ...
    def smart_mobile_number(self) -> str: ...
    def smart_mobile_number_prefix(self) -> str: ...
    def sun_mobile_number(self) -> str: ...
    def sun_mobile_number_prefix(self) -> str: ...
    def gsis(self) -> str: ...
    def pagibig(self) -> str: ...
    def philhealth(self) -> str: ...
    def sss(self) -> str: ...
    def umid(self) -> str: ...
    def municipality(self) -> str:
        """
        :example: "La Plata"
        """
        ...
    def municipality_code(self) -> str:
        """
        :example: "1900"
        """
        ...
    def provinces_code(self) -> str:
        """
        :example: "BA"
        """
        ...
    def street_municipality(self) -> str:
        """
        :example: "La Plata"
        """
        ...
    def street_procer(self) -> str:
        """
        :example: "Belgrano"
        """
        ...
    def street_province(self) -> str:
        """
        :example: "San Juan"
        """
        ...
    def license_plate_mercosur(self) -> str:
        """
        Generate an new plate with Mercosur format. Since 2016
        """
        ...
    def license_plate_old(self) -> str:
        """
        Generate an old format license plate. Since 1995 to 2016
        """
        ...
    def cif(self) -> str:
        """
        https://es.wikipedia.org/wiki/C%C3%B3digo_de_identificaci%C3%B3n_fiscal
        :return: a random Spanish CIF
        """
        ...
    def doi(self) -> str:
        """
        https://es.wikipedia.org/wiki/Identificador_de_objeto_digital
        :return: a random Spanish CIF or NIE or NIF
        """
        ...
    def nie(self) -> str:
        """
        https://es.wikipedia.org/wiki/N%C3%BAmero_de_identidad_de_extranjero
        :return: a random Spanish NIE
        """
        ...
    def nif(self) -> str:
        """
        https://es.wikipedia.org/wiki/N%C3%BAmero_de_identificaci%C3%B3n_fiscal
        :return: NIF
        """
        ...
    def nuss(self, company: bool = ...) -> str:
        """
        :param company: flag to indicate if we should generate a company NUSS
        :return: a random Spanish Social Security Number (Número de la Seguridad Social)
        """
        ...
    def common_street_name(self) -> str: ...
    def commune(self) -> str: ...
    def commune_and_region(self) -> str: ...
    def commune_code(self) -> str: ...
    def highway_name(self) -> str: ...
    def historic_people_street_name(self) -> str: ...
    def plant_street_name(self) -> str: ...
    def province_code(self) -> str: ...
    def region_code(self) -> str: ...
    def road_name(self) -> str: ...
    def license_plate_diplomatic(self) -> str: ...
    def license_plate_new(self) -> str: ...
    def license_plate_police(self) -> str: ...
    def license_plate_temporary(self) -> str: ...
    def company_prefix(self) -> str:
        """
        :example: 'Grupo'
        """
        ...
    def given_name(self) -> str:
        """
        Generates a composite given name with two unique names
        """
        ...
    def given_name_female(self) -> str:
        """
        Generates a composite female given name with two unique names
        """
        ...
    def given_name_male(self) -> str:
        """
        Generates a composite male given name with two unique names
        """
        ...
    def cellphone_block(self) -> str: ...
    def landline_code(self) -> str: ...
    def special_code(self) -> str: ...
    def company_rut(self) -> str:
        """
        :return: a random Chilean RUT between 60.000.000 and 99.999.999
        """
        ...
    def person_rut(self) -> str:
        """
        :return: a random Chilean RUT between a 10 and 31.999.999 range
        """
        ...
    def rut(self, min: int = ..., max: int = ...) -> str:
        """
        Generates a RUT within the specified ranges, inclusive.

        :param min: Minimum RUT to generate.
        :param max: Maximum RUT to generate.
        :return: a random Chilean RUT between 35.000.000 and 99.999.999
        """
        ...
    def department(self) -> str:
        """
        :example: "Bogotá, D.C."
        """
        ...
    def department_code(self) -> str:
        """
        :example: "11"
        """
        ...
    def legal_person_nit(self) -> str:
        """
        https://es.wikipedia.org/wiki/N%C3%BAmero_de_Identificaci%C3%B3n_Tributaria
        :example: '967807269'
        """
        ...
    def legal_person_nit_with_check_digit(self) -> str:
        """
        :example: '967807269-7'
        """
        ...
    def natural_person_nit(self) -> str:
        """
        https://es.wikipedia.org/wiki/C%C3%A9dula_de_Ciudadan%C3%ADa_(Colombia)
        :example: '1095312769'
        """
        ...
    def natural_person_nit_with_check_digit(self) -> str:
        """
        :example: '1095312769-0'
        """
        ...
    def nuip(self) -> str:
        """
        https://es.wikipedia.org/wiki/C%C3%A9dula_de_Ciudadan%C3%ADa_(Colombia)
        :example: '1095312769'
        """
        ...
    def autonomous_community(self) -> str: ...
    def state_name(self) -> str: ...
    def license_plate_by_province(self, province_prefix: Optional[str] = ...) -> str:
        """
        Generate a provincial license plate.

        If a value for ``province_prefix`` is provided, the value will be used
        as the prefix regardless of validity. If ``None``, then a valid prefix
        will be selected at random.
        """
        ...
    def license_plate_unified(self) -> str:
        """
        Generate a unified license plate.
        """
        ...
    def random_name_complements(self) -> str: ...
    def city_adjective(self) -> str: ...
    def clabe(self, bank_code: Optional[int] = ...) -> str:
        """
        Generate a mexican bank account CLABE.

        Sources:

        - https://en.wikipedia.org/wiki/CLABE

        :return: A fake CLABE number.

        :sample:
        :sample: bank_code=2
        """
        ...
    def curp(self) -> str:
        """
        See https://es.wikipedia.org/wiki/Clave_%C3%9Anica_de_Registro_de_Poblaci%C3%B3n.

        :return: a random Mexican CURP (Unique Population Registry Code)
        """
        ...
    def elector_code(self, gender: Optional[Literal["H", "M"]] = ...) -> str:
        """
        Unique elector code issued by INE (Instituto Nacional Electoral) in Mexico.

        :param gender: Gender for which to generate the code. Will be randomly
            selected if not provided.
        :type gender: str
        :return: a random INE elector code

        :sample:
        :sample: gender='M'
        """
        ...
    def rfc(self, natural: bool = ...) -> str:
        """
        See https://es.wikipedia.org/wiki/Registro_Federal_de_Contribuyentes

        :param natural: Whether to return the RFC of a natural person.
            Otherwise return the RFC of a legal person.
        :type natural: bool
        :return: a random Mexican RFC
        """
        ...
    def first_name_est(self) -> str: ...
    def first_name_female_est(self) -> str: ...
    def first_name_female_rus(self) -> str: ...
    def first_name_male_est(self) -> str: ...
    def first_name_male_rus(self) -> str: ...
    def first_name_rus(self) -> str: ...
    def last_name_est(self) -> str: ...
    def last_name_rus(self) -> str: ...
    def company_business_id(self) -> str:
        """
        Returns Finnish company Business Identity Code (y-tunnus).
        Format is 8 digits - e.g. FI99999999,[8] last digit is a check
        digit utilizing MOD 11-2. The first digit is zero for some old
        organizations. This function provides current codes starting with
        non-zero.
        """
        ...
    def company_vat(self) -> str:
        """
        Returns Finnish VAT identification number (Arvonlisaveronumero).
        This can be calculated from company business identity code by
        adding prefix "FI" and removing dash before checksum.
        """
        ...
    def english_catch_phrase(self) -> str: ...
    def random_good_service_adjective(self) -> str: ...
    def random_good_service_adjective_chain(self) -> str: ...
    def random_noun_ish_good_trait(self) -> str: ...
    def random_object_of_concern(self) -> str: ...
    def catch_phrase_attribute(self) -> str:
        """
        Returns a random catch phrase attribute.
        """
        ...
    def catch_phrase_noun(self) -> str:
        """
        Returns a random catch phrase noun.
        """
        ...
    def catch_phrase_verb(self) -> str:
        """
        Returns a random catch phrase verb.
        """
        ...
    def ide(self) -> str:
        """
        Generates a IDE number (9 digits).
        http://www.bfs.admin.ch/bfs/portal/fr/index/themen/00/05/blank/03/02.html
        """
        ...
    def idi(self) -> str:
        """
        Generates a IDE number (9 digits).
        http://www.bfs.admin.ch/bfs/portal/fr/index/themen/00/05/blank/03/02.html
        """
        ...
    def siren(self) -> str:
        """
        Generates a siren number (9 digits). Formatted as '### ### ###'.
        """
        ...
    def siret(self, max_sequential_digits: int = ...) -> str:
        """
        Generates a siret number (14 digits).
        It is in fact the result of the concatenation of a siren number (9 digits),
        a sequential number (4 digits) and a control number (1 digit) concatenation.
        If $max_sequential_digits is invalid, it is set to 2.

        The siret number is formatted as '### ### ### #####'.
        :param max_sequential_digits The maximum number of digits for the sequential number (> 0 && <= 4).
        """
        ...
    def uid(self) -> str:
        """
        Generates a IDE number (9 digits).
        http://www.bfs.admin.ch/bfs/portal/fr/index/themen/00/05/blank/03/02.html
        """
        ...
    def department_name(self) -> str:
        """
        Randomly returns a french department name.
        :example: 'Ardèche'
        """
        ...
    def department_number(self) -> str:
        """
        Randomly returns a french department number.

        :example: '59'
        """
        ...
    def area_code_with_separator(self) -> str: ...
    def area_code_without_separator(self) -> str: ...
    def street_title(self) -> str: ...
    def city_part(self) -> str: ...
    def frequent_street_name(self) -> str: ...
    def real_city_name(self) -> str: ...
    def street_address_with_county(self) -> str: ...
    def first_name_female_abbreviated(self) -> str: ...
    def first_name_male_abbreviated(self) -> str: ...
    def village_prefix(self) -> str:
        """
        :example: 'գ.'
        """
        ...
    def postcode_city_province(self) -> str: ...
    @staticmethod
    def is_leap_year(year: int) -> bool:
        """
        Checks if the one given is a leap year
        """
        ...
    def ban(self) -> str:
        """
        :example: '3番'
        """
        ...
    def chome(self) -> str:
        """
        :example: '1丁目'
        """
        ...
    def gou(self) -> str:
        """
        :example: '10号'
        """
        ...
    def prefecture(self) -> str:
        """
        :example: '東京都'
        """
        ...
    def jan(self, length: int = ...) -> str:
        """
        Generate a JAN barcode of the specified ``length``.

        This method is an alias for |JaJpProvider.localized_ean|.

        :sample:
        :sample: length=8
        :sample: length=13
        """
        ...
    def jan13(self) -> str:
        """
        Generate a 13 digit JAN barcode.

        This method is an alias for |JaJpProvider.localized_ean13|.
        """
        ...
    def jan8(self) -> str:
        """
        Generate a 8 digit JAN barcode.

        This method is an alias for |JaJpProvider.localized_ean8|.
        """
        ...
    def company_category(self) -> str: ...
    def traditional_month_name(self) -> str: ...
    def first_kana_name(self) -> str:
        """
        :example: 'アケミ'
        """
        ...
    def first_kana_name_female(self) -> str:
        """
        :example: 'アケミ'
        """
        ...
    def first_kana_name_male(self) -> str:
        """
        :example: 'アキラ'
        """
        ...
    def first_name_female_pair(self) -> Tuple[str, str, str]:
        """
        :example: ('明美', 'アケミ', 'Akemi')
        """
        ...
    def first_name_male_pair(self) -> Tuple[str, str, str]:
        """
        :example: ('晃', 'アキラ', 'Akira')
        """
        ...
    def first_name_pair(self) -> Tuple[str, str, str]:
        """
        :example: ('明美', 'アケミ', 'Akemi')
        """
        ...
    def first_romanized_name(self) -> str:
        """
        :example: 'Akemi'
        """
        ...
    def first_romanized_name_female(self) -> str:
        """
        :example: 'Akemi'
        """
        ...
    def first_romanized_name_male(self) -> str:
        """
        :example: 'Akira'
        """
        ...
    def kana_name(self) -> str:
        """
        :example: 'サトウ アケミ'
        """
        ...
    def kana_name_female(self) -> str:
        """
        :example: 'サトウ アケミ'
        """
        ...
    def kana_name_male(self) -> str:
        """
        :example: 'サトウ アキラ'
        """
        ...
    def last_kana_name(self) -> str:
        """
        :example: 'サトウ'
        """
        ...
    def last_name_pair(self) -> Tuple[str, str, str]:
        """
        :example: ('佐藤', 'サトウ', 'Sato')
        """
        ...
    def last_romanized_name(self) -> str:
        """
        :example: 'Sato'
        """
        ...
    def romanized_name(self) -> str:
        """
        :example: 'Akemi Sato'
        """
        ...
    def romanized_name_female(self) -> str:
        """
        :example: 'Akemi Sato'
        """
        ...
    def romanized_name_male(self) -> str:
        """
        :example: 'Akira Sato'
        """
        ...
    def address_detail(self) -> str:
        """
        :example: 가나아파트 가동 102호
        """
        ...
    def borough(self) -> str:
        """
        :example: 중구
        """
        ...
    def building_dong(self) -> str:
        """
        :example: 가
        """
        ...
    def building_suffix(self) -> str:
        """
        :example: 아파트
        """
        ...
    def land_address(self) -> str:
        """
        :example: 세종특별자치시 어진동 507
        """
        ...
    def land_number(self) -> str:
        """
        :example: 507
        """
        ...
    def metropolitan_city(self) -> str:
        """
        :example: 서울특별시
        """
        ...
    def old_postal_code(self) -> str:
        """
        :example: 123-456
        """
        ...
    def postal_code(self) -> str:
        """
        :example: 12345
        """
        ...
    def road(self) -> str:
        """
        :example: 도움5로
        """
        ...
    def road_address(self) -> str:
        """
        :example: 세종특별자치시 도움5로 19 (어진동)
        """
        ...
    def road_number(self) -> str:
        """
        :example: 24
        """
        ...
    def road_suffix(self) -> str:
        """
        :example: 길
        """
        ...
    def town_suffix(self) -> str:
        """
        :example: 동
        """
        ...
    def building_prefix(self) -> str:
        """
        :example: वडा
        """
        ...
    def license_plate_car(self) -> str:
        """
        Generate a license plate for cars.
        """
        ...
    def license_plate_motorbike(self) -> str:
        """
        Generate a license plate for motorbikes.
        """
        ...
    def first_name_unisex(self) -> str: ...
    def middle_name(self) -> str: ...
    def license_plate_regex_formats(self) -> List[str]:
        """
        Return a regex for matching license plates.

        .. warning::
           This is technically not a method that generates fake data, and it
           should not be part of the public API. User should refrain from using
           this method.
        """
        ...
    def local_regon(self) -> str:
        """
        Returns 14 character Polish National Business Registry Number,
        local entity number.

        https://pl.wikipedia.org/wiki/REGON
        """
        ...
    def regon(self) -> str:
        """
        Returns 9 character Polish National Business Registry Number,
        Polish: Rejestr Gospodarki Narodowej - REGON.

        https://pl.wikipedia.org/wiki/REGON
        """
        ...
    def identity_card_number(self) -> str:
        """
        Returns 9 character Polish Identity Card Number,
        Polish: Numer Dowodu Osobistego.

        The card number consists of 3 letters followed by 6 digits (for example, ABA300000),
        of which the first digit (at position 3) is the check digit.

        https://en.wikipedia.org/wiki/Polish_identity_card
        """
        ...
    def nip(self) -> str:
        """
        Returns 10 digit of Number of tax identification.
        Polish: Numer identyfikacji podatkowej (NIP).

        https://pl.wikipedia.org/wiki/NIP
        list of codes
        http://www.algorytm.org/numery-identyfikacyjne/nip.html
        """
        ...
    def pesel(self, date_of_birth: Optional[datetime.datetime] = ..., sex: Optional[str] = ...) -> str:
        """
        Returns 11 characters of Universal Electronic System for Registration of the Population.
        Polish: Powszechny Elektroniczny System Ewidencji Ludności.

        PESEL has 11 digits which identifies just one person.
        pesel_date: if person was born in
            * 1900-1999 - month field number is not modified
            * 2000–2099 – month field number is increased by 20
            * 2100–2199 – month + 40
            * 2200–2299 – month + 60
            * 1800–1899 – month + 80
            * outside range 1800-2299 function will raise ValueError

        pesel_sex: last digit identifies person's sex. Even for females, odd for males.

        https://en.wikipedia.org/wiki/PESEL
        """
        ...
    def pesel_compute_check_digit(self, pesel: str) -> int: ...
    def pwz_doctor(self) -> str:
        """
        Function generates an identification number for medical doctors
        Polish: Prawo Wykonywania Zawodu (PWZ)

        https://www.nil.org.pl/rejestry/centralny-rejestr-lekarzy/zasady-weryfikowania-nr-prawa-wykonywania-zawodu
        """
        ...
    def pwz_doctor_compute_check_digit(self, x: Sequence[int]) -> int: ...
    def pwz_nurse(self, kind: str = ...) -> str:
        """
        Function generates an identification number for nurses and midwives
        Polish: Prawo Wykonywania Zawodu (PWZ)

        http://arch.nipip.pl/index.php/prawo/uchwaly/naczelnych-rad/w-roku-2015/posiedzenie-15-17-grudnia/3664-uchwala-
        nr-381-vi-2015-w-sprawie-trybu-postepowania-dotyczacego-stwierdzania-i-przyznawania-prawa-wykonywania-zawodu-pi
        elegniarki-i-zawodu-poloznej-oraz-sposobu-prowadzenia-rejestru-pielegniarek-i-rejestru-poloznych-przez-okregowe
        -rady-pielegniarek-i-polo
        """
        ...
    def bairro(self) -> str:
        """
        Randomly returns a bairro (neighborhood) name.
        The names were taken from the city of Belo Horizonte - Minas Gerais
        :example: 'Serra'
        """
        ...
    def estado(self) -> Tuple[str, str]:
        """
        Randomly returns a Brazilian State  ('sigla' , 'nome').
        :example: ('MG' . 'Minas Gerais')
        """
        ...
    def estado_nome(self) -> str:
        """
        Randomly returns a Brazilian State Name
        :example: 'Minas Gerais'
        """
        ...
    def estado_sigla(self) -> str:
        """
        Randomly returns the abbreviation of a Brazilian State
        :example: 'MG'
        """
        ...
    def neighborhood(self) -> str: ...
    def cnpj(self) -> str: ...
    def company_id(self) -> str: ...
    def cpf(self) -> str: ...
    def rg(self) -> str:
        """
        Brazilian RG, return plain numbers.
        Check:  https://www.ngmatematica.com/2014/02/como-determinar-o-digito-verificador-do.html
        """
        ...
    def concelho(self) -> str:
        """
        :example: 'Tondela'
        """
        ...
    def distrito(self) -> str:
        """
        :example: 'Bragança'
        """
        ...
    def freguesia(self) -> str:
        """
        :example: 'Miranda do Douro'
        """
        ...
    def place_name(self) -> str:
        """
        :example: "do Pombal"
        """
        ...
    def nationality(self) -> str:
        """
        :example: 'Portuguesa'
        """
        ...
    def plate_letter(self) -> str:
        """
        Generate a letter for license plates.
        """
        ...
    def plate_number(self) -> str:
        """
        Generate a number for license plates.
        """
        ...
    def plate_number_extra(self) -> str:
        """
        Generate extra numerical code for license plates.
        """
        ...
    def plate_number_special(self) -> str:
        """
        Generate a special code for license plates.
        """
        ...
    def plate_suffix(self) -> str:
        """
        Generate a suffix code for license plates.
        """
        ...
    def vehicle_category(self) -> str:
        """
        Generate a vehicle category code for license plates.
        """
        ...
    def bic(self) -> str:
        """
        Generate a bank identification code (BIC).

        BIC is a bank identification code that is used in Russia.
        See https://ru.wikipedia.org/wiki/Банковский_идентификационный_код.
        """
        ...
    def checking_account(self) -> str:
        """
        Generate a checking account number.

        Checking account is used in banks to handle financial operations of
        clients.
        See https://ru.wikipedia.org/wiki/Расчётный_счёт.
        """
        ...
    def correspondent_account(self) -> str:
        """
        Generate a correspondent account number.

        Correspondent account is established to handle various financial
        operations between financial institutions.
        See https://ru.wikipedia.org/wiki/Корреспондентский_счёт.
        """
        ...
    def businesses_inn(self) -> str:
        """
        Returns tax identification number for businesses (ru. идентификационный номер налогоплательщика, ИНН).
        """
        ...
    def businesses_ogrn(self) -> str:
        """
        Returns primary state registration number for businesses
        (ru. основной государственный регистрационный номер, ОГРН).
        """
        ...
    def individuals_inn(self) -> str:
        """
        Returns tax identification number for individuals (ru. идентификационный номер налогоплательщика, ИНН).
        """
        ...
    def individuals_ogrn(self) -> str:
        """
        Returns primary state registration number for individuals
        (ru. основной государственный регистрационный номер, ОГРН).
        """
        ...
    def kpp(self) -> str:
        """
        Returns tax registration reason code (ru. код причины постановки на учет, КПП).
        """
        ...
    def middle_name_female(self) -> str: ...
    def middle_name_male(self) -> str: ...
    def org_and_vat_id(self, long: bool = ..., dash: bool = ...) -> Tuple[str, str]:
        """
        Returns matching Org ID and VAT number
        """
        ...
    def org_id(self, long: bool = ..., dash: bool = ...) -> str:
        """
        Returns a 10 or 12 digit Organisation ID for a Swedish
        company.
        (In Swedish) https://sv.wikipedia.org/wiki/Organisationsnummer
        """
        ...
    def amphoe(self) -> str:
        """
        Get a random Amphoe (district) name.
        Currently it's total random and not necessarily matched with a province.
        :example: 'บางสะพานน้อย'
        """
        ...
    def tambon(self) -> str:
        """
        Get a random Tambon (subdistrict) name.
        Currently it's total random and not necessarily matched with an amphoe or province.
        :example: 'ห้วยนาง'
        """
        ...
    def company_limited_prefix(self) -> str:
        """
        :example: 'บริษัท'
        """
        ...
    def company_limited_suffix(self) -> str:
        """
        :example: 'จำกัด'
        """
        ...
    def nonprofit_prefix(self) -> str:
        """
        :example: 'มูลนิธิ'
        """
        ...
    def diplomatic_license_plate(self) -> str:
        """
        Example: 'CDP 000'  or 'DP 000 000' or 'S 000 000' format

        :sample:
        """
        ...
    def plate_letter_prefix(self, region_name: Optional[str] = ...) -> str:
        """
        Generate a letter for license plates.

        :sample:
        :sample: region_name="Kyiv"
        """
        ...
    def plate_letter_suffix(self) -> str:
        """
        Generate a end letter for license plates.

        :sample:
        """
        ...
    def plate_region_code(self, region_name: Optional[str] = ...) -> str:
        """
        Generate plate region number

        :sample:
        :sample: region_name="Kyiv"
        """
        ...
    def full_name(self, gender: Optional[Literal["M", "F"]] = ..., short: Optional[bool] = ...) -> str:
        """
        Generate Full Name
            - gender = 'M' or 'F' optional params
            - short: bool optional params. default is False

        :example: 'Петриченко Петро Сергійович'
        :example: 'Петриченко П.С.'

        :sample:
        :sample: gender='F'
        :sample: gender='M'
        :sample: short=True
        """
        ...
    def phonenumber_prefix(self) -> int: ...
    def city_name_suffix(self) -> str: ...
    def section_number(self) -> str: ...
    def street_name_suffix(self) -> str: ...
    def minguo_year(self) -> str: ...
    def __deepcopy__(self, memodict): ...
    def __dir__(self):
        """
        Default dir() implementation.
        """
        ...
    def __getattr__(self, attr: "str") -> "Any":
        """
        Handles cache access and proxying behavior

        :param attr: attribute name
        :return: the appropriate attribute
        """
        ...
    def __getattribute__(self, attr: "str") -> "Any":
        """
        Handles the "attribute resolution" behavior for declared members of this proxy class

        The class method `seed` cannot be called from an instance.

        :param attr: attribute name
        :return: the appropriate attribute
        """
        ...
    def __getitem__(self, locale: "str") -> "Faker": ...
    def __init__(
        self,
        locale: "str | Sequence[str] | dict[str, int | float] | None" = ...,
        providers: "list[str] | None" = ...,
        generator: "Generator | None" = ...,
        includes: "list[str] | None" = ...,
        use_weighting: "bool" = ...,
        **config: "Any"
    ) -> "None":
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
    def __setstate__(self, state: "Any") -> "None": ...
    def items(self) -> "list[tuple[str, Generator | Faker]]": ...
    @staticmethod
    def seed(seed: "SeedType | None" = ...) -> "None":
        """
        Hashables the shared `random.Random` object across all factories

        :param seed: seed value
        """
        ...
    def seed_instance(self, seed: "SeedType | None" = ...) -> "None":
        """
        Creates and seeds a new `random.Random` object for each factory

        :param seed: seed value
        """
        ...
    def seed_locale(self, locale: "str", seed: "SeedType | None" = ...) -> "None":
        """
        Creates and seeds a new `random.Random` object for the factory of the specified locale

        :param locale: locale string
        :param seed: seed value
        """
        ...
