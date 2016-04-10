# -*- coding: utf-8 -*-

from pyyp import utils


def test_encode_params():
    tests = (
        ({'a': 'b'}, 'a=b'),
        ({'a': 'b#'}, 'a=b#'),
        ({'a': 'b', 'apikey': '2fc7ddf68d81440bee7db3710763dc6f'},
         'a=b&apikey=2fc7************************dc6f')
    )

    for params, text in tests:
        assert utils.encode_params(params) == text


def test_mask_api_key():
    tests = (
        ('A', 'AA'),
        ('2fc7ddf68d81440bee7db3710763dc6f',
         '2fc7************************dc6f'),
    )

    for text, want in tests:
        assert utils.mask_api_key(text) == want
