#!/usr/bin/env python
#####################################################
# Sep 2, 2013 18:10
# by Seung Joong Kim, Peter Cimermancic, Riccardo Pellarin
# at UCSF Andrej Sali group
#####################################################
import IMP
import IMP.core
import IMP.base
import IMP.algebra
import IMP.atom
import IMP.container

import IMP.pmi1.restraints as restraints
import IMP.pmi1.representation as representation
import IMP.pmi1.analysis as analysis
import IMP.pmi1.tools as tools
import IMP.pmi1.output as output
import IMP.pmi1.samplers as samplers
import random

ncycl = 100         #number of Monte Carlo steps per cycle
rbmaxtrans = 1.50
fbmaxtrans = 1.50
rbmaxrot = 0.025
outputobjects = []
sampleobjects = []
partialscore1 = []
partialscore2 = []


#####################################################
# Parsing parameter inputs
#####################################################
import argparse

parser = argparse.ArgumentParser(description='Performing the INITIAL/REFINEMENT Monte Carlo job, with crosslinks and selected/ALL domain mapping data. Example of usage: setup_environment.sh python ./sj_SEA_XLDM.py -f models_1877.rmf -n 0')
parser.add_argument('-copy', action="store", dest="ncopy", help="copy numbers (stoichiometry) for SEA4 and Seh1" )
parser.add_argument('-sym', action="store", dest="symmetry", help="symmetry option for SEA4 and Seh1" )
parser.add_argument('-f', action="store", dest="rmf_input", help="rmf file name to continue" )
parser.add_argument('-n', action="store", dest="frame_number", help="frame number to continue" )
parser.add_argument('-r', action="store", dest="nrepeats", help="number of Monte Carlo cycles" )
parser.add_argument('-x', action="store", dest="XL_input", help="Cross-links file name to read" )
parser.add_argument('-o', action="store", dest="rmf_output", help="rmf file name for output" )
parser.add_argument('-s', action="store", dest="stat_output", help="stat file name for output" )
parser.add_argument('-REFINE', action="store", dest="refinement", help="refinement True or False" )
parser.add_argument('-w', action="store", dest="weight", help="weight for domain mapping data" )
parser.add_argument('-res_cry', action="store", dest="res_cry", help="resolution of the crystal structures" )
parser.add_argument('-res_hom', action="store", dest="res_hom", help="resolution of the comparative (homology) models" )
parser.add_argument('-res_ev', action="store", dest="res_ev", help="resolution of the excluded volume restraints" )
parser.add_argument('-res_compo', action="store", dest="res_compo", help="resolution of the composite restraints" )
parser.add_argument('-draw_hierarchy', action="store", dest="draw_hierarchy", help="draw hierarchy" )
inputs = parser.parse_args()

# Setting up the input parameters
if inputs.ncopy==None:
    inputs.ncopy = "3"
if (inputs.symmetry=="True") or (inputs.symmetry=="true") or (inputs.symmetry=="Yes") or (inputs.symmetry=="yes") :
    inputs.symmetry = True
else:
    inputs.symmetry = True
if inputs.rmf_input!=None:
    f=open(inputs.rmf_input,"r")
    f.close()
if inputs.XL_input==None:
    inputs.XL_input = "../SEAcmplx_XL.txt"
else:
    f=open(inputs.XL_input,"r")
    f.close()
if inputs.frame_number==None:
    inputs.frame_number = 1
if inputs.nrepeats==None:
    inputs.nrepeats = 5
if inputs.rmf_output==None:
    inputs.rmf_output = "models.rmf"
if inputs.stat_output==None:
    inputs.stat_output = "stat.dat"
if (inputs.refinement=="True") or (inputs.refinement=="true") or (inputs.refinement=="Yes") or (inputs.refinement=="yes") :
    inputs.refinement = True
else:
    inputs.refinement = False
if inputs.weight==None:
    inputs.weight = 1.0
if inputs.res_cry==None:
    inputs.res_cry = 1.0
if inputs.res_hom==None:
    inputs.res_hom = 5.0
if inputs.res_ev==None:
    inputs.res_ev = 5.0
if inputs.res_compo==None:
    inputs.res_compo = 100.0
if (inputs.draw_hierarchy=="True") or (inputs.draw_hierarchy=="true") or (inputs.draw_hierarchy=="Yes") or (inputs.draw_hierarchy=="yes") :
    inputs.draw_hierarchy = True
else:
    inputs.draw_hierarchy = False
print inputs


