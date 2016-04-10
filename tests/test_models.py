# -*- coding: utf-8 -*-

from pyyp import models

class TestRequests:
    def test_sms_send_request(self):
        r = models.SMSSendRequest(
                apikey='API_KEY', mobile='13812345678', text='hello')
        assert r.url == 'https://sms.yunpian.com/v2/sms/single_send.json'
        assert r.params == {'apikey': 'API_KEY', 'mobile': '13812345678',
                'text': 'hello'}

    def test_sms_batch_send_request(self):
        r = models.SMSBatchSendRequest(
                apikey='API_KEY',
                mobile='13812345678,13887654321',
                text='hello')
        assert r.url == 'https://sms.yunpian.com/v2/sms/batch_send.json'
        assert r.params == {
                'apikey': 'API_KEY',
                'mobile': '13812345678,13887654321',
                'text': 'hello'
               }
