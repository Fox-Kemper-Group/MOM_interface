import os, sys

CIMEROOT = os.environ.get("CIMEROOT")
if CIMEROOT is None:
    raise SystemExit("ERROR: must set CIMEROOT environment variable")
sys.path.append(os.path.join(CIMEROOT, "scripts", "lib", "CIME", "ParamGen"))
from paramgen import ParamGen

class FType_input_nml(ParamGen):
    """Encapsulates data and read/write methods for MOM6 (FMS) input.nml file"""

    def write(self, output_path, case):

        self.reduce(lambda varname: case.get_value(varname))
        self.write_nml(output_path)