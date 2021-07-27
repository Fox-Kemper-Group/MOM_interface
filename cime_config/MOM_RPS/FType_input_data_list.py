import os, sys

CIMEROOT = os.environ.get("CIMEROOT")
if CIMEROOT is None:
    raise SystemExit("ERROR: must set CIMEROOT environment variable")
sys.path.append(os.path.join(CIMEROOT, "scripts", "lib", "CIME", "ParamGen"))
from paramgen import ParamGen

class FType_input_data_list(ParamGen):
    """Encapsulates data and read/write methods for MOM6 input_data_list file."""

    def write(self, output_path, case, MOM_input_final=None):

        def expand_func(varname):
            val = case.get_value(varname)
            if val==None:
                val = MOM_input_final.data['Global'][varname]['value'].strip()
            if val==None:
                raise RuntimeError("Cannot determine the value of variable: "+varname)
            return val

        # Reduce Param Data
        self.reduce(expand_func)


        with open(os.path.join(output_path), 'w') as input_data_list:
            for module in self._data:
                for file_category in self._data[module]:
                    file_path = self._data[module][file_category]
                    if file_path != None:
                        file_path = file_path.replace('"','').replace("'","").strip()
                        if os.path.isabs(file_path):
                            input_data_list.write(file_category+" = "+file_path+"\n")
                        else:
                            pass # skip if custom INPUTDIR is used.

