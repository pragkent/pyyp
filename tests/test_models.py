# -*- coding: utf-8 -*-

from pyyp import models


def test_sms_send_request():
    r = models.SMSSendRequest(
            apikey='API_KEY', mobile='13812345678', text='hello')
    params = {
        'apikey': 'API_KEY',
        'mobile': '13812345678',
        'text': 'hello'
    }

    assert r.url == 'https://sms.yunpian.com/v2/sms/single_send.json'
    assert r.params == params


def test_sms_batch_send_request():
    r = models.SMSBatchSendRequest(
            apikey='API_KEY',
            mobile='13812345678,13887654321',
            text='hello')

    params = {
        'apikey': 'API_KEY',
        'mobile': '13812345678,13887654321',
        'text': 'hello'
    }

    assert r.url == 'https://sms.yunpian.com/v2/sms/batch_send.json'
    assert r.params == params