#####################################################
#create hierarchies and rigid bodies and flexible parts
#####################################################
m = IMP.Model()
simo = representation.SimplifiedModel(m,upperharmonic=True,disorderedlength=True)
res_cry = float(inputs.res_cry)
res_hom = float(inputs.res_hom)
res_ev = float(inputs.res_ev)
res_compo = float(inputs.res_compo)
res = []
res2 = [] 

#list of resolution for the homology (comparative) models
if (res_hom == res_ev):
    res = [res_hom, res_compo]
elif (res_hom > res_ev):
    res = [res_ev, res_hom, res_compo]
else:
    res = [res_hom, res_ev, res_compo]
print "resolutions for the homology models = ", res

#list of resolution for the crystal structures
if (res_cry == res_ev):
    res2 = [res_cry, res_compo]
elif (res_cry > res_ev):
    res2 = [res_ev, res_cry, res_compo]
else:
    res2 = [res_cry, res_ev, res_compo]
print "resolutions for the crystal structures = ", res2


# SEA1
tmp_color=0.5
simo.add_component_name("SEA1")
ds=[(1,50),(51,100)]; simo.add_component_beads("SEA1", ds,colors=[tmp_color])
simo.add_component_pdb("SEA1", '../../pdb/SEA1_101-275.pdb', "A", resolutions=res, color=tmp_color)
ds=[(276,278)]; simo.add_component_beads("SEA1", ds,colors=[tmp_color])
simo.add_component_pdb("SEA1", '../../pdb/SEA1_279-473.pdb', "A", resolutions=res, color=tmp_color, resrange=(279,331))
ds=[(332,343)]; simo.add_component_beads("SEA1", ds,colors=[tmp_color])
simo.add_component_pdb("SEA1", '../../pdb/SEA1_279-473.pdb', "A", resolutions=res, color=tmp_color, resrange=(344,376))
ds=[(377,399)]; simo.add_component_beads("SEA1", ds,colors=[tmp_color])
simo.add_component_pdb("SEA1", '../../pdb/SEA1_279-473.pdb', "A", resolutions=res, color=tmp_color, resrange=(400,473))
ds=[(474,526),\
    (527,609),(610,692),(693,775),(776,859),\
    (860,948),(949,1037),(1038,1126),\
    (1127,1177)]; simo.add_component_beads("SEA1", ds,colors=[tmp_color])
simo.add_component_pdb("SEA1", '../../pdb/SEA1_1178-1273.pdb', "A", resolutions=res, color=tmp_color)
ds=[(1274,1340),\
    (1341,1421),(1422,1502),(1503,1584)]; simo.add_component_beads("SEA1", ds,colors=[tmp_color])
simo.setup_component_sequence_connectivity("SEA1", res_cry)


# SEA2
tmp_color=0.7
simo.add_component_name("SEA2")
ds=[(1,63),(64,126)]; simo.add_component_beads("SEA2", ds,colors=[tmp_color])
simo.add_component_pdb("SEA2",'../../pdb/SEA2_127-520.pdb', "A", resolutions=res, color=tmp_color, resrange=(127,172))
ds=[(173,200)]; simo.add_component_beads("SEA2", ds,colors=[tmp_color])
simo.add_component_pdb("SEA2",'../../pdb/SEA2_127-520.pdb', "A", resolutions=res, color=tmp_color, resrange=(201,319))
ds=[(320,337)]; simo.add_component_beads("SEA2", ds,colors=[tmp_color])
simo.add_component_pdb("SEA2",'../../pdb/SEA2_127-520.pdb', "A", resolutions=res, color=tmp_color, resrange=(338,403))
ds=[(404,433)]; simo.add_component_beads("SEA2", ds,colors=[tmp_color])
simo.add_component_pdb("SEA2",'../../pdb/SEA2_127-520.pdb', "A", resolutions=res, color=tmp_color, resrange=(434,520))
ds=[(521,563),\
    (564,662),(663,761),(762,860),(861,959),(960,1058),(1059,1155),\
    (1156,1217),(1218,1279)]; simo.add_component_beads("SEA2", ds,colors=[tmp_color])
simo.add_component_pdb("SEA2",'../../pdb/SEA2_1280-1341.pdb', "A", resolutions=res, color=tmp_color)
simo.setup_component_sequence_connectivity("SEA2", res_cry)
#simo.set_uncertianty(5,("SEA2",100,110),resolution=1)


