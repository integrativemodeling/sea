# SEA Complex

These scripts demonstrate the use of [IMP](http://salilab.org/imp), [MODELLER](http://salilab.org/modeller), 
[PMI](https://github.com/salilab/pmi) in the modeling of the SEA complex using 188 DSS chemical cross-links and 23 affinity purification data.

First, [MODELLER](http://salilab.org/modeller) is used to generate
initial structures for the individual components where reliable templates are available. Then, IMP
is used to model these components using the DSS/EDC crosslinks and the affinity purification data for the entire SEA complex.


A full description of the scripts can be found in
[Molecular architecture and function of the SEA complex, a modulator of the TORC1 pathway](http://mcponline.org/content/early/2014/07/29/mcp.M114.039388).

## List of files and directories:

- `data`		                         contains all relevant data, input structure, etc.

- `scripts`
  - `nup84.isd.modeling.withXrayInterface.py`  the main modeling script with 3 crystal interfaces

  - `nup84.isd.modeling.py`                    the main modeling script with no crystal interfaces

  - `nup84.topology.withXrayInterface.py`      constructs Nup84 subunits with 3 crystal interfaces

  - `nup84.topology.py`                        constructs Nup84 subunits with no crystal interfaces

  - `nup84.merge.py`                           script to merge output files from all runs ; filter threshold on total score can be set here
 
  - `vmd_scripts/rmdstt.tcl`                   VMD script to launch RMSD Trajectory Tool window 

  - `vmd_scripts/nup84_3-xray_density.tcl`     VMD script to calculate localization density for Nup84 with 3 crystal interfaces

  - `vmd_scripts/nup84_no-xray_density.tcl`    VMD script to calculate localization density for Nup84 with no crystal interfaces

  - `vmd_scripts/ALPS_motif_density.tcl`       VMD script to calculate localization density for Nup84 at ALPS motif regions 

  - `chimera_scripts/nup84_density.cmd`        Chimera script to view all localization density files 


- `output.1/pdbs`    the production will write the best scoring models into pdb files they are initialized and then updated as long as the calculation goes
                 (They are the best 500 models, so at the beginning they are empty, since you haven't start the calculation yet)

- `output.1/rmfs`    the production will write the rmf3 files for lowest temperature replica.
			
- `stat.n.out`	 log files. They contain all relevant numbers of the calculation.

## Running nup84 script:
with 3 crystal interfaces:
- `python nup84.isd.modeling.withXrayInterface.py & > nup84.isd.modeling.withXrayInterface.out` (on a single processor; prepend `mpirun -np 4` or similar if you built IMP with MPI support)
- `python nup84.merge.py`
- `clustering_master_script_3-xray.sh`
- `python nup84.analysis.py`

with no crystal interfaces:
- `python nup84.isd.modeling.py &> nup84.isd.modeling.out`
- `python nup84.merge.py`
- `clustering_master_script_no-xray.sh`
- `python nup84.analysis.py`


## Information

_Author(s)_: Seung Joong Kim, Riccardo Pellarin, and Peter Cimermancic

_Date_: September 2nd, 2014

_License_: [LGPL](http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html).
This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

_Last known good IMP version_: [![build info](https://salilab.org/imp/systems/?sysstat=1)](http://salilab.org/imp/systems/)

_Testable_: Yes.

_Parallelizeable_: No

_Publications_:
 - Romain Algret, Javier Fernandez-Martinez, Yi Shi, Seung Joong Kim, Riccardo Pellarin, Peter Cimermancic, Emilie Cochet, Andrej Sali, Brian T. Chait, Michael P. Rout, and Svetlana Dokudovskaya, [Molecular architecture and function of the SEA complex, a modulator of the TORC1 pathway](http://mcponline.org/content/early/2014/07/29/mcp.M114.039388), Molecular & Cellular Proteomics, 2014, mcp.M114.039388.
