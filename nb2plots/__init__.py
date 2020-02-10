# nb2plots package

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from . import nbplots
from . import runroles
from . import mpl_interactive
from . import codelinks
from . import sphinx2foos


def setup(app):
    nbplots.setup(app)
    runroles.setup(app)
    mpl_interactive.setup(app)
    codelinks.setup(app)
    sphinx2foos.setup(app)
    return {"version": __version__,
            "parallel_read_safe": True,
            "parallel_write_safe": True}