# SEA3
tmp_color=0.0
simo.add_component_name("SEA3")
ds=[(1,53)]; simo.add_component_beads("SEA3",ds,colors=[tmp_color])
simo.add_component_pdb("SEA3",'../../pdb/SEA3_54-424.pdb', "A", resolutions=res, color=tmp_color, resrange=(54,278))
ds=[(279,289)]; simo.add_component_beads("SEA3",ds,colors=[tmp_color])
simo.add_component_pdb("SEA3",'../../pdb/SEA3_54-424.pdb', "A", resolutions=res, color=tmp_color, resrange=(290,314))
ds=[(315,324)]; simo.add_component_beads("SEA3",ds,colors=[tmp_color])
simo.add_component_pdb("SEA3",'../../pdb/SEA3_54-424.pdb', "A", resolutions=res, color=tmp_color, resrange=(325,344))
ds=[(345,389)]; simo.add_component_beads("SEA3",ds,colors=[tmp_color])
simo.add_component_pdb("SEA3",'../../pdb/SEA3_54-424.pdb', "A", resolutions=res, color=tmp_color, resrange=(390,424))
ds=[(425,429)]; simo.add_component_beads("SEA3",ds,colors=[tmp_color])
simo.add_component_pdb("SEA3",'../../pdb/SEA3_430-536.pdb', "A", resolutions=res, color=tmp_color)
ds=[(537,615),(616,694),(695,772),\
    (773,825),(826,878),\
    (879,937),(938,995),\
    (996,1091)]; simo.add_component_beads("SEA3",ds,colors=[tmp_color])
simo.add_component_pdb("SEA3",'../../pdb/SEA3_1092_1139.pdb', "A", resolutions=res, color=tmp_color)
ds=[(1140,1148)]; simo.add_component_beads("SEA3",ds,colors=[tmp_color])
simo.setup_component_sequence_connectivity("SEA3", res_cry)


# SEA4
tmp_color=1.0
cnames={}
if (inputs.ncopy == "3"):
    cnames=["SEA4.1", "SEA4.2", "SEA4.3"]
else:
    cnames=["SEA4"]
for cname in cnames:
    simo.add_component_name(cname)
    ds=[(1,44)]; simo.add_component_beads(cname,ds,colors=[tmp_color])
    simo.add_component_pdb(cname,'../../pdb/SEA4_45-426.pdb', "A", resolutions=res, color=tmp_color, resrange=(45,87))
    ds=[(88,123)]; simo.add_component_beads(cname,ds,colors=[tmp_color])
    simo.add_component_pdb(cname,'../../pdb/SEA4_45-426.pdb', "A", resolutions=res, color=tmp_color, resrange=(124,130))
    ds=[(131,148)]; simo.add_component_beads(cname,ds,colors=[tmp_color])
    simo.add_component_pdb(cname,'../../pdb/SEA4_45-426.pdb', "A", resolutions=res, color=tmp_color, resrange=(149,272))
    ds=[(273,284)]; simo.add_component_beads(cname,ds,colors=[tmp_color])
    simo.add_component_pdb(cname,'../../pdb/SEA4_45-426.pdb', "A", resolutions=res, color=tmp_color, resrange=(285,333))
    ds=[(334,355)]; simo.add_component_beads(cname,ds,colors=[tmp_color])
    simo.add_component_pdb(cname,'../../pdb/SEA4_45-426.pdb', "A", resolutions=res, color=tmp_color, resrange=(356,426))
    ds=[(427,490),\
        (491,574),(575,658)]; simo.add_component_beads(cname,ds,colors=[tmp_color])
    simo.add_component_pdb(cname,'../../pdb/SEA4_659-835.pdb', "A", resolutions=res, color=tmp_color, resrange=(659,782))    
    ds=[(783,808)]; simo.add_component_beads(cname,ds,colors=[tmp_color])
    simo.add_component_pdb(cname,'../../pdb/SEA4_659-835.pdb', "A", resolutions=res, color=tmp_color, resrange=(809,835))    
    ds=[(836,888),\
        (889,941)]; simo.add_component_beads(cname,ds,colors=[tmp_color])
    simo.add_component_pdb(cname,'../../pdb/SEA4_942-1032.pdb', "A", resolutions=res, color=tmp_color, resrange=(942,963))
    ds=[(964,999)]; simo.add_component_beads(cname,ds,colors=[tmp_color])
    simo.add_component_pdb(cname,'../../pdb/SEA4_942-1032.pdb', "A", resolutions=res, color=tmp_color, resrange=(1000,1032))
    ds=[(1033,1038)]; simo.add_component_beads(cname,ds,colors=[tmp_color])
    if not (inputs.symmetry) or (cname=="SEA4.1"):
        simo.setup_component_sequence_connectivity(cname, res_cry)
    print cname


