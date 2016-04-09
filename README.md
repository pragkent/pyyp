pyyp
====

[![Build Status](https://travis-ci.org/pragkent/pyyp.png?branch=master)](https://travis-ci.org/pragkent/pyyp)

pyyp is a wrapper of the Yunpian SMS API, written in Python.

Installation
------------

Install pyyp with `pip`:
```bash
pip install pyyp
```

Example
-------
```python
import pyyp

yunpian = pyyp.Yunpian(api_key=API_KEY)
yunpian.send(mobile, 'hello yunpian!')

```

TODO
----
- Add unit tests
