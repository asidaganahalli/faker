import logging

from faker.providers.bank import Provider as BankProvider

logger = logging.getLogger(__name__)


class Provider(BankProvider):
    country_code = 'PH'
    bban_format = '################'
    swift_bank_codes = (
        'ANZB', 'AUBK', 'BKCH', 'BKKB', 'BNOR', 'BNPA', 'BOFA', 'BOPI',
        'BOTK', 'BPDI', 'BPFS', 'BPGO', 'CHAS', 'CHBK', 'CHSV', 'CITI',
        'CPHI', 'CTCB', 'DBPH', 'DEUT', 'EQSN', 'EWBC', 'FCBK', 'HBPH',
        'HNBK', 'HSBC', 'IBKO', 'ICBC', 'INGB', 'KOEX', 'MBBE', 'MBTC',
        'MHCB', 'PABI', 'PHSB', 'PHTB', 'PHVB', 'PNBM', 'PPBU', 'RCBC',
        'ROBP', 'SCBL', 'SETC', 'SHBK', 'SMBC', 'STLA', 'TACB', 'TLBP',
        'TYBK', 'UBPH', 'UCPB', 'UOVB', 'UWCB',
    )
    swift_location_codes = (
        '22', '2X', 'M1',
        'MM', 'MQ', 'MX',
    )
    swift_branch_codes = (
        'CBU', 'EQI', 'TSU', 'XXX',
    )

    def bban(self):
        """Generate a BBAN

        .. warning::

           Philippine bank accounts do not have BBANs or IBANs, so any number generated by this
           method is a purely hypothetical number. Local bank account numbers are typically 10
           or 12 digits long, so the BBAN format used in this implementation has been arbitrarily
           set to 16 digits to simulate a hypothetical standardization of account numbers. Using
           this method will also log a warning regarding the hypotheticality of the result.

        :sample:
        """
        logger.warning("Numbers generated by this method are purely hypothetical.")
        return super().bban()

    def iban(self):
        """Generate a BBAN

        .. warning::

           Philippine bank accounts do not have BBANs or IBANs, so any number generated by this
           method is a purely hypothetical number. This method uses hypothetical PH BBANs and the
           PH country code as inputs to the IBAN generation algorithm. Using this method will also
           log a warning regarding the hypotheticality of the result.

        :sample:
        """
        logger.warning("Numbers generated by this method are purely hypothetical.")
        return super().iban()