# Npr2
tmp_color=0.8
simo.add_component_name("Npr2")
ds=[(1,8)]; simo.add_component_beads("Npr2",ds,colors=[tmp_color])
simo.add_component_pdb("Npr2",'../../pdb/Npr2_9-127.pdb', "A", resolutions=res, color=tmp_color)
ds=[(128,192),(193,256)]; simo.add_component_beads("Npr2",ds,colors=[tmp_color])
simo.add_component_pdb("Npr2",'../../pdb/Npr2_257-327.pdb', "A", resolutions=res, color=tmp_color)
ds=[(328,355),\
    (356,430),\
    (431,493),\
    (494,562)]; simo.add_component_beads("Npr2",ds,colors=[tmp_color])
simo.add_component_pdb("Npr2",'../../pdb/Npr2_563-610.pdb', "A", resolutions=res, color=tmp_color)
ds=[(611,615)]; simo.add_component_beads("Npr2",ds,colors=[tmp_color])
simo.setup_component_sequence_connectivity("Npr2", res_cry)


# Npr3
tmp_color=0.87
simo.add_component_name("Npr3")
simo.add_component_pdb("Npr3",'../../pdb/Npr3_1-31.pdb', "A", resolutions=res, color=tmp_color)
ds=[(32,128),(129,225),(226,321)]; simo.add_component_beads("Npr3",ds,colors=[tmp_color])
simo.add_component_pdb("Npr3",'../../pdb/Npr3_322-438.pdb', "A", resolutions=res, color=tmp_color, resrange=(322,351))
ds=[(352,399)]; simo.add_component_beads("Npr3",ds,colors=[tmp_color])
simo.add_component_pdb("Npr3",'../../pdb/Npr3_322-438.pdb', "A", resolutions=res, color=tmp_color, resrange=(400,438))
ds=[(439,530)]; simo.add_component_beads("Npr3",ds,colors=[tmp_color])
simo.add_component_pdb("Npr3",'../../pdb/Npr3_531-577.pdb', "A", resolutions=res, color=tmp_color)
ds=[(578,670),(671,763),(764,856),(857,949)]; simo.add_component_beads("Npr3",ds,colors=[tmp_color])
simo.add_component_pdb("Npr3",'../../pdb/Npr3_950-988.pdb', "A", resolutions=res, color=tmp_color)
ds=[(989,1082)]; simo.add_component_beads("Npr3",ds,colors=[tmp_color])
simo.add_component_pdb("Npr3",'../../pdb/Npr3_1083-1140.pdb', "A", resolutions=res, color=tmp_color)
ds=[(1141,1146)]; simo.add_component_beads("Npr3",ds,colors=[tmp_color])
simo.setup_component_sequence_connectivity("Npr3", res_cry)


# Seh1; Residues (249-287) and (347-349) are missing in PDB
tmp_color=0.4
cnames={}
if (inputs.ncopy == "3"):
    cnames=["Seh1.1", "Seh1.2", "Seh1.3"]
else:
    cnames=["Seh1"]
for cname in cnames:
    simo.add_component_name(cname)
    simo.add_component_pdb(cname,'../../pdb/3F3F.pdb', "A", resolutions=res2, color=tmp_color, resrange=(1,248))
    ds=[(249,287)]; simo.add_component_beads(cname,ds,colors=[tmp_color])
    simo.add_component_pdb(cname,'../../pdb/3F3F.pdb', "A", resolutions=res2, color=tmp_color, resrange=(288,346))
    ds=[(347,349)]; simo.add_component_beads(cname,ds,colors=[tmp_color])
    if not (inputs.symmetry) or (cname=="Seh1.1"):
        simo.setup_component_sequence_connectivity(cname, res_cry)
    print cname


# Sec13; Residues (1), (159-165), (297) are missing in PDB
tmp_color=0.3
simo.add_component_name("Sec13")
ds=[(1,1)]; simo.add_component_beads("Sec13",ds,colors=[tmp_color])
simo.add_component_pdb("Sec13",'../../pdb/2PM7.pdb', "D", resolutions=res2, color=tmp_color, resrange=(2,158))
ds=[(159,165)]; simo.add_component_beads("Sec13",ds,colors=[tmp_color])
simo.add_component_pdb("Sec13",'../../pdb/2PM7.pdb', "D", resolutions=res2, color=tmp_color, resrange=(166,296))
ds=[(297,297)]; simo.add_component_beads("Sec13",ds,colors=[tmp_color])
simo.setup_component_sequence_connectivity("Sec13", res_cry)


