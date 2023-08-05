try:
    from ._version import __version__
except ImportError:
    __version__ = __А те зачем?__'

from .events import *
from . import dispatcher as dp
from .database import db
