from mangopi.helper.decorators import memoize
from mangopi.helper.util import Util


class HasUrl(object):
    @property
    @memoize
    def source(self):
        return Util.getSourceCode(self.url)
