'''
https://py.checkio.org/en/mission/currency-style/

Currency Style
 Elementary+
English
 "Well, it's that time of the month again. Payroll checks for our employees,
 which require your signatures. And no forgetting to sign the big ones!" --
 Trading Places

Many countries use different conventions for the thousands separator and
decimal mark. For example in the Netherlands one million one thousand two
hundred and eighty one-hundredths is written as 1.001.200,80, but in the US
this is written as 1,001,200.80. Use your coding skills to convert dollars in
the first style (Netherlands, Germany, Russia, Turkey, Brazil, and others) to
the second style (US, UK, Canada, China, Japan, Mexico, and others).

Only currency amounts in dollars should be converted: $1.234,50 to $1,234.50,
$1.000 to $1,000, and $4,57 to $4.57. Don't accidentally convert your router's
IP address 192.168.1.1. You should leave currency noted in the US style
unchanged.

Input: A string containing dollar amounts to be converted.

Output: A string with converted currencies.

Example:

checkio("Lot 192.001 costs $1.000,94.") == "Lot 192.001 costs $1,000.94."
checkio("$1,23 + $2,34 = $3,57.") == "$1.23 + $2.34 = $3.57."
1
2
How it is used: This is an exercise in working with strings and using the
Python standard library.

Precondition: 0 < len(text) ≤ 1000;
len(fractional_part_of_currency) in {0,2};
all(s[-1].isdigit() for s in currency_substrings);
all(s[0] == '$' for s in currency_substrings)
'''

import re


def checkio(text):
    if re.search(r'\d{3}\.\d{3}\.\d{3}\.\d{3}', text):
        return text
    else:
        return re.sub(r'\.(?=\d{3}\b)', ',',
                      re.sub(r'\,(?=\d{2}\b)', '.', text))


if __name__ == '__main__':

    assert checkio("$1.234.567,89") == "$1,234,567.89", "1st Example"

    assert checkio("$0,89") == "$0.89", "2nd Example"

    assert checkio("Euro Style = $12.345,67, US Style = $12,345.67") == \
        "Euro Style = $12,345.67, US Style = $12,345.67",\
        "European and US"

    assert checkio("Us Style = $12,345.67, Euro Style = $12.345,67") == \
        "Us Style = $12,345.67, Euro Style = $12,345.67", "US and European"

    assert checkio("$1.234, $5.678 and $9") == \
        "$1,234, $5,678 and $9", "Dollars without cents"
