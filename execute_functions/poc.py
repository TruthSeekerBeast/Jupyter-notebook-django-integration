import time

from DVS_Analysis import settings

start_time = time.time()
import nbformat
from nbparameterise import (
    extract_parameters, replace_definitions, parameter_values
)


def get_result(PLOT_KIND, PLOT_HIST_SIZE):
    path = settings.NOTEBOOKS + 'DVS_ANALYSIS.ipynb'
    with open(path) as f:
        nb = nbformat.read(f, as_version=4)

    orig_parameters = extract_parameters(nb)
    params = parameter_values(orig_parameters, **{'PLOT_KIND': PLOT_KIND, 'PLOT_HIST_SIZE': PLOT_HIST_SIZE})

    new_nb = replace_definitions(nb, params, execute=False)

    exec(new_nb.cells[0].source)
    exec(new_nb.cells[2].source)
    exec(new_nb.cells[5].source)

    a = ''
    exec('a = ' + new_nb.cells[6].source)
    # a.savefig('abcd')
    print("--- %s seconds ---" % (time.time() - start_time))
    return a
