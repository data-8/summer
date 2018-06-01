test = {
    'name': 'Euclidean algorithm',
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> gcd(200, 15)
                    5
                    """
                },
                {
                    'code': r"""
                    >>> gcd(200, 14)
                    2
                    """
                },
                {
                    'code': r"""
                    >>> gcd(19, 201)
                    1
                    >>> gcd(19, 201) # Wrong
                    12
                    """
                }
            ]
        }
    ]
}
