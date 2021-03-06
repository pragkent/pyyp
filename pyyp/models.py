# -*- coding: utf-8 -*-

"""
pyyp.models
~~~~~~~~~~~

This module provides the requests and responses for Yunpian.
"""

import requests

from .exceptions import HTTPError, BadResponse
from .compat import is_py2


class Request(object):
    BASE_URL = 'https://sms.yunpian.com'
    PATH = '/'

    def __init__(self, **kwargs):
        self._params = kwargs

    @property
    def url(self):
        return '%s%s' % (self.BASE_URL, self.PATH)

    @property
    def params(self):
        return self._params


class Response(object):
    @classmethod
    def parse(cls, http_resp):
        """Parse response from http request."""

        try:
            http_resp.raise_for_status()
            data = http_resp.json()
        except requests.exceptions.HTTPError as e:
            msg = '%s: %s' % (e, http_resp.text[:200])
            if is_py2:
                msg = msg.encode('utf-8')
            raise HTTPError(msg)
        except ValueError:
            raise BadResponse('Response is not JSON')

        return cls(**data)


class SMSSendRequest(Request):
    PATH = '/v2/sms/single_send.json'


class SMSSendResponse(Response):
    def __init__(self, **kwargs):
        try:
            self.code = kwargs['code']
            self.msg = kwargs['msg']
            self.count = kwargs['count']
            self.fee = kwargs['fee']
            self.unit = kwargs['unit']
            self.mobile = kwargs['mobile']
            self.sid = kwargs['sid']
        except KeyError as e:
            raise BadResponse('"%s" attribute is missing' % str(e))

    def __repr__(self):
        return ('SMSSendResponse(code={self.code}, msg={self.msg}, '
                'count={self.count}, fee={self.fee}, unit={self.unit}, '
                'mobile={self.mobile}, sid={self.sid})').format(self=self)


class SMSBatchSendRequest(Request):
    PATH = '/v2/sms/batch_send.json'


class SMSBatchSendResponse(Response):
    def __init__(self, **kwargs):
        try:
            self.total_count = kwargs['total_count']
            self.total_fee = kwargs['total_fee']
            self.unit = kwargs['unit']
            self.results = []

            for r in kwargs['data']:
                self.results.append(SMSSendResponse(**r))
        except KeyError as e:
            raise BadResponse('"%s" attribute is missing' % str(e))

    def __repr__(self):
        return ('SMSBatchSendResponse(total_count={self.total_count}, '
                'total_fee={self.total_fee}, unit={self.unit}, '
                'results={self.results})').format(self=self)


class GetBlackWordRequest(Request):
    PATH = '/v2/sms/get_black_word.json'


class GetBlackWordResponse(Response):

    def __init__(self, **kwargs):
        self.http_status_code = kwargs.get('http_status_code', 0)
        self.code = kwargs.get('code', 0)
        self.message = kwargs.get('msg', None)
        self.detail = kwargs.get('detail', None)
        self.results = kwargs.get('results', None)

    def __repr__(self):
        return ('GetBlackWordResponse(http_status_code={self.http_status_code}, '
                'code={self.code}, message={self.message}, detail={self.detail}, '
                'results={self.results})').format(self=self)

    @classmethod
    def parse(cls, http_resp):
        """Parse response from http request, overload."""

        try:
            http_resp.raise_for_status()
            data = http_resp.json()
        except requests.exceptions.HTTPError as e:
            msg = '%s: %s' % (e, http_resp.text[:200])
            if is_py2:
                msg = msg.encode('utf-8')
            raise HTTPError(msg)
        except ValueError:
            raise BadResponse('Response is not JSON')

        if type(data) == list:
            return cls(results=data)
        else:
            return cls(**data)
