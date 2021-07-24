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

        with open(os.path.join(output_path), 'w') as input_nml:
            for module in self._data:
                input_nml.write("&"+module+"\n")

                for var in self._data[module]:
                    val = self._data[module][var]["value"]
                    if val==None:
                        continue
                    input_nml.write("    "+var+" = "+str(self._data[module][var]["value"])+"\n")

                input_nml.write('/\n\n')

