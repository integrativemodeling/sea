# SEA Complex (UNDER CONSTRUCTION)

These scripts demonstrate the use of [IMP](http://salilab.org/imp),
[PMI](https://github.com/salilab/pmi),
[FoXS](http://salilab.org/foxs), and
[Minimal Ensemble Search](http://bl1231.als.lbl.gov/saxs_protocols/mes.php) in the modeling of the
SEA complex. First, MODELLER is used to generate
structures for the individual components in the Nup133. Then, IMP
is used to fit these components together into the electron microscopy density
map of Nup133.

A full description of the scripts can be found in
[Molecular architecture and function of the SEA complex, a modulator of the TORC1 pathway](http://mcponline.org/content/early/2014/07/29/mcp.M114.039388).

## Steps (UNDER CONSTRUCTION)

First, make a directory for the output by running `mkdir output`. Output
files that were generated when these scripts were run for the first time are
also provided, in the `precalculate_results` directory. Then, the scripts can
be run in order:

1. Template identification:
    `scripts/script1_build_profile.py`
2. Template(s) selection by sequence:
    `scripts/script2_compare_templates.py`
3. Density map segmentation:
    `scripts/script3_density_segmentation.py`
4. Template selection by fitting to a density map:
    `scripts/script4_score_templates_by_cc.py`
5. Template alignment:
    `scripts/script5_template_alignment.py`
6. Model building and assessment:
    `scripts/script6_model_building_and_assessment.py` and
    `scripts/script7_pairwise_rmsd.py`
7. Multiple fitting into a density map:
    `scripts/script8_split_density.py` and
    `scripts/script9_symmetric_multiple_fitting.py`

## Information

_Author(s)_: Seung Joong Kim, Riccardo Pellarin, Peter Cimermancic

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
