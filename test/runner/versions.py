#!/usr/bin/env python
"""Show python and pip versions."""

import os
import sys

try:
    import pip
except ImportError:
    pip = None

print('.'.join(u'%s' % i for i in sys.version_info))

if pip:
    print('pip %s from %s' % (pip.__version__, os.path.dirname(pip.__file__)))
