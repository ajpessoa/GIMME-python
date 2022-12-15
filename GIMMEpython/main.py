import rdata
import os
import GIMMEpython.gimmeSEM as gs


def run_from_cli(data:str, out: str):
    """function to run gimmeSEM from the command line

    Args:
        data (str): the path to the dataset file (in .rda format)
        out (str): the path to the folder where the output is written
    """
    parsed = rdata.parser.parse_file("GIMMEpython\simDataLV.rda")
    converted = rdata.conversion.convert(parsed)
    res = gs.gimmeSEM_python(converted, out)
    
    return res
