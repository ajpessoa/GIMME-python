import pytest
import rdata
import pandas as pd
from GIMMEpython.gimmeSEM import gimmeSEM_python

def test_gimmeSEM():
    parsed = rdata.parser.parse_file("GIMMEpython\simDataLV.rda")
    converted = rdata.conversion.convert(parsed)
    
    assert isinstance(gimmeSEM_python(converted, ""), list)