#####################################################
## Read the coordinates from the previous runs,
## or starts from scratch
#####################################################
if (inputs.rmf_input!=None):
    print "Reading coordinates from", inputs.rmf_input, inputs.frame_number
    simo.link_components_to_rmf(inputs.rmf_input, int(inputs.frame_number))

    simo.set_rigid_bodies([("SEA1",(101,275))])
    simo.set_rigid_bodies([("SEA1",(279,473))]) 
    simo.set_rigid_bodies([("SEA1",(1178,1273))]) 
    simo.set_rigid_bodies([("SEA2",(127,520))])
    simo.set_rigid_bodies([("SEA2",(1280,1341))])
    simo.set_rigid_bodies([("SEA3",(54,424))])
    simo.set_rigid_bodies([("SEA3",(430,536))])
    simo.set_rigid_bodies([("SEA3",(1092,1139))])
    
    if (inputs.ncopy == "3"):
        simo.set_rigid_bodies([("SEA4.1",(45,426))])
        simo.set_rigid_bodies([("SEA4.1",(659,835))])
        simo.set_rigid_bodies([("SEA4.1",(942,1032))])
        simo.set_rigid_bodies(["Seh1.1"])
        if not (inputs.symmetry):
            simo.set_rigid_bodies([("SEA4.2",(45,426))])
            simo.set_rigid_bodies([("SEA4.2",(659,835))])
            simo.set_rigid_bodies([("SEA4.2",(942,1032))])
            simo.set_rigid_bodies([("SEA4.3",(45,426))])
            simo.set_rigid_bodies([("SEA4.3",(659,835))])
            simo.set_rigid_bodies([("SEA4.3",(942,1032))])
            simo.set_rigid_bodies(["Seh1.2"])
            simo.set_rigid_bodies(["Seh1.3"])
    else:
        simo.set_rigid_bodies([("SEA4",(45,426))])
        simo.set_rigid_bodies([("SEA4",(659,835))])
        simo.set_rigid_bodies([("SEA4",(942,1032))])
        simo.set_rigid_bodies(["Seh1"])
    
    simo.set_rigid_bodies([("Npr2",(9,127))])
    simo.set_rigid_bodies([("Npr2",(257,327))])
    simo.set_rigid_bodies([("Npr2",(563,610))])
    simo.set_rigid_bodies([("Npr3",(1,31))])
    simo.set_rigid_bodies([("Npr3",(322,438))])
    simo.set_rigid_bodies([("Npr3",(531,577))])
    simo.set_rigid_bodies([("Npr3",(950,988))])
    simo.set_rigid_bodies([("Npr3",(1083,1140))])
    simo.set_rigid_bodies(["Sec13"])

