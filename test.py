import pytest
from library import *

def test_quality_to_probability():
    assert(quality_to_probability("ACCGGGGGFG") == [0.00063096, 0.00039811, 0.00039811,
                                                    0.00015849, 0.00015849, 0.00015849,
                                                    0.00015849, 0.00015849, 0.00019953,
                                                    0.00015849])
