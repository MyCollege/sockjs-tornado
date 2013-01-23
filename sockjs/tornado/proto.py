# -*- coding: utf-8 -*-
"""
    sockjs.tornado.proto
    ~~~~~~~~~~~~~~~~~~~~

    SockJS protocol related functions
"""
import logging
import tornado.escape

# Use tornado.escape json for encoding and decoding to handle py 2v3 str vs bytes support
json_encode = tornado.escape.json_encode
json_decode = tornado.escape.json_decode

# Protocol handlers
CONNECT = 'o'
DISCONNECT = 'c'
MESSAGE = 'm'
HEARTBEAT = 'h'


# Various protocol helpers
def disconnect(code, reason):
    """Return SockJS packet with code and close reason

    `code`
        Closing code
    `reason`
        Closing reason
    """
    return 'c[%d,"%s"]' % (code, reason)
