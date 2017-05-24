These scripts demonstrate the use of [IMP](https://integrativemodeling.org/),
[MODELLER](https://salilab.org/modeller), and
[PMI](https://github.com/salilab/pmi) in the modeling of the SEA complex using 188 DSS chemical cross-links and 23 composites from affinity purification.

First, [MODELLER](https://salilab.org/modeller) is used to generate
initial structures for the individual components where reliable templates are available. Then, [IMP](https://integrativemodeling.org/) / [PMI](https://github.com/salilab/pmi) are used to model these components using the DSS crosslinks and the affinity purification data for the entire SEA complex.

The scripts work with the 65734ec version (develop branch) of [IMP](https://integrativemodeling.org/) and the 47dafcc version (develop branch) of [PMI](https://github.com/salilab/pmi).

A full description of the scripts can be found in
[Molecular architecture and function of the SEA complex, a modulator of the TORC1 pathway](http://mcponline.org/content/early/2014/07/29/mcp.M114.039388).

## List of files and directories:

- `pdb`	contains all input crystal structures that were deposited in PDB.

- `scripts`
  - `sj_SEA_multi_layers.py`                   The main modeling script with 1:3 stoichiometry and rotational symmetry

  - `MODELLER/Npr2` MODELLER scripts and output comparative models of Npr2

  - `MODELLER/Npr3` MODELLER scripts and output comparative models of Npr3

  - `MODELLER/SEA1` MODELLER scripts and output comparative models of SEA1

  - `MODELLER/SEA2` MODELLER scripts and output comparative models of SEA2

  - `MODELLER/SEA3` MODELLER scripts and output comparative models of SEA3
  
  - `MODELLER/SEA4` MODELLER scripts and output comparative models of SEA4

- `output/three_sym_cluster`

  - Largest output cluster as a set of RMF files. Each file is named
    `XX_REFINED_models_YY.rmf` where `XX` identifies the run from which the
    model was taken and `YY` the frame number. For the publication, 885 runs
    were carried out.

  - `global` Localization densities in MRC format and a Chimera session file
    (`Chimera_three_sym.py`) to display them.

## Running the MODELLER scripts:
- `cd scripts/MODELLER/Npr2 && python all_sjkim_final1.py` : Npr2 9-127
- `cd scripts/MODELLER/Npr2 && python all_sjkim_final2.py` : Npr2 257-327
- `cd scripts/MODELLER/Npr2 && python all_sjkim_final3.py` : Npr2 563-610
- `cd scripts/MODELLER/Npr3 && python all_sjkim_final1.py` : Npr3 322-438
- `cd scripts/MODELLER/Npr3 && python all_sjkim_final2.py` : Npr3 531-577
- `cd scripts/MODELLER/Npr3 && python all_sjkim_final3.py` : Npr3 1-31
- `cd scripts/MODELLER/Npr3 && python all_sjkim_final4.py` : Npr3 950-988
- `cd scripts/MODELLER/Npr3 && python all_sjkim_final5.py` : Npr3 1083-1140
- `cd scripts/MODELLER/SEA1 && python all_sjkim_final1.py` : SEA1 101-275
- `cd scripts/MODELLER/SEA1 && python all_sjkim_final2.py` : SEA1 279-473
- `cd scripts/MODELLER/SEA1 && python all_sjkim_final3.py` : SEA1 1178-1273
- `cd scripts/MODELLER/SEA2 && python all_sjkim_final1.py` : SEA2 127-520
- `cd scripts/MODELLER/SEA2 && python all_sjkim_final2.py` : SEA2 1280-1341
- `cd scripts/MODELLER/SEA3 && python all_sjkim_final1.py` : SEA3 54-424
- `cd scripts/MODELLER/SEA3 && python all_sjkim_final2.py` : SEA3 430-536
- `cd scripts/MODELLER/SEA3 && python all_sjkim_final3.py` : SEA3 1092-1139
- `cd scripts/MODELLER/SEA4 && python all_sjkim_final1.py` : SEA4 45-426
- `cd scripts/MODELLER/SEA4 && python all_sjkim_final2.py` : SEA4 659-835
- `cd scripts/MODELLER/SEA4 && python all_sjkim_final3.py` : SEA4 942-1032


## Running the IMP/PMI scripts for the SEA complex:

To produce a single model with 1:3 stoichiometry and rotational
symmetry, as in the publication, use the `run_qsub.sh` script:

    run_qsub.sh 50000 20000 3 True

For the publication, this script was run 885 times to generate the final
ensemble, which was then clustered to produce the 340 models in the `output`
directory.

This script in turn runs `scripts/sj_SEA_multi_layers.py`, which if desired
can be run with different options to explore other representations and sampling
options.

## Information

_Author(s)_: Seung Joong Kim, Riccardo Pellarin, and Peter Cimermancic

_Date_: October 6th, 2014

_License_: [LGPL](http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html).
This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

_Last known good IMP version_: [![build info](https://salilab.org/imp/systems/?sysstat=13&branch=master)](https://integrativemodeling.org/systems/) [![build info](https://integrativemodeling.org/systems/?sysstat=13&branch=develop)](https://integrativemodeling.org/systems/)

_Testable_: Yes.

_Parallelizeable_: No

_Publications_:
 - Romain Algret, Javier Fernandez-Martinez, Yi Shi, Seung Joong Kim, Riccardo Pellarin, Peter Cimermancic, Emilie Cochet, Andrej Sali, Brian T. Chait, Michael P. Rout, and Svetlana Dokudovskaya, [Molecular architecture and function of the SEA complex, a modulator of the TORC1 pathway](http://mcponline.org/content/early/2014/07/29/mcp.M114.039388), Molecular & Cellular Proteomics, 2014, mcp.M114.039388.
