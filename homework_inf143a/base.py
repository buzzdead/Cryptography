#!/usr/bin/env python

import base64


def Base64Encode(name):
    # Use a breakpoint in the code line below to debug your script.
    print(base64.b64encode(b'hello\njello'))


Base64Encode('hello\njello')
