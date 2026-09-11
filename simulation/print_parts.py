"""Author-supplied print geometry for the three unreliable STEP tessellations.

No mesh repair: these are the standard upstream print files, in the same local
frames. Exact tests deliberately use the faceted backend at these interfaces.
See docs/measurements.md for the source comparison and boolean findings.
"""

from pathlib import Path
from solid_node.node import StlNode

PRINTS = Path(__file__).resolve().parents[1] / 'STLs'


class DigitsCover(StlNode):
    part = 'digits cover'
    stl_source = str(PRINTS / '42 - Digit Cover & Upper Housing/digits cover.stl')
    color = '#263846'


class UpperHousing(StlNode):
    part = 'upper housing'
    stl_source = str(PRINTS / '42 - Digit Cover & Upper Housing/upper housing.stl')
    color = '#263846'


class CrankCollar(StlNode):
    part = 'crank collar'
    stl_source = str(PRINTS / '43 - Clearing Cover & Collar/crank collar.stl')
    color = '#9aa5af'
