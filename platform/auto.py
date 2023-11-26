import sys

if sys.platform == 'darwin':
    from platform.darwin import *
else:
    raise NotImplementedError('Unsupported platform: {}'.format(sys.platform))
