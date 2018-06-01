test = {
    'name': 'THE NAME OF THE TEST/QUESTION',
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> import re
                    >>> test_string = 'Call me maybe? 510-123-4567'
                    >>> match = re.search(phone_number_pattern, test_string)
                    >>> bool(match)
                    True
                    """
                }
            ]
        }
    ]
}