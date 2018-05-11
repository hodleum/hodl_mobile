'''
Plyer
=====

'''

__all__ = ('orientation', 'proximity')

__version__ = '1.2.5dev'


from plyer import facades
from plyer.utils import Proxy


#: Orientation proxy to :class:`plyer.facades.Orientation`
orientation = Proxy('orientation', facades.Orientation)
#: Proximity proxy to :class:`plyer.facades.Proximity`
proximity = Proxy('proximity', facades.Proximity)
