test = {
    'name': 'THE NAME OF THE TEST/QUESTION',
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # Make sure you assigned your answer to a variable called 'phone_number_pattern'.
                    >>> 'phone_number_pattern' in vars()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Remember that phone_number_pattern should be a string.
                    >>> isinstance(phone_number_pattern, str)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # We're just looking for phone numbers without parentheses at the moment!
                    >>> import re
                    >>> test_string = "Don't do anything fancy with parentheses: (510)-123-4567"
                    >>> match = re.search(phone_number_pattern, test_string)
                    >>> bool(match)
                    False
                    """
                },
                {
                    'code': r"""
                    >>> # Are you sure your regular expression is looking for all ten digits?
                    >>> import re
                    >>> test_string = "You shouldn't match on 123-4567 but you should on 510-123-4567"
                    >>> matches = re.findall(phone_number_pattern, test_string)
                    >>> len(matches)
                    1
                    """
                }
            ]
        }
    ]
}