else:
    rmx=150
    simo.set_rigid_bodies([("SEA1",(101,275))],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
    simo.set_rigid_bodies([("SEA1",(279,473))],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx))) 
    simo.set_rigid_bodies([("SEA1",(1178,1273))],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx))) 
    simo.set_rigid_bodies([("SEA2",(127,520))],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
    simo.set_rigid_bodies([("SEA2",(1280,1341))],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
    simo.set_rigid_bodies([("SEA3",(54,424))],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
    simo.set_rigid_bodies([("SEA3",(430,536))],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
    simo.set_rigid_bodies([("SEA3",(1092,1139))],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
    
    if (inputs.ncopy == "3"):
        simo.set_rigid_bodies([("SEA4.1",(45,426))],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
        simo.set_rigid_bodies([("SEA4.1",(659,835))],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
        simo.set_rigid_bodies([("SEA4.1",(942,1032))],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
        simo.set_rigid_bodies(["Seh1.1"],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
        if not (inputs.symmetry):
            simo.set_rigid_bodies([("SEA4.2",(45,426))],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
            simo.set_rigid_bodies([("SEA4.2",(659,835))],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
            simo.set_rigid_bodies([("SEA4.2",(942,1032))],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
            simo.set_rigid_bodies([("SEA4.3",(45,426))],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
            simo.set_rigid_bodies([("SEA4.3",(659,835))],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
            simo.set_rigid_bodies([("SEA4.3",(942,1032))],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
            simo.set_rigid_bodies(["Seh1.2"],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
            simo.set_rigid_bodies(["Seh1.3"],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
    else:
        simo.set_rigid_bodies([("SEA4",(45,426))],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
        simo.set_rigid_bodies([("SEA4",(659,835))],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
        simo.set_rigid_bodies([("SEA4",(942,1032))],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
        simo.set_rigid_bodies(["Seh1"],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
    
    simo.set_rigid_bodies([("Npr2",(9,127))],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
    simo.set_rigid_bodies([("Npr2",(257,327))],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
    simo.set_rigid_bodies([("Npr2",(563,610))],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
    simo.set_rigid_bodies([("Npr3",(1,31))],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
    simo.set_rigid_bodies([("Npr3",(322,438))],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
    simo.set_rigid_bodies([("Npr3",(531,577))],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
    simo.set_rigid_bodies([("Npr3",(950,988))],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
    simo.set_rigid_bodies([("Npr3",(1083,1140))],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))
    simo.set_rigid_bodies(["Sec13"],(random.uniform(-rmx, rmx), random.uniform(-rmx, rmx), random.uniform(-rmx, rmx)))

if (inputs.ncopy == "3") and (inputs.symmetry):
    simo.create_rotational_symmetry("SEA4.1",["SEA4.2","SEA4.3"])
    simo.create_rotational_symmetry("Seh1.1",["Seh1.2","Seh1.3"])


simo.set_floppy_bodies()
simo.set_rigid_bodies_max_trans(rbmaxtrans)
simo.set_rigid_bodies_max_rot(rbmaxrot)
simo.set_floppy_bodies_max_trans(fbmaxtrans)


#re-orient initial positions
if (inputs.rmf_input==None):
    simo.shuffle_configuration(translate=False)

if (inputs.draw_hierarchy):
    simo.draw_hierarchy_composition()
    #simo.draw_hierarchy_graph()

    simo.show_component_table("SEA1")
    simo.show_component_table("SEA2")
    simo.show_component_table("SEA3")
    if (inputs.ncopy == "3"):
        simo.show_component_table("SEA4.1")
        simo.show_component_table("SEA4.2")
        simo.show_component_table("SEA4.3")
        simo.show_component_table("Seh1.1")
        simo.show_component_table("Seh1.2")
        simo.show_component_table("Seh1.3")
    else:
        simo.show_component_table("SEA4")
        simo.show_component_table("Seh1")
    simo.show_component_table("Npr2")
    simo.show_component_table("Npr3")
    simo.show_component_table("Sec13")

    d = simo.get_particles_to_sample()
    print d

prot = simo.get_hierarchy()
#simo.set_output_level("high")

#expl=simo.get_connected_intra_pairs()
outputobjects.append(simo)
sampleobjects.append(simo)
partialscore1.append(simo)
partialscore2.append(simo)


#####################################################
# Restraints setup
# Excluded Volume restraint
#####################################################
ev = restraints.ExcludedVolumeSphere(prot, resolution=res_ev)
#ev.add_excluded_particle_pairs(expl)
ev.add_to_model()
#ev.set_weight(0.1)
outputobjects.append(ev)
partialscore1.append(ev)
#partialscore2.append(ev)
print "ExcludedVolumeSphere !!"

"""
#####################################################
# setting up the composite restraint
#####################################################
weight = float(inputs.weight)
crd={}
if (inputs.ncopy == "3"):
    crd["Npr2_dNpr2_497_615_P"]=[(1,496,"Npr2"),"Npr3"]
    crd["SEA4_dSEA4:931-1038_P"]=[(1,930,"SEA4.1"),(1,930,"SEA4.2"),(1,930,"SEA4.3"),"Seh1.1","Seh1.2","Seh1.3"]
    if (inputs.refinement):
        crd["SEA1_WT_P"]=["SEA1","Npr2","Npr3","SEA3","SEA4.1","SEA4.2","SEA4.3","Seh1.1","Seh1.2","Seh1.3","Sec13","SEA2"]
        crd["SEA1_dSEA4_P"]=["SEA1","Npr2","Npr3","SEA3","Sec13"]
        crd["SEA3_dSEA2_P"]=["SEA3","SEA4.1","SEA4.2","SEA4.3","Seh1.1","Seh1.2","Seh1.3","Sec13"]
        crd["SEA3_dNpr3_P"]=["SEA3","SEA4.1","SEA4.2","SEA4.3","Seh1.1","Seh1.2","Seh1.3","Sec13","SEA2"]
        crd["SEA3_dSEA3:401-1148_P"]=["SEA1","Npr2","Npr3",(1,400,"SEA3")]
        crd["SEA3_dSEA3:401-1148_P2"]=["SEA1","Npr3",(1,400,"SEA3")]
        crd["SEA3_dSEA3:910-1148_P"]=["SEA1","Npr2","Npr3",(1,909,"SEA3"),"Sec13"]
        crd["SEA4_dSEA3_P"]=["SEA4.1","SEA4.2","SEA4.3","Seh1.1","Seh1.2","Seh1.3","SEA2"]
        crd["SEA4_dSEA3_P2"]=["SEA4.1","SEA4.2","SEA4.3","Seh1.1","Seh1.2","Seh1.3"]
        print "All composite restraints !! with weight =", weight    
else:
    crd["Npr2_dNpr2_497_615_P"]=[(1,496,"Npr2"),"Npr3"]
    if (inputs.refinement):
        crd["SEA1_WT_P"]=["SEA1","Npr2","Npr3","SEA3","SEA4","Seh1","Sec13","SEA2"]
        crd["SEA1_dSEA4_P"]=["SEA1","Npr2","Npr3","SEA3","Sec13"]
        crd["SEA3_dSEA2_P"]=["SEA3","SEA4","Seh1","Sec13"]
        crd["SEA3_dNpr3_P"]=["SEA3","SEA4","Seh1","Sec13","SEA2"]
        crd["SEA3_dSEA3:401-1148_P"]=["SEA1","Npr2","Npr3",(1,400,"SEA3")]
        crd["SEA3_dSEA3:401-1148_P2"]=["SEA1","Npr3",(1,400,"SEA3")]
        crd["SEA3_dSEA3:910-1148_P"]=["SEA1","Npr2","Npr3",(1,909,"SEA3"),"Sec13"]
        crd["SEA4_dSEA3_P"]=["SEA4","Seh1","SEA2"]
        crd["SEA4_dSEA3_P2"]=["SEA4","Seh1"]
        crd["SEA4_dSEA4:931-1038_P"]=[(1,930,"SEA4"),"Seh1"]
        print "All composite restraints !! with weight =", weight
    
for key in crd:
    cr=restraints.ConnectivityRestraint(prot,crd[key],resolution=res_compo)
    cr.add_to_model()
    cr.set_label(key)
    cr.set_weight(weight)
    partialscore1.append(cr)  
    partialscore2.append(cr)
    outputobjects.append(cr)
    print key, crd[key]

print "Composite Restraint !! with weight =", weight


#####################################################
# Cross-link restraint
# sample format: "ssl1 ssl1 196 200"
#####################################################
#res_XL = res_cry + 1.0
res_XL = res_cry
xl = restraints.ConnectivityCrossLinkMS(prot, inputs.XL_input, expdistance=17., resolution=res_XL)
#xl = restraints.ConnectivityCrossLinkMS(prot, inputs.XL_input, expdistance=17., strength=0.2, resolution=res_XL)
#xl = restraints.SimplifiedCrossLinkMS(prot, inputs.XL_input, expdistance=17., strength=0.2)
#xl = restraints.SigmoidCrossLinkMS(prot, inputs.XL_input, inflection=25., slope=1.0, amplitude=1.0, resolution=res_XL)
#xl.plot_restraint(uncertainty1=4.95, uncertainty2=6.25, maxdist=100)

xl.add_to_model()
#xl.set_weight(0.1)

outputobjects.append(xl)
partialscore1.append(xl)
partialscore2.append(xl)
print "Cross-Links !!"
print inputs
"""  
#####################################################
# GaussianEMRestraint
# TODO: Nothing here yet
#####################################################


#####################################################
#analyze RMFs
#####################################################

import pickle
import numpy as np
import glob
import IMP.rmf
import RMF
import inspect
import os

files = glob.glob('../*_REFINED*.rmf')

"""
#####################################################
### --- Get clustered heat map  (Manual)
#####################################################
Clusters = analysis.Clustering()
# read in all the frames with score lower than XXX
for cnt,fil in enumerate(files):

    # load the frame
    rh= RMF.open_rmf_file(fil)
    IMP.rmf.link_hierarchies(rh, [prot])

    frame_number = 0
    IMP.rmf.load_frame(rh, frame_number)
    m.update()

    Clusters.set_prot(prot)

    # set alignment template (if global, list all proteins, or just a few for local)   
    template = {}
    for pr in ['Seh1.1', 'Seh1.2', 'Seh1.3', 'Sec13']:
        parts = IMP.atom.Selection(prot,molecule=pr).get_selected_particles()
        coords = np.array([np.array(IMP.core.XYZ(i).get_coordinates()) for i in parts])
        template[pr] = coords

    #print 'TEMPLATE', template
    if len(Clusters.all_coords)==0:
        Clusters.set_template(template)

    # set particles to calculate RMSDs on 
    # (if global, list all proteins, or just a few for local)    
    Coords = {}
    #for pr in ['Seh1.1', 'Seh1.2', 'Seh1.3', 'Sec13']:
    for pr in [p.get_name() for p in prot.get_children()]:
        parts = IMP.atom.Selection(prot,molecule=pr).get_selected_particles()
        coords = np.array([np.array(IMP.core.XYZ(i).get_coordinates()) for i in parts])
        Coords[pr] = coords  
    
    Clusters.fill(fil, Coords, alignment=1)


print "Global clustered heat map, aligned by Seh1 and Sec13"
Clusters.dist_matrix()
os.rename("tmp_clustering.pdf", "Seh1_Sec13_global.pdf")
os.remove("tmp_cluster_493.pkl")
exit()


#####################################################
### --- Get ("Localized" and "Global") clustered heat map - Automated
#####################################################
for mols in ['SEA1','Npr2','Npr3','SEA3','SEA4','Seh1','Sec13','SEA2']:
    Clusters_local = tools.Clustering()
    Clusters_global = tools.Clustering()

    # read in all the frames with score lower than XXX?    
    for cnt,fil in enumerate(files):

        # load the frame
        rh = RMF.open_rmf_file(fil)
        IMP.rmf.link_hierarchies(rh, [prot])

        frame_number = 0    
        IMP.rmf.load_frame(rh, frame_number)
        Clusters_local.set_prot(prot)
        #Clusters_local.get_subunit_coords(fil)
        
        Clusters_global.set_prot(prot)
        #Clusters_global.get_subunit_coords(fil)
        
        indx = []
        parts = []

        # localized clustered heat map for each molecule
        # Global clustered heat map, aligned and referenced by each molecule
        parts += IMP.atom.Selection(prot, molecule=mols).get_selected_particles()
        coords = [IMP.core.XYZ(i).get_coordinates() for i in parts]

        if len(Clusters_local.all_coords)==0:
            Clusters_local.set_template(coords)

        if len(Clusters_global.all_coords)==0:    
            Clusters_global.set_template(coords)

        Clusters_local.align_and_fill(fil, coords, prot, global_ali=0)
        Clusters_global.align_and_fill(fil, coords, prot, global_ali=1)

    print "Localized clustered heat map, for", mols
    Clusters_local.dist_matrix()
    os.rename("tmp_clustering.pdf", mols+"_local.pdf")
    os.remove("tmp_cluster_493.pkl")

    print "Global clustered heat map, aligned by", mols
    Clusters_global.dist_matrix()
    os.rename("tmp_clustering.pdf", mols+"_global.pdf")
    os.remove("tmp_cluster_493.pkl")
#exit()
#
"""


"""
#####################################################
### --- Get contact map
#####################################################
ContactMap = analysis.GetContactMap(distance=25.)
print files
for z, fil in enumerate(files):

    # load the frame
    rh= RMF.open_rmf_file(fil)
    IMP.rmf.link_hierarchies(rh, [prot])

    print "1"
    frame_number = 0
    IMP.rmf.load_frame(rh, frame_number)
    m.update()
    print "2"
        
    ContactMap.set_prot(prot)
    print "3"
    ContactMap.get_subunit_coords(fil)
    print "4"

#ContactMap.add_xlinks('../SEAcmplx_XL.txt')  
ContactMap.dist_matrix(skip_cmap=0, skip_xl=1)
exit()
"""



#####################################################
### ---- Get global or local density map
#####################################################
DensModule = analysis.GetModelDensity(margin=100., voxel=9.)
for z, fil in enumerate(files):

    # load the frame
    rh= RMF.open_rmf_file(fil)
    IMP.rmf.link_hierarchies(rh, [prot])

    frame_number = 0
    IMP.rmf.load_frame(rh, frame_number)
    m.update()

    # set alignment template (if global, list all proteins, or just a few for local)    
    template = {}
    #for pr in ['Seh1.1', 'Seh1.2', 'Seh1.3', 'Sec13']:
    for pr in [p.get_name() for p in prot.get_children()]:
        parts = IMP.atom.Selection(prot,molecule=pr).get_selected_particles()
        coords = np.array([np.array(IMP.core.XYZ(i).get_coordinates()) for i in parts])
        template[pr] = coords

    # set particles to calculate density from 
    # (if global, list all proteins, or just a few for local)    
    Coords = {}
    #for pr in ['Seh1', 'Sec13']:
    for pr in [p.get_name() for p in prot.get_children()]:
        parts = IMP.atom.Selection(prot,molecule=pr).get_selected_particles()
        coords = np.array([np.array(IMP.core.XYZ(i).get_coordinates()) for i in parts])
        Coords[pr] = coords

    # set grid
    if DensModule.densities == {}:
        coords = [IMP.core.XYZ(i).get_coordinates() for i in IMP.atom.get_leaves(prot)]
        grid = DensModule.set_grid(coords)
        DensModule.set_template(template)

    DensModule.fill(Coords, prot, alignment=1)
    print z,fil

DensModule.write_mrc('SEA_complex')        
#exit()

