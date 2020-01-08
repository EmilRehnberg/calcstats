__title__ = "calcstats"
__version__ = "0.0.1"
__date__ = "2020-01-07"
__author__ = "Emil Rehnberg"
__email__ = "emil.rehnberg@gmail.com"
__contact__ = "emil.rehnberg@gmail.com"
__license__ = "MIT"
__copyright__ = "Copyright 2020 by Emil"
__maintainer__ = "Emil Rehnberg"
__credits__ = ["Emil Rehnberg", "Joel Grus"]
__status__ = "development"

__doc__ = """
Calculate some stats package.

Main Features
-------------

- mean
- median
- etc....
"""

from calcstats.calc import (
    count_nums,
    data_range,
    mean,
    median,
    mode,
    pad_w_zeros,
    quantile,
)
