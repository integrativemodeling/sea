import cPickle, base64
try:
	from SimpleSession.versions.v61 import beginRestore,\
	    registerAfterModelsCB, reportRestoreError, checkVersion
except ImportError:
	from chimera import UserError
	raise UserError('Cannot open session that was saved in a'
	    ' newer version of Chimera; update your version')
checkVersion([1, 9, 39395])
import chimera
from chimera import replyobj
replyobj.status('Restoring session...', \
    blankAfter=0)
replyobj.status('Beginning session restore...', \
    blankAfter=0, secondary=True)
beginRestore()

def restoreCoreModels():
	from SimpleSession.versions.v61 import init, restoreViewer, \
	     restoreMolecules, restoreColors, restoreSurfaces, \
	     restoreVRML, restorePseudoBondGroups, restoreModelAssociations
	molInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVRFyaWJib25JbnNpZGVDb2xvcnECSwFOfYdVCWJhbGxTY2FsZXEDSwFHP9AAAAAAAAB9h1UJcG9pbnRTaXplcQRLAUc/8AAAAAAAAH2HVQVjb2xvcnEFSwFLAH2HVQpyaWJib25UeXBlcQZLAUsAfYdVCnN0aWNrU2NhbGVxB0sBRz/wAAAAAAAAfYdVDGFyb21hdGljTW9kZXEISwFLAX2HVQp2ZHdEZW5zaXR5cQlLAUdAFAAAAAAAAH2HVQZoaWRkZW5xCksBiX2HVQ1hcm9tYXRpY0NvbG9ycQtLAU59h1UPcmliYm9uU21vb3RoaW5ncQxLAUsAfYdVCWF1dG9jaGFpbnENSwGIfYdVCG9wdGlvbmFscQ59cQ9VCG9wZW5lZEFzcRCIiUsBKFVbL1VzZXJzL3Nqa2ltL0Ryb3Bib3gvU0VBX2NvbXBsZXgvTW9kZWxpbmcvYW5hbHl6ZURNX1hMXzEwMF9zZWxlY3RlZC8wMV8xMFNBX0RNX201M181NDM0LnJtZk5OiXRxEX2Hh3NVD2xvd2VyQ2FzZUNoYWluc3ESSwGJfYdVCWxpbmVXaWR0aHETSwFHP/AAAAAAAAB9h1UPcmVzaWR1ZUxhYmVsUG9zcRRLAUsAfYdVBG5hbWVxFUsBWGQAAAAvVXNlcnMvc2praW0vRHJvcGJveC9TRUFfY29tcGxleC9Nb2RlbGluZy9hbmFseXplRE1fWExfMTAwX3NlbGVjdGVkLzAxXzEwU0FfRE1fbTUzXzU0MzQucm1mIC0gYm91bmRzfYdVD2Fyb21hdGljRGlzcGxheXEWSwGJfYdVD3JpYmJvblN0aWZmbmVzc3EXSwFHP+mZmZmZmZp9h1UKcGRiSGVhZGVyc3EYXXEZfXEaYVUDaWRzcRtLAUsKSwCGfYdVDnN1cmZhY2VPcGFjaXR5cRxLAUe/8AAAAAAAAH2HVRBhcm9tYXRpY0xpbmVUeXBlcR1LAUsCfYdVFHJpYmJvbkhpZGVzTWFpbmNoYWlucR5LAYh9h1UHZGlzcGxheXEfSwGJfYd1Lg=='))
	resInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQZpbnNlcnRxAku+VQEgfYdVC2ZpbGxEaXNwbGF5cQNLvol9h1UEbmFtZXEES75YAwAAAEJTUH2HVQVjaGFpbnEFS75YAQAAACB9h1UOcmliYm9uRHJhd01vZGVxBku+SwJ9h1UCc3NxB0u+iYmGfYdVCG1vbGVjdWxlcQhLvksAfYdVC3JpYmJvbkNvbG9ycQlLvksHfXEKKEsBTl1xC0sASw+GcQxhhksCTl1xDUsPSwuGcQ5hhksDTl1xD0saSwiGcRBhhksETl1xEUsiSweGcRJhhksFTl1xE0spSwaGcRRhhksGTl1xFUsvSwuGcRZhhksITl1xF0uBSz2GcRhhhnWHVQVsYWJlbHEZS75YAAAAAH2HVQpsYWJlbENvbG9ycRpLvk59h1UIZmlsbE1vZGVxG0u+SwF9h1UFaXNIZXRxHEu+iX2HVQtsYWJlbE9mZnNldHEdS75OfYdVCHBvc2l0aW9ucR5dcR9LAEu+hnEgYVUNcmliYm9uRGlzcGxheXEhS76JfYdVCG9wdGlvbmFscSJ9VQRzc0lkcSNLvkr/////fYd1Lg=='))
	atomInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQdyZXNpZHVlcQJLvksBfXEDKEsCTl1xBEsBSwGGcQVhhksDTl1xBksCSwGGcQdhhksETl1xCEsDSwGGcQlhhksFTl1xCksESwGGcQthhksGTl1xDEsFSwGGcQ1hhksHTl1xDksGSwGGcQ9hhksITl1xEEsHSwGGcRFhhksJTl1xEksISwGGcRNhhksKTl1xFEsJSwGGcRVhhksLTl1xFksKSwGGcRdhhksMTl1xGEsLSwGGcRlhhksNTl1xGksMSwGGcRthhksOTl1xHEsNSwGGcR1hhksPTl1xHksOSwGGcR9hhksQTl1xIEsPSwGGcSFhhksRTl1xIksQSwGGcSNhhksSTl1xJEsRSwGGcSVhhksTTl1xJksSSwGGcSdhhksUTl1xKEsTSwGGcSlhhksVTl1xKksUSwGGcSthhksWTl1xLEsVSwGGcS1hhksXTl1xLksWSwGGcS9hhksYTl1xMEsXSwGGcTFhhksZTl1xMksYSwGGcTNhhksaTl1xNEsZSwGGcTVhhksbTl1xNksaSwGGcTdhhkscTl1xOEsbSwGGcTlhhksdTl1xOkscSwGGcTthhkseTl1xPEsdSwGGcT1hhksfTl1xPkseSwGGcT9hhksgTl1xQEsfSwGGcUFhhkshTl1xQksgSwGGcUNhhksiTl1xREshSwGGcUVhhksjTl1xRksiSwGGcUdhhkskTl1xSEsjSwGGcUlhhkslTl1xSkskSwGGcUthhksmTl1xTEslSwGGcU1hhksnTl1xTksmSwGGcU9hhksoTl1xUEsnSwGGcVFhhkspTl1xUksoSwGGcVNhhksqTl1xVEspSwGGcVVhhksrTl1xVksqSwGGcVdhhkssTl1xWEsrSwGGcVlhhkstTl1xWkssSwGGcVthhksuTl1xXEstSwGGcV1hhksvTl1xXksuSwGGcV9hhkswTl1xYEsvSwGGcWFhhksxTl1xYkswSwGGcWNhhksyTl1xZEsxSwGGcWVhhkszTl1xZksySwGGcWdhhks0Tl1xaEszSwGGcWlhhks1Tl1xaks0SwGGcWthhks2Tl1xbEs1SwGGcW1hhks3Tl1xbks2SwGGcW9hhks4Tl1xcEs3SwGGcXFhhks5Tl1xcks4SwGGcXNhhks6Tl1xdEs5SwGGcXVhhks7Tl1xdks6SwGGcXdhhks8Tl1xeEs7SwGGcXlhhks9Tl1xeks8SwGGcXthhks+Tl1xfEs9SwGGcX1hhks/Tl1xfks+SwGGcX9hhktATl1xgEs/SwGGcYFhhktBTl1xgktASwGGcYNhhktCTl1xhEtBSwGGcYVhhktDTl1xhktCSwGGcYdhhktETl1xiEtDSwGGcYlhhktFTl1xiktESwGGcYthhktGTl1xjEtFSwGGcY1hhktHTl1xjktGSwGGcY9hhktITl1xkEtHSwGGcZFhhktJTl1xkktISwGGcZNhhktKTl1xlEtJSwGGcZVhhktLTl1xlktKSwGGcZdhhktMTl1xmEtLSwGGcZlhhktNTl1xmktMSwGGcZthhktOTl1xnEtNSwGGcZ1hhktPTl1xnktOSwGGcZ9hhktQTl1xoEtPSwGGcaFhhktRTl1xoktQSwGGcaNhhktSTl1xpEtRSwGGcaVhhktTTl1xpktSSwGGcadhhktUTl1xqEtTSwGGcalhhktVTl1xqktUSwGGcathhktWTl1xrEtVSwGGca1hhktXTl1xrktWSwGGca9hhktYTl1xsEtXSwGGcbFhhktZTl1xsktYSwGGcbNhhktaTl1xtEtZSwGGcbVhhktbTl1xtktaSwGGcbdhhktcTl1xuEtbSwGGcblhhktdTl1xuktcSwGGcbthhkteTl1xvEtdSwGGcb1hhktfTl1xvkteSwGGcb9hhktgTl1xwEtfSwGGccFhhkthTl1xwktgSwGGccNhhktiTl1xxEthSwGGccVhhktjTl1xxktiSwGGccdhhktkTl1xyEtjSwGGcclhhktlTl1xyktkSwGGccthhktmTl1xzEtlSwGGcc1hhktnTl1xzktmSwGGcc9hhktoTl1x0EtnSwGGcdFhhktpTl1x0ktoSwGGcdNhhktqTl1x1EtpSwGGcdVhhktrTl1x1ktqSwGGcddhhktsTl1x2EtrSwGGcdlhhkttTl1x2ktsSwGGcdthhktuTl1x3EttSwGGcd1hhktvTl1x3ktuSwGGcd9hhktwTl1x4EtvSwGGceFhhktxTl1x4ktwSwGGceNhhktyTl1x5EtxSwGGceVhhktzTl1x5ktySwGGcedhhkt0Tl1x6EtzSwGGcelhhkt1Tl1x6kt0SwGGcethhkt2Tl1x7Et1SwGGce1hhkt3Tl1x7kt2SwGGce9hhkt4Tl1x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SyNLJGVHQAIuuMAAAABdcugBAABLoWFHQBPfoOAAAABdcukBAABLS2FHQBO9bsAAAABdcuoBAABLg2FHQBLMCQAAAABdcusBAABLRWFHQAf25aAAAABdcuwBAAAoS7xLvWVHQBMFQkAAAABdcu0BAABLimFHQBPgSKAAAABdcu4BAABLTmFHQCxZaUAAAABdcu8BAAAoSyVLJmVHQBStOMAAAABdcvABAABLp2FHQBQvcWAAAABdcvEBAABLQmFHQBR3UKAAAABdcvIBAABLlmFHQBUbaYAAAABdcvMBAABLr2FHQBPuYaAAAABdcvQBAABLWGFHQBTUQmAAAABdcvUBAABLsWFHQCsjucAAAABdcvYBAABLOGFHQCVOmgAAAABdcvcBAABLK2FHQBObNCAAAABdcvgBAABLpmFHQBQvHeAAAABdcvkBAABLPGFHQBKeUiAAAABdcvoBAABLP2FHQCuF7gAAAABdcvsBAABLKGFHQBQOsmAAAABdcvwBAABLVGFHQCohOoAAAABdcv0BAABLJ2FHQBKUu2AAAABdcv4BAABLhWFHQCKdGQAAAABdcv8BAABLL2FHQBPVQqAAAABdcgACAABLqGFHQCe1esAAAABdcgECAAAoSw9LEGVHQBLd8uAAAABdcgICAABLO2FHQBLkmwAAAABdcgMCAABLmWFHQBQzPeAAAABdcgQCAABLXGFHQBKoAyAAAABdcgUCAABLdWFHQBSIiKAAAABdcgYCAABLiWFHQBLrg+AAAABdcgcCAABLY2FHQBPzA2AAAABdcggCAABLnGFHQBOfq4AAAABdcgkCAABLVmFHQBQ1qIAAAABdcgoCAABLomFHQBDn86AAAABdcgsCAABLrWFHQCwUS8AAAABdcgwCAAAoSwxLDUsOSxxLHUseSx9LIGVHQCXro2AAAABdcg0CAAAoSwBLAWVHQBLNwgAAAABdcg4CAABLlGFHQBRoM+AAAABdcg8CAABLVWFHQBQ+vUAAAABdchACAABLumFHQBTwlCAAAABdchECAABLV2FHQBIoTgAAAABdchICAABLnmFHQBXMLEAAAABdchMCAABLTWFHQC12tGAAAABdchQCAAAoSxtLKmVHQCsKvIAAAABdchUCAABLN2FHQAgPtKAAAABdchYCAAAoS21LcWVHQBRwGaAAAABdchcCAABLeGFHQBKB1OAAAABdchgCAABLT2FHQBXnzWAAAABdchkCAABLjGFHQBSUV8AAAABdchoCAABLYGFHQBOqvyAAAABdchsCAABLfmFHQBQUFqAAAABdchwCAABLq2FHQBS6ZaAAAABdch0CAABLZWFHQBJzVkAAAABdch4CAABLl2FHQBQMzcAAAABdch8CAABLaWFHQBUGRmAAAABdciACAABLrGFHQBPDReAAAABdciECAABLo2FHQBEGXgAAAABdciICAABLa2FHQBXlqQAAAABdciMCAABLOmFHQBSkzkAAAABdciQCAABLtGFHQBPf5mAAAABdciUCAABLqWFHQCcNvoAAAABdciYCAABLOWFHQBRNVqAAAABdcicCAABLR2FHQBRR/sAAAABdcigCAABLZGFHQBVCtuAAAABdcikCAABLpWFHQBLOMGAAAABdcioCAABLmGFHQBO6r0AAAABdcisCAABLWWFHQBRdNuAAAABdciwCAABLs2FHQBQoa+AAAABdci0CAABLSWFHQBNQgyAAAABdci4CAABLi2FHQAhpzIAAAABdci8CAAAoS2xLcEt0ZXWHVQpjb29yZEluZGV4cjACAABdcjECAABLAEu+hnIyAgAAYVULbGFiZWxPZmZzZXRyMwIAAEu+Tn2HVRJtaW5pbXVtTGFiZWxSYWRpdXNyNAIAAEu+RwAAAAAAAAAAfYdVCGRyYXdNb2RlcjUCAABLvksBfYdVCG9wdGlvbmFscjYCAAB9cjcCAAAoVQxzZXJpYWxOdW1iZXJyOAIAAIiJS75K/////32Hh1UHYmZhY3RvcnI5AgAAiIlLvkcAAAAAAAAAAH2Hh1UJb2NjdXBhbmN5cjoCAACIiUu+Rz/wAAAAAAAAfYeHdVUHZGlzcGxheXI7AgAAS76IfYd1Lg=='))
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVhdG9tc3ECXVUFbGFiZWxxA0sATn2HVQZyYWRpdXNxBEsATn2HVQtsYWJlbE9mZnNldHEFSwBOfYdVCGRyYXdNb2RlcQZLAE59h1UIb3B0aW9uYWxxB31VB2Rpc3BsYXlxCEsATn2HdS4='))
	crdInfo = cPickle.loads(base64.b64decode('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'))
	surfInfo = {'category': (0, None, {}), 'probeRadius': (0, None, {}), 'pointSize': (0, None, {}), 'name': [], 'density': (0, None, {}), 'colorMode': (0, None, {}), 'useLighting': (0, None, {}), 'transparencyBlendMode': (0, None, {}), 'molecule': [], 'smoothLines': (0, None, {}), 'lineWidth': (0, None, {}), 'allComponents': (0, None, {}), 'twoSidedLighting': (0, None, {}), 'customVisibility': [], 'drawMode': (0, None, {}), 'display': (0, None, {}), 'customColors': []}
	vrmlInfo = {'subid': (0, None, {}), 'display': (0, None, {}), 'id': (0, None, {}), 'vrmlString': [], 'name': (0, None, {})}
	colors = {'Ru': ((0.141176, 0.560784, 0.560784), 1, u'default'), 'Re': ((0.14902, 0.490196, 0.670588), 1, u'default'), 'Rf': ((0.8, 0, 0.34902), 1, u'default'), 'Ra': ((0, 0.490196, 0), 1, u'default'), 'Rb': ((0.439216, 0.180392, 0.690196), 1, u'default'), 'Rn': ((0.258824, 0.509804, 0.588235), 1, u'default'), 'Rh': ((0.0392157, 0.490196, 0.54902), 1, u'default'), 'Be': ((0.760784, 1, 0), 1, u'default'), 'Ba': ((0, 0.788235, 0), 1, u'default'), 'Bh': ((0.878431, 0, 0.219608), 1, u'default'), 'Bi': ((0.619608, 0.309804, 0.709804), 1, u'default'), 'Bk': ((0.541176, 0.309804, 0.890196), 1, u'default'), 'Br': ((0.65098, 0.160784, 0.160784), 1, u'default'), 'H': ((1, 1, 1), 1, u'default'), 'P': ((1, 0.501961, 0), 1, u'default'), 'Os': ((0.14902, 0.4, 0.588235), 1, u'default'), 'Ge': ((0.4, 0.560784, 0.560784), 1, u'default'), 'Gd': ((0.270588, 1, 0.780392), 1, u'default'), 'Ga': ((0.760784, 0.560784, 0.560784), 1, u'default'), 'Pr': ((0.85098, 1, 0.780392), 1, u'default'), 'Pt': ((0.815686, 0.815686, 0.878431), 1, u'default'), 'Pu': ((0, 0.419608, 1), 1, u'default'),
'C': ((0.564706, 0.564706, 0.564706), 1, u'default'), 'Pb': ((0.341176, 0.34902, 0.380392), 1, u'default'), 'Pa': ((0, 0.631373, 1), 1, u'default'), 'Pd': ((0, 0.411765, 0.521569), 1, u'default'), 'Cd': ((1, 0.85098, 0.560784), 1, u'default'), 'Po': ((0.670588, 0.360784, 0), 1, u'default'), 'Pm': ((0.639216, 1, 0.780392), 1, u'default'), 'Hs': ((0.901961, 0, 0.180392), 1, u'default'), 'Ho': ((0, 1, 0.611765), 1, u'default'), 'Hf': ((0.301961, 0.760784, 1), 1, u'default'), 'Hg': ((0.721569, 0.721569, 0.815686), 1, u'default'), 'He': ((0.85098, 1, 1), 1, u'default'), 'Md': ((0.701961, 0.0509804, 0.65098), 1, u'default'), 'Mg': ((0.541176, 1, 0), 1, u'default'), 'K': ((0.560784, 0.25098, 0.831373), 1, u'default'), 'Mn': ((0.611765, 0.478431, 0.780392), 1, u'default'), 'O': ((1, 0.0509804, 0.0509804), 1, u'default'), 'Mt': ((0.921569, 0, 0.14902), 1, u'default'), 'S': ((1, 1, 0.188235), 1, u'default'), 'W': ((0.129412, 0.580392, 0.839216), 1, u'default'), 'Zn': ((0.490196, 0.501961, 0.690196), 1, u'default'), 'Eu': ((0.380392, 1, 0.780392), 1, u'default'),
'Zr': ((0.580392, 0.878431, 0.878431), 1, u'default'), 'Er': ((0, 0.901961, 0.458824), 1, u'default'), 'Ni': ((0.313725, 0.815686, 0.313725), 1, u'default'), 'No': ((0.741176, 0.0509804, 0.529412), 1, u'default'), 'Na': ((0.670588, 0.360784, 0.94902), 1, u'default'), 'Nb': ((0.45098, 0.760784, 0.788235), 1, u'default'), 'Nd': ((0.780392, 1, 0.780392), 1, u'default'), 'Ne': ((0.701961, 0.890196, 0.960784), 1, u'default'), 'Np': ((0, 0.501961, 1), 1, u'default'), 'Fr': ((0.258824, 0, 0.4), 1, u'default'), 'Fe': ((0.878431, 0.4, 0.2), 1, u'default'), 'Fm': ((0.701961, 0.121569, 0.729412), 1, u'default'), 'B': ((1, 0.709804, 0.709804), 1, u'default'), 'F': ((0.564706, 0.878431, 0.313725), 1, u'default'), 'Sr': ((0, 1, 0), 1, u'default'), 'N': ((0.188235, 0.313725, 0.972549), 1, u'default'), 'Kr': ((0.360784, 0.721569, 0.819608), 1, u'default'), 'Si': ((0.941176, 0.784314, 0.627451), 1, u'default'), 'Sn': ((0.4, 0.501961, 0.501961), 1, u'default'), 'Sm': ((0.560784, 1, 0.780392), 1, u'default'), 'V': ((0.65098, 0.65098, 0.670588), 1, u'default'), 'Sc': ((0.901961, 0.901961, 0.901961), 1, u'default'),
'Sb': ((0.619608, 0.388235, 0.709804), 1, u'default'), 'Sg': ((0.85098, 0, 0.270588), 1, u'default'), 'Se': ((1, 0.631373, 0), 1, u'default'), 'Co': ((0.941176, 0.564706, 0.627451), 1, u'default'), 'Cm': ((0.470588, 0.360784, 0.890196), 1, u'default'), 'Cl': ((0.121569, 0.941176, 0.121569), 1, u'default'), 'Ca': ((0.239216, 1, 0), 1, u'default'), 'Cf': ((0.631373, 0.211765, 0.831373), 1, u'default'), 'Ce': ((1, 1, 0.780392), 1, u'default'), 'Xe': ((0.258824, 0.619608, 0.690196), 1, u'default'), 'Tm': ((0, 0.831373, 0.321569), 1, u'default'), 'Cs': ((0.341176, 0.0901961, 0.560784), 1, u'default'), 'Cr': ((0.541176, 0.6, 0.780392), 1, u'default'), 'Cu': ((0.784314, 0.501961, 0.2), 1, u'default'), 'La': ((0.439216, 0.831373, 1), 1, u'default'), 'Li': ((0.8, 0.501961, 1), 1, u'default'), 'Tl': ((0.65098, 0.329412, 0.301961), 1, u'default'), 'Lu': ((0, 0.670588, 0.141176), 1, u'default'), 'Lr': ((0.780392, 0, 0.4), 1, u'default'), 'Th': ((0, 0.729412, 1), 1, u'default'), 'Ti': ((0.74902, 0.760784, 0.780392), 1, u'default'), 'Te': ((0.831373, 0.478431, 0), 1, u'default'),
'Tb': ((0.188235, 1, 0.780392), 1, u'default'), 'Tc': ((0.231373, 0.619608, 0.619608), 1, u'default'), 'Ta': ((0.301961, 0.65098, 1), 1, u'default'), 'Yb': ((0, 0.74902, 0.219608), 1, u'default'), 'Db': ((0.819608, 0, 0.309804), 1, u'default'), 'Dy': ((0.121569, 1, 0.780392), 1, u'default'), 'At': ((0.458824, 0.309804, 0.270588), 1, u'default'), 'I': ((0.580392, 0, 0.580392), 1, u'default'), 'medium purple': ((0.576471, 0.439216, 0.858824), 1, u'default'), 'U': ((0, 0.560784, 1), 1, u'default'), 'Y': ((0.580392, 1, 1), 1, u'default'), 'Ac': ((0.439216, 0.670588, 0.980392), 1, u'default'), 'Ag': ((0.752941, 0.752941, 0.752941), 1, u'default'), 'Ir': ((0.0901961, 0.329412, 0.529412), 1, u'default'), 'Am': ((0.329412, 0.360784, 0.94902), 1, u'default'), 'Al': ((0.74902, 0.65098, 0.65098), 1, u'default'), 'As': ((0.741176, 0.501961, 0.890196), 1, u'default'), 'Ar': ((0.501961, 0.819608, 0.890196), 1, u'default'), 'Au': ((1, 0.819608, 0.137255), 1, u'default'), 'Es': ((0.701961, 0.121569, 0.831373), 1, u'default'), 'In': ((0.65098, 0.458824, 0.45098), 1, u'default'),
'Mo': ((0.329412, 0.709804, 0.709804), 1, u'default')}
	materials = {u'default': ((0.85, 0.85, 0.85), 30)}
	pbInfo = {'category': [u'distance monitor'], 'bondInfo': [{'color': (0, None, {}), 'atoms': [], 'label': (0, None, {}), 'halfbond': (0, None, {}), 'labelColor': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {})}], 'lineType': (1, 2, {}), 'color': (1, 9, {}), 'optional': {'fixedLabels': (True, False, (1, False, {}))}, 'display': (1, True, {}), 'showStubBonds': (1, False, {}), 'lineWidth': (1, 1, {}), 'stickScale': (1, 1, {}), 'id': [-2]}
	modelAssociations = {}
	colorInfo = (12, (u'green', (0, 1, 0, 1)), {(u'', (0.74, 0.26, 0, 1)): [6], (u'', (1, 0, 0, 1)): [4], (u'white', (1, 1, 1, 1)): [10], (u'', (0.6, 0.4, 0, 1)): [5], (u'', (0, 1, 0, 1)): [1], (u'', (0.4, 0.6, 0, 1)): [2], (u'yellow', (1, 1, 0, 1)): [9], (u'', (0, 0.6, 0.4, 1)): [8], (u'gray', (0.745, 0.745, 0.745, 1)): [0], (u'', (0, 0, 1, 1)): [3], (u'', (0, 0.8, 0.2, 1)): [7]})
	viewerInfo = {'cameraAttrs': {'center': (-176.40135990212, -609.08500647589, -360.57543209591), 'fieldOfView': 13.3923, 'nearFar': (-167.72291773989, -560.00437486258), 'ortho': False, 'eyeSeparation': 50.8, 'focal': 24.9618}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': False, 'showSilhouette': True, 'showShadows': False, 'viewSize': 387.13079185206, 'labelsOnTop': True, 'depthCueRange': (0.5, 1), 'silhouetteWidth': 3, 'singleLayerTransparency': True, 'shadowTextureSize': 2048, 'backgroundImage': [None, 1, 2, 1, 0, 0], 'backgroundGradient': [('Chimera default', [(1, 1, 1, 1), (0, 0, 1, 1)], 1), 1, 0, 0], 'depthCue': False, 'highlight': 0, 'scaleFactor': 1.219145976618, 'angleDependentTransparency': True, 'backgroundMethod': 0}, 'viewerHL': 11, 'cameraMode': 'mono', 'detail': 5, 'viewerFog': None, 'viewerBG': 10}

	replyobj.status("Initializing session restore...", blankAfter=0,
		secondary=True)
	from SimpleSession.versions.v61 import expandSummary
	init(dict(enumerate(expandSummary(colorInfo))))
	replyobj.status("Restoring colors...", blankAfter=0,
		secondary=True)
	restoreColors(colors, materials)
	replyobj.status("Restoring molecules...", blankAfter=0,
		secondary=True)
	restoreMolecules(molInfo, resInfo, atomInfo, bondInfo, crdInfo)
	replyobj.status("Restoring surfaces...", blankAfter=0,
		secondary=True)
	restoreSurfaces(surfInfo)
	replyobj.status("Restoring VRML models...", blankAfter=0,
		secondary=True)
	restoreVRML(vrmlInfo)
	replyobj.status("Restoring pseudobond groups...", blankAfter=0,
		secondary=True)
	restorePseudoBondGroups(pbInfo)
	replyobj.status("Restoring model associations...", blankAfter=0,
		secondary=True)
	restoreModelAssociations(modelAssociations)
	replyobj.status("Restoring camera...", blankAfter=0,
		secondary=True)
	restoreViewer(viewerInfo)

try:
	restoreCoreModels()
except:
	reportRestoreError("Error restoring core models")

	replyobj.status("Restoring extension info...", blankAfter=0,
		secondary=True)


try:
	import StructMeasure
	from StructMeasure.DistMonitor import restoreDistances
	registerAfterModelsCB(restoreDistances, 1)
except:
	reportRestoreError("Error restoring distances in session")


def restoreMidasBase():
	formattedPositions = {'session-start': (0.44888994912461, 123.31664595174, (-15.9236, -47.7896, -126.37201595396), (190.67898936959, -203.91753837193), 24.9618, {(7, 0): ((-131.1498588643062, -403.365098219722, -315.4045739504914), (-0.14171622176601884, -0.8784667247786911, 0.45630332668627804, 176.2742795356673)), (3, 0): ((-131.1498588643062, -403.365098219722, -315.4045739504914), (-0.14171622176601884, -0.8784667247786911, 0.45630332668627804, 176.2742795356673)), (8, 0): ((-131.1498588643062, -403.365098219722, -315.4045739504914), (-0.14171622176601884, -0.8784667247786911, 0.45630332668627804, 176.2742795356673)), (6, 0): ((-131.1498588643062, -403.365098219722, -315.4045739504914), (-0.14171622176601884, -0.8784667247786911, 0.45630332668627804, 176.2742795356673)), (2, 0): ((-131.1498588643062, -403.365098219722, -315.4045739504914), (-0.14171622176601884, -0.8784667247786911, 0.45630332668627804, 176.2742795356673)), (5, 0): ((-131.1498588643062, -403.365098219722, -315.4045739504914), (-0.14171622176601884, -0.8784667247786911, 0.45630332668627804, 176.2742795356673)), (10, 0): ((-153.02106760033, -412.19205997895, -309.59672199723), (0.234967244557893, 0.8787537979131107, -0.41543008634204054, 179.4068270277408)), (1, 0): ((-131.1498588643062, -403.365098219722, -315.4045739504914), (-0.14171622176601884, -0.8784667247786911, 0.45630332668627804, 176.2742795356673)), (4, 0): ((-131.1498588643062, -403.365098219722, -315.4045739504914), (-0.14171622176601884, -0.8784667247786911, 0.45630332668627804, 176.2742795356673))}, {(6, 0, 'Volume'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, False, 5.0), (3, 0, 'Volume'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, False, 5.0), (5, 0, 'Volume'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, False, 5.0), (2, 0, 'Volume'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, False, 5.0), (10, 0, 'Molecule'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, False, 5.0), (7, 0, 'Volume'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, False, 5.0), (4, 0, 'Volume'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, False, 5.0), (1, 0, 'Volume'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, False, 5.0), (8, 0, 'Volume'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, False, 5.0)}, 4, (-170.0111970129073, -608.1364183490848, -398.5852177292626), False, 13.3923)}
	import Midas
	Midas.restoreMidasBase(formattedPositions)
try:
	restoreMidasBase()
except:
	reportRestoreError('Error restoring Midas base state')


def restoreMidasText():
	from Midas import midas_text
	midas_text.aliases = {}
	midas_text.userSurfCategories = {}

try:
	restoreMidasText()
except:
	reportRestoreError('Error restoring Midas text state')

geomData = {'AxisManager': {}, 'CentroidManager': {}, 'PlaneManager': {}}

try:
	from StructMeasure.Geometry import geomManager
	geomManager._restoreSession(geomData)
except:
	reportRestoreError("Error restoring geometry objects in session")


def restoreSession_RibbonStyleEditor():
	import SimpleSession
	import RibbonStyleEditor
	userScalings = [('licorice', [[0.35, 0.35], [0.35, 0.35], [0.35, 0.35], [0.35, 0.35, 0.35, 0.35], [0.35, 0.35]])]
	userXSections = []
	userResidueClasses = []
	residueData = [(1, 'Chimera default', 'rounded', u'unknown'), (2, 'Chimera default', 'rounded', u'unknown'), (3, 'Chimera default', 'rounded', u'unknown'), (4, 'Chimera default', 'rounded', u'unknown'), (5, 'Chimera default', 'rounded', u'unknown'), (6, 'Chimera default', 'rounded', u'unknown'), (7, 'Chimera default', 'rounded', u'unknown'), (8, 'Chimera default', 'rounded', u'unknown'), (9, 'Chimera default', 'rounded', u'unknown'), (10, 'Chimera default', 'rounded', u'unknown'), (11, 'Chimera default', 'rounded', u'unknown'), (12, 'Chimera default', 'rounded', u'unknown'), (13, 'Chimera default', 'rounded', u'unknown'), (14, 'Chimera default', 'rounded', u'unknown'), (15, 'Chimera default', 'rounded', u'unknown'), (16, 'Chimera default', 'rounded', u'unknown'), (17, 'Chimera default', 'rounded', u'unknown'), (18, 'Chimera default', 'rounded', u'unknown'), (19, 'Chimera default', 'rounded', u'unknown'), (20, 'Chimera default', 'rounded', u'unknown'), (21, 'Chimera default', 'rounded', u'unknown'), (22, 'Chimera default', 'rounded', u'unknown'), (23, 'Chimera default', 'rounded', u'unknown'),
(24, 'Chimera default', 'rounded', u'unknown'), (25, 'Chimera default', 'rounded', u'unknown'), (26, 'Chimera default', 'rounded', u'unknown'), (27, 'Chimera default', 'rounded', u'unknown'), (28, 'Chimera default', 'rounded', u'unknown'), (29, 'Chimera default', 'rounded', u'unknown'), (30, 'Chimera default', 'rounded', u'unknown'), (31, 'Chimera default', 'rounded', u'unknown'), (32, 'Chimera default', 'rounded', u'unknown'), (33, 'Chimera default', 'rounded', u'unknown'), (34, 'Chimera default', 'rounded', u'unknown'), (35, 'Chimera default', 'rounded', u'unknown'), (36, 'Chimera default', 'rounded', u'unknown'), (37, 'Chimera default', 'rounded', u'unknown'), (38, 'Chimera default', 'rounded', u'unknown'), (39, 'Chimera default', 'rounded', u'unknown'), (40, 'Chimera default', 'rounded', u'unknown'), (41, 'Chimera default', 'rounded', u'unknown'), (42, 'Chimera default', 'rounded', u'unknown'), (43, 'Chimera default', 'rounded', u'unknown'), (44, 'Chimera default', 'rounded', u'unknown'), (45, 'Chimera default', 'rounded', u'unknown'), (46, 'Chimera default', 'rounded', u'unknown'),
(47, 'Chimera default', 'rounded', u'unknown'), (48, 'Chimera default', 'rounded', u'unknown'), (49, 'Chimera default', 'rounded', u'unknown'), (50, 'Chimera default', 'rounded', u'unknown'), (51, 'Chimera default', 'rounded', u'unknown'), (52, 'Chimera default', 'rounded', u'unknown'), (53, 'Chimera default', 'rounded', u'unknown'), (54, 'Chimera default', 'rounded', u'unknown'), (55, 'Chimera default', 'rounded', u'unknown'), (56, 'Chimera default', 'rounded', u'unknown'), (57, 'Chimera default', 'rounded', u'unknown'), (58, 'Chimera default', 'rounded', u'unknown'), (59, 'Chimera default', 'rounded', u'unknown'), (60, 'Chimera default', 'rounded', u'unknown'), (61, 'Chimera default', 'rounded', u'unknown'), (62, 'Chimera default', 'rounded', u'unknown'), (63, 'Chimera default', 'rounded', u'unknown'), (64, 'Chimera default', 'rounded', u'unknown'), (65, 'Chimera default', 'rounded', u'unknown'), (66, 'Chimera default', 'rounded', u'unknown'), (67, 'Chimera default', 'rounded', u'unknown'), (68, 'Chimera default', 'rounded', u'unknown'), (69, 'Chimera default', 'rounded', u'unknown'),
(70, 'Chimera default', 'rounded', u'unknown'), (71, 'Chimera default', 'rounded', u'unknown'), (72, 'Chimera default', 'rounded', u'unknown'), (73, 'Chimera default', 'rounded', u'unknown'), (74, 'Chimera default', 'rounded', u'unknown'), (75, 'Chimera default', 'rounded', u'unknown'), (76, 'Chimera default', 'rounded', u'unknown'), (77, 'Chimera default', 'rounded', u'unknown'), (78, 'Chimera default', 'rounded', u'unknown'), (79, 'Chimera default', 'rounded', u'unknown'), (80, 'Chimera default', 'rounded', u'unknown'), (81, 'Chimera default', 'rounded', u'unknown'), (82, 'Chimera default', 'rounded', u'unknown'), (83, 'Chimera default', 'rounded', u'unknown'), (84, 'Chimera default', 'rounded', u'unknown'), (85, 'Chimera default', 'rounded', u'unknown'), (86, 'Chimera default', 'rounded', u'unknown'), (87, 'Chimera default', 'rounded', u'unknown'), (88, 'Chimera default', 'rounded', u'unknown'), (89, 'Chimera default', 'rounded', u'unknown'), (90, 'Chimera default', 'rounded', u'unknown'), (91, 'Chimera default', 'rounded', u'unknown'), (92, 'Chimera default', 'rounded', u'unknown'),
(93, 'Chimera default', 'rounded', u'unknown'), (94, 'Chimera default', 'rounded', u'unknown'), (95, 'Chimera default', 'rounded', u'unknown'), (96, 'Chimera default', 'rounded', u'unknown'), (97, 'Chimera default', 'rounded', u'unknown'), (98, 'Chimera default', 'rounded', u'unknown'), (99, 'Chimera default', 'rounded', u'unknown'), (100, 'Chimera default', 'rounded', u'unknown'), (101, 'Chimera default', 'rounded', u'unknown'), (102, 'Chimera default', 'rounded', u'unknown'), (103, 'Chimera default', 'rounded', u'unknown'), (104, 'Chimera default', 'rounded', u'unknown'), (105, 'Chimera default', 'rounded', u'unknown'), (106, 'Chimera default', 'rounded', u'unknown'), (107, 'Chimera default', 'rounded', u'unknown'), (108, 'Chimera default', 'rounded', u'unknown'), (109, 'Chimera default', 'rounded', u'unknown'), (110, 'Chimera default', 'rounded', u'unknown'), (111, 'Chimera default', 'rounded', u'unknown'), (112, 'Chimera default', 'rounded', u'unknown'), (113, 'Chimera default', 'rounded', u'unknown'), (114, 'Chimera default', 'rounded', u'unknown'),
(115, 'Chimera default', 'rounded', u'unknown'), (116, 'Chimera default', 'rounded', u'unknown'), (117, 'Chimera default', 'rounded', u'unknown'), (118, 'Chimera default', 'rounded', u'unknown'), (119, 'Chimera default', 'rounded', u'unknown'), (120, 'Chimera default', 'rounded', u'unknown'), (121, 'Chimera default', 'rounded', u'unknown'), (122, 'Chimera default', 'rounded', u'unknown'), (123, 'Chimera default', 'rounded', u'unknown'), (124, 'Chimera default', 'rounded', u'unknown'), (125, 'Chimera default', 'rounded', u'unknown'), (126, 'Chimera default', 'rounded', u'unknown'), (127, 'Chimera default', 'rounded', u'unknown'), (128, 'Chimera default', 'rounded', u'unknown'), (129, 'Chimera default', 'rounded', u'unknown'), (130, 'Chimera default', 'rounded', u'unknown'), (131, 'Chimera default', 'rounded', u'unknown'), (132, 'Chimera default', 'rounded', u'unknown'), (133, 'Chimera default', 'rounded', u'unknown'), (134, 'Chimera default', 'rounded', u'unknown'), (135, 'Chimera default', 'rounded', u'unknown'), (136, 'Chimera default', 'rounded', u'unknown'),
(137, 'Chimera default', 'rounded', u'unknown'), (138, 'Chimera default', 'rounded', u'unknown'), (139, 'Chimera default', 'rounded', u'unknown'), (140, 'Chimera default', 'rounded', u'unknown'), (141, 'Chimera default', 'rounded', u'unknown'), (142, 'Chimera default', 'rounded', u'unknown'), (143, 'Chimera default', 'rounded', u'unknown'), (144, 'Chimera default', 'rounded', u'unknown'), (145, 'Chimera default', 'rounded', u'unknown'), (146, 'Chimera default', 'rounded', u'unknown'), (147, 'Chimera default', 'rounded', u'unknown'), (148, 'Chimera default', 'rounded', u'unknown'), (149, 'Chimera default', 'rounded', u'unknown'), (150, 'Chimera default', 'rounded', u'unknown'), (151, 'Chimera default', 'rounded', u'unknown'), (152, 'Chimera default', 'rounded', u'unknown'), (153, 'Chimera default', 'rounded', u'unknown'), (154, 'Chimera default', 'rounded', u'unknown'), (155, 'Chimera default', 'rounded', u'unknown'), (156, 'Chimera default', 'rounded', u'unknown'), (157, 'Chimera default', 'rounded', u'unknown'), (158, 'Chimera default', 'rounded', u'unknown'),
(159, 'Chimera default', 'rounded', u'unknown'), (160, 'Chimera default', 'rounded', u'unknown'), (161, 'Chimera default', 'rounded', u'unknown'), (162, 'Chimera default', 'rounded', u'unknown'), (163, 'Chimera default', 'rounded', u'unknown'), (164, 'Chimera default', 'rounded', u'unknown'), (165, 'Chimera default', 'rounded', u'unknown'), (166, 'Chimera default', 'rounded', u'unknown'), (167, 'Chimera default', 'rounded', u'unknown'), (168, 'Chimera default', 'rounded', u'unknown'), (169, 'Chimera default', 'rounded', u'unknown'), (170, 'Chimera default', 'rounded', u'unknown'), (171, 'Chimera default', 'rounded', u'unknown'), (172, 'Chimera default', 'rounded', u'unknown'), (173, 'Chimera default', 'rounded', u'unknown'), (174, 'Chimera default', 'rounded', u'unknown'), (175, 'Chimera default', 'rounded', u'unknown'), (176, 'Chimera default', 'rounded', u'unknown'), (177, 'Chimera default', 'rounded', u'unknown'), (178, 'Chimera default', 'rounded', u'unknown'), (179, 'Chimera default', 'rounded', u'unknown'), (180, 'Chimera default', 'rounded', u'unknown'),
(181, 'Chimera default', 'rounded', u'unknown'), (182, 'Chimera default', 'rounded', u'unknown'), (183, 'Chimera default', 'rounded', u'unknown'), (184, 'Chimera default', 'rounded', u'unknown'), (185, 'Chimera default', 'rounded', u'unknown'), (186, 'Chimera default', 'rounded', u'unknown'), (187, 'Chimera default', 'rounded', u'unknown'), (188, 'Chimera default', 'rounded', u'unknown'), (189, 'Chimera default', 'rounded', u'unknown'), (190, 'Chimera default', 'rounded', u'unknown')]
	flags = RibbonStyleEditor.NucleicDefault1
	SimpleSession.registerAfterModelsCB(RibbonStyleEditor.restoreState,
				(userScalings, userXSections,
				userResidueClasses, residueData, flags))
try:
	restoreSession_RibbonStyleEditor()
except:
	reportRestoreError("Error restoring RibbonStyleEditor state")

trPickle = 'gAJjQW5pbWF0ZS5UcmFuc2l0aW9ucwpUcmFuc2l0aW9ucwpxASmBcQJ9cQMoVQxjdXN0b21fc2NlbmVxBGNBbmltYXRlLlRyYW5zaXRpb24KVHJhbnNpdGlvbgpxBSmBcQZ9cQcoVQZmcmFtZXNxCEsBVQ1kaXNjcmV0ZUZyYW1lcQlLAVUKcHJvcGVydGllc3EKXXELVQNhbGxxDGFVBG5hbWVxDVUMY3VzdG9tX3NjZW5lcQ5VBG1vZGVxD1UGbGluZWFycRB1YlUIa2V5ZnJhbWVxEWgFKYFxEn1xEyhoCEsUaAlLAWgKXXEUaAxhaA1VCGtleWZyYW1lcRVoD2gQdWJVBXNjZW5lcRZoBSmBcRd9cRgoaAhLAWgJSwFoCl1xGWgMYWgNVQVzY2VuZXEaaA9oEHVidWIu'
scPickle = 'gAJjQW5pbWF0ZS5TY2VuZXMKU2NlbmVzCnEBKYFxAn1xA1UHbWFwX2lkc3EEfXNiLg=='
kfPickle = 'gAJjQW5pbWF0ZS5LZXlmcmFtZXMKS2V5ZnJhbWVzCnEBKYFxAn1xA1UHZW50cmllc3EEXXEFc2Iu'
def restoreAnimation():
	'A method to unpickle and restore animation objects'
	# Scenes must be unpickled after restoring transitions, because each
	# scene links to a 'scene' transition. Likewise, keyframes must be 
	# unpickled after restoring scenes, because each keyframe links to a scene.
	# The unpickle process is left to the restore* functions, it's 
	# important that it doesn't happen prior to calling those functions.
	import SimpleSession
	from Animate.Session import restoreTransitions
	from Animate.Session import restoreScenes
	from Animate.Session import restoreKeyframes
	SimpleSession.registerAfterModelsCB(restoreTransitions, trPickle)
	SimpleSession.registerAfterModelsCB(restoreScenes, scPickle)
	SimpleSession.registerAfterModelsCB(restoreKeyframes, kfPickle)
try:
	restoreAnimation()
except:
	reportRestoreError('Error in Animate.Session')

def restoreLightController():
	import Lighting
	Lighting._setFromParams({'ratio': 1.25, 'brightness': 1.16, 'material': [30.0, (0.85, 0.85, 0.85), 1.0], 'back': [(0.3574067443365933, 0.6604015517481455, -0.6604015517481456), (1.0, 1.0, 1.0), 0.0], 'mode': 'two-point', 'key': [(-0.3574067443365933, 0.6604015517481455, 0.6604015517481456), (1.0, 1.0, 1.0), 1.0], 'contrast': 0.83, 'fill': [(0.2505628070857316, 0.2505628070857316, 0.9351131265310294), (1.0, 1.0, 1.0), 0.0]})
try:
	restoreLightController()
except:
	reportRestoreError("Error restoring lighting parameters")


def restore_volume_data():
 volume_data_state = \
  {
   'class': 'Volume_Manager_State',
   'data_and_regions_state': [
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90.0, 90.0, 90.0, ),
       'class': 'Data_State',
       'file_type': 'mrc',
       'grid_id': '',
       'name': u'SEA_complex_SEA3.mrc',
       'path': u'SEA_complex_SEA3.mrc',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 0.7, 0.7, 1, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 49, 54, 50, ),
          [ 1, 1, 1, ],
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 2,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 74, 72, 74, ),
            ),
            (
             ( 0, 0, 0, ),
             ( 50, 49, 48, ),
            ),
            (
             ( 0, 0, 0, ),
             ( 49, 54, 50, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'box_faces': False,
          'bt_correction': 0,
          'cap_faces': 1,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': 1,
          'dim_transparent_voxels': 1,
          'flip_normals': 0,
          'limit_voxel_count': 1,
          'line_thickness': 1.0,
          'linear_interpolation': 1,
          'maximum_intensity_projection': 0,
          'mesh_lighting': 1,
          'minimal_texture_memory': 0,
          'orthoplane_positions': ( 0, 0, 0, ),
          'orthoplanes_shown': ( False, False, False, ),
          'outline_box_linewidth': 1.0,
          'outline_box_rgb': ( 1.0, 1.0, 1.0, ),
          'projection_mode': 'auto',
          'show_outline_box': 0,
          'smooth_lines': 0,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': 1,
          'subdivide_surface': 0,
          'subdivision_levels': 1,
          'surface_smoothing': 0,
          'two_sided_lighting': 1,
          'version': 1,
          'voxel_limit': 0.135,
         },
        'representation': 'surface',
        'session_volume_id': 'G-.f39Gs3-(v\\Fn||\n/==3n*<Omal#&>',
        'solid_brightness_factor': 1.0,
        'solid_colors': [
          ( 0.7, 0.7, 1, 1, ),
          ( 0.7, 0.7, 1, 1, ),
          ( 0.7, 0.7, 1, 1, ),
         ],
        'solid_levels': [
          ( 0.0, 0, ),
          ( 9.044557251036167e-05, 0.99, ),
          ( 0.016444649547338486, 1, ),
         ],
        'solid_model': None,
        'surface_brightness_factor': 1.0,
        'surface_colors': [
          ( 0.0, 0.07407407407407407, 0.8636363636363636, 1.0, ),
         ],
        'surface_levels': [ 0.012699425649229757, ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( 0.0, 0.0, -1.0, ),
          'clip_plane_origin': ( 0.0, 0.0, 0.0, ),
          'clip_thickness': 5.0,
          'display': True,
          'id': 4,
          'name': u'SEA_complex_SEA3.mrc',
          'osl_identifier': u'#4',
          'silhouette': True,
          'subid': 0,
          'use_clip_plane': False,
          'use_clip_thickness': False,
          'version': 5,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 85.73205662677236,
            'rotation_axis': ( -0.5492039978818357, 0.611441099003517, 0.5696619621845749, ),
            'translation': ( -264.72219474443557, -786.5882321529023, -487.26238546005493, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.5,
        'transparency_factor': 0.2,
        'version': 6,
       },
      ],
     ),
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90.0, 90.0, 90.0, ),
       'class': 'Data_State',
       'file_type': 'mrc',
       'grid_id': '',
       'name': u'SEA_complex_Sec13.mrc',
       'path': u'SEA_complex_Sec13.mrc',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 0.7, 0.7, 0.7, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 49, 54, 50, ),
          [ 1, 1, 1, ],
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 2,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 74, 72, 74, ),
            ),
            (
             ( 0, 0, 0, ),
             ( 50, 49, 48, ),
            ),
            (
             ( 0, 0, 0, ),
             ( 49, 54, 50, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'box_faces': False,
          'bt_correction': 0,
          'cap_faces': 1,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': 1,
          'dim_transparent_voxels': 1,
          'flip_normals': 0,
          'limit_voxel_count': 1,
          'line_thickness': 1.0,
          'linear_interpolation': 1,
          'maximum_intensity_projection': 0,
          'mesh_lighting': 1,
          'minimal_texture_memory': 0,
          'orthoplane_positions': ( 0, 0, 0, ),
          'orthoplanes_shown': ( False, False, False, ),
          'outline_box_linewidth': 1.0,
          'outline_box_rgb': ( 1.0, 1.0, 1.0, ),
          'projection_mode': 'auto',
          'show_outline_box': 0,
          'smooth_lines': 0,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': 1,
          'subdivide_surface': 0,
          'subdivision_levels': 1,
          'surface_smoothing': 0,
          'two_sided_lighting': 1,
          'version': 1,
          'voxel_limit': 0.135,
         },
        'representation': 'surface',
        'session_volume_id': '(q&f|qV\nbTOf+rC<\\>_|^N|`Aq\tH2$01',
        'solid_brightness_factor': 1.0,
        'solid_colors': [
          ( 1.0, 1.0, 1.0, 1, ),
          ( 1.0, 1.0, 1.0, 1, ),
         ],
        'solid_levels': [
          ( 0.0, 0, ),
          ( 0.017253417521715164, 1, ),
         ],
        'solid_model': None,
        'surface_brightness_factor': 1.0,
        'surface_colors': [
          ( 0.2727272727272727, 0.7272727272727273, 0.6363636363636364, 1.0, ),
         ],
        'surface_levels': [ 0.0175341728823667, ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( 0.0, 0.0, -1.0, ),
          'clip_plane_origin': ( 0.0, 0.0, 0.0, ),
          'clip_thickness': 5.0,
          'display': True,
          'id': 1,
          'name': u'SEA_complex_Sec13.mrc',
          'osl_identifier': u'#1',
          'silhouette': True,
          'subid': 0,
          'use_clip_plane': False,
          'use_clip_thickness': False,
          'version': 5,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 85.73205662677236,
            'rotation_axis': ( -0.5492039978818357, 0.611441099003517, 0.5696619621845749, ),
            'translation': ( -264.72219474443557, -786.5882321529023, -487.26238546005493, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.5,
        'transparency_factor': 0.0,
        'version': 6,
       },
      ],
     ),
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90.0, 90.0, 90.0, ),
       'class': 'Data_State',
       'file_type': 'mrc',
       'grid_id': '',
       'name': u'SEA_complex_Npr2.mrc',
       'path': u'SEA_complex_Npr2.mrc',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 0.9, 0.75, 0.6, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 49, 54, 50, ),
          [ 1, 1, 1, ],
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 2,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 74, 72, 74, ),
            ),
            (
             ( 0, 0, 0, ),
             ( 50, 49, 48, ),
            ),
            (
             ( 0, 0, 0, ),
             ( 49, 54, 50, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'box_faces': False,
          'bt_correction': 0,
          'cap_faces': 1,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': 1,
          'dim_transparent_voxels': 1,
          'flip_normals': 0,
          'limit_voxel_count': 1,
          'line_thickness': 1.0,
          'linear_interpolation': 1,
          'maximum_intensity_projection': 0,
          'mesh_lighting': 1,
          'minimal_texture_memory': 0,
          'orthoplane_positions': ( 0, 0, 0, ),
          'orthoplanes_shown': ( False, False, False, ),
          'outline_box_linewidth': 1.0,
          'outline_box_rgb': ( 1.0, 1.0, 1.0, ),
          'projection_mode': 'auto',
          'show_outline_box': 0,
          'smooth_lines': 0,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': 1,
          'subdivide_surface': 0,
          'subdivision_levels': 1,
          'surface_smoothing': 0,
          'two_sided_lighting': 1,
          'version': 1,
          'voxel_limit': 0.135,
         },
        'representation': 'mesh',
        'session_volume_id': '~.0F08\x0beaC}i4+\x0b/*QT$Q[AkO4\x0czas%h',
        'solid_brightness_factor': 1.0,
        'solid_colors': [
          ( 1.0, 0.8333333333333333, 0.6666666666666666, 1, ),
          ( 1.0, 0.8333333333333333, 0.6666666666666666, 1, ),
          ( 1.0, 0.8333333333333333, 0.6666666666666666, 1, ),
         ],
        'solid_levels': [
          ( 0.0, 0, ),
          ( 0.00026951692916918547, 0.99, ),
          ( 0.0019320209976285696, 1, ),
         ],
        'solid_model': None,
        'surface_brightness_factor': 1.0,
        'surface_colors': [
          ( 0.9545454545454546, 0.7727272727272727, 0.4090909090909091, 1.0, ),
         ],
        'surface_levels': [ 0.0032271677241732448, ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( 0.0, 0.0, -1.0, ),
          'clip_plane_origin': ( 0.0, 0.0, 0.0, ),
          'clip_thickness': 5.0,
          'display': True,
          'id': 8,
          'name': u'SEA_complex_Npr2.mrc',
          'osl_identifier': u'#8',
          'silhouette': True,
          'subid': 0,
          'use_clip_plane': False,
          'use_clip_thickness': False,
          'version': 5,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 85.73205662677236,
            'rotation_axis': ( -0.5492039978818357, 0.611441099003517, 0.5696619621845749, ),
            'translation': ( -264.72219474443557, -786.5882321529023, -487.26238546005493, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.5,
        'transparency_factor': 0.0,
        'version': 6,
       },
      ],
     ),
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90.0, 90.0, 90.0, ),
       'class': 'Data_State',
       'file_type': 'mrc',
       'grid_id': '',
       'name': u'SEA_complex_SEA4.mrc',
       'path': u'SEA_complex_SEA4.mrc',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 0.7, 1, 1, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 49, 54, 50, ),
          [ 1, 1, 1, ],
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 2,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 74, 72, 74, ),
            ),
            (
             ( 0, 0, 0, ),
             ( 50, 49, 48, ),
            ),
            (
             ( 0, 0, 0, ),
             ( 49, 54, 50, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'box_faces': False,
          'bt_correction': 0,
          'cap_faces': 1,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': 1,
          'dim_transparent_voxels': 1,
          'flip_normals': 0,
          'limit_voxel_count': 1,
          'line_thickness': 1.0,
          'linear_interpolation': 1,
          'maximum_intensity_projection': 0,
          'mesh_lighting': 1,
          'minimal_texture_memory': 0,
          'orthoplane_positions': ( 0, 0, 0, ),
          'orthoplanes_shown': ( False, False, False, ),
          'outline_box_linewidth': 1.0,
          'outline_box_rgb': ( 1.0, 1.0, 1.0, ),
          'projection_mode': 'auto',
          'show_outline_box': 0,
          'smooth_lines': 0,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': 1,
          'subdivide_surface': 0,
          'subdivision_levels': 1,
          'surface_smoothing': 0,
          'two_sided_lighting': 1,
          'version': 1,
          'voxel_limit': 0.135,
         },
        'representation': 'surface',
        'session_volume_id': "M$F![\r!\x0cIV\r5W#j!`9]Zev'xY,8A&^X\n",
        'solid_brightness_factor': 1.0,
        'solid_colors': [
          ( 0.7, 1, 1, 1, ),
          ( 0.7, 1, 1, 1, ),
         ],
        'solid_levels': [
          ( 0.0, 0, ),
          ( 0.02206098474562168, 1, ),
         ],
        'solid_model': None,
        'surface_brightness_factor': 1.0,
        'surface_colors': [
          ( 0.8518518518518519, 0.037037037037037035, 0.0, 1.0, ),
         ],
        'surface_levels': [ 0.017402780857184684, ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( 0.0, 0.0, -1.0, ),
          'clip_plane_origin': ( 0.0, 0.0, 0.0, ),
          'clip_thickness': 5.0,
          'display': True,
          'id': 3,
          'name': u'SEA_complex_SEA4.mrc',
          'osl_identifier': u'#3',
          'silhouette': True,
          'subid': 0,
          'use_clip_plane': False,
          'use_clip_thickness': False,
          'version': 5,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 85.73205662677236,
            'rotation_axis': ( -0.5492039978818357, 0.611441099003517, 0.5696619621845749, ),
            'translation': ( -264.72219474443557, -786.5882321529023, -487.26238546005493, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.86,
        'transparency_factor': 0.0,
        'version': 6,
       },
      ],
     ),
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90.0, 90.0, 90.0, ),
       'class': 'Data_State',
       'file_type': 'mrc',
       'grid_id': '',
       'name': u'SEA_complex_Npr3.mrc',
       'path': u'SEA_complex_Npr3.mrc',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 0.7, 1, 0.7, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 49, 54, 50, ),
          [ 1, 1, 1, ],
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 2,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 74, 72, 74, ),
            ),
            (
             ( 0, 0, 0, ),
             ( 50, 49, 48, ),
            ),
            (
             ( 0, 0, 0, ),
             ( 49, 54, 50, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'box_faces': False,
          'bt_correction': 0,
          'cap_faces': 1,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': 1,
          'dim_transparent_voxels': 1,
          'flip_normals': 0,
          'limit_voxel_count': 1,
          'line_thickness': 1.0,
          'linear_interpolation': 1,
          'maximum_intensity_projection': 0,
          'mesh_lighting': 1,
          'minimal_texture_memory': 0,
          'orthoplane_positions': ( 0, 0, 0, ),
          'orthoplanes_shown': ( False, False, False, ),
          'outline_box_linewidth': 1.0,
          'outline_box_rgb': ( 1.0, 1.0, 1.0, ),
          'projection_mode': 'auto',
          'show_outline_box': 0,
          'smooth_lines': 0,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': 1,
          'subdivide_surface': 0,
          'subdivision_levels': 1,
          'surface_smoothing': 0,
          'two_sided_lighting': 1,
          'version': 1,
          'voxel_limit': 0.135,
         },
        'representation': 'surface',
        'session_volume_id': '*r3\tRs\tURZ;_EGetG;,twD?!S1ke&\nq1',
        'solid_brightness_factor': 1.0,
        'solid_colors': [
          ( 0.7, 1, 0.7, 1, ),
          ( 0.7, 1, 0.7, 1, ),
          ( 0.7, 1, 0.7, 1, ),
         ],
        'solid_levels': [
          ( 0.0, 0, ),
          ( 0.00031498220935463904, 0.99, ),
          ( 0.011412398889660835, 1, ),
         ],
        'solid_model': None,
        'surface_brightness_factor': 1.0,
        'surface_colors': [
          ( 1.0, 0.2222222222222222, 0.6296296296296297, 1.0, ),
         ],
        'surface_levels': [ 0.01065169614140351, ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( 0.0, 0.0, -1.0, ),
          'clip_plane_origin': ( 0.0, 0.0, 0.0, ),
          'clip_thickness': 5.0,
          'display': True,
          'id': 7,
          'name': u'SEA_complex_Npr3.mrc',
          'osl_identifier': u'#7',
          'silhouette': True,
          'subid': 0,
          'use_clip_plane': False,
          'use_clip_thickness': False,
          'version': 5,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 85.73205662677236,
            'rotation_axis': ( -0.5492039978818357, 0.611441099003517, 0.5696619621845749, ),
            'translation': ( -264.72219474443557, -786.5882321529023, -487.26238546005493, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.5,
        'transparency_factor': 0.0,
        'version': 6,
       },
      ],
     ),
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90.0, 90.0, 90.0, ),
       'class': 'Data_State',
       'file_type': 'mrc',
       'grid_id': '',
       'name': u'SEA_complex_SEA1.mrc',
       'path': u'SEA_complex_SEA1.mrc',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 1, 0.7, 0.7, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 49, 54, 50, ),
          [ 1, 1, 1, ],
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 2,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 74, 72, 74, ),
            ),
            (
             ( 0, 0, 0, ),
             ( 50, 49, 48, ),
            ),
            (
             ( 0, 0, 0, ),
             ( 49, 54, 50, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'box_faces': False,
          'bt_correction': 0,
          'cap_faces': 1,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': 1,
          'dim_transparent_voxels': 1,
          'flip_normals': 0,
          'limit_voxel_count': 1,
          'line_thickness': 1.0,
          'linear_interpolation': 1,
          'maximum_intensity_projection': 0,
          'mesh_lighting': 1,
          'minimal_texture_memory': 0,
          'orthoplane_positions': ( 0, 0, 0, ),
          'orthoplanes_shown': ( False, False, False, ),
          'outline_box_linewidth': 1.0,
          'outline_box_rgb': ( 1.0, 1.0, 1.0, ),
          'projection_mode': 'auto',
          'show_outline_box': 0,
          'smooth_lines': 0,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': 1,
          'subdivide_surface': 0,
          'subdivision_levels': 1,
          'surface_smoothing': 0,
          'two_sided_lighting': 1,
          'version': 1,
          'voxel_limit': 0.135,
         },
        'representation': 'surface',
        'session_volume_id': 'la7e,L9o.(Nn0r\x0cI\r]lB4mzD*=,BI )t',
        'solid_brightness_factor': 1.0,
        'solid_colors': [
          ( 1, 0.7, 0.7, 1, ),
          ( 1, 0.7, 0.7, 1, ),
          ( 1, 0.7, 0.7, 1, ),
         ],
        'solid_levels': [
          ( 0.0, 0, ),
          ( 0.0005389756741002202, 0.99, ),
          ( 0.0062453728169202805, 1, ),
         ],
        'solid_model': None,
        'surface_brightness_factor': 1.0,
        'surface_colors': [
          ( 0.25925925925925924, 0.8518518518518519, 0.2222222222222222, 1.0, ),
         ],
        'surface_levels': [ 0.012772026173212665, ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( 0.0, 0.0, -1.0, ),
          'clip_plane_origin': ( 0.0, 0.0, 0.0, ),
          'clip_thickness': 5.0,
          'display': True,
          'id': 6,
          'name': u'SEA_complex_SEA1.mrc',
          'osl_identifier': u'#6',
          'silhouette': True,
          'subid': 0,
          'use_clip_plane': False,
          'use_clip_thickness': False,
          'version': 5,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 85.73205662677236,
            'rotation_axis': ( -0.5492039978818357, 0.611441099003517, 0.5696619621845749, ),
            'translation': ( -264.72219474443557, -786.5882321529023, -487.26238546005493, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.5,
        'transparency_factor': 0.2,
        'version': 6,
       },
      ],
     ),
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90.0, 90.0, 90.0, ),
       'class': 'Data_State',
       'file_type': 'mrc',
       'grid_id': '',
       'name': u'SEA_complex_SEA2.mrc',
       'path': u'SEA_complex_SEA2.mrc',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 1, 0.7, 1, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 49, 54, 50, ),
          [ 1, 1, 1, ],
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 2,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 74, 72, 74, ),
            ),
            (
             ( 0, 0, 0, ),
             ( 50, 49, 48, ),
            ),
            (
             ( 0, 0, 0, ),
             ( 49, 54, 50, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'box_faces': False,
          'bt_correction': 0,
          'cap_faces': 1,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': 1,
          'dim_transparent_voxels': 1,
          'flip_normals': 0,
          'limit_voxel_count': 1,
          'line_thickness': 1.0,
          'linear_interpolation': 1,
          'maximum_intensity_projection': 0,
          'mesh_lighting': 1,
          'minimal_texture_memory': 0,
          'orthoplane_positions': ( 0, 0, 0, ),
          'orthoplanes_shown': ( False, False, False, ),
          'outline_box_linewidth': 1.0,
          'outline_box_rgb': ( 1.0, 1.0, 1.0, ),
          'projection_mode': 'auto',
          'show_outline_box': 0,
          'smooth_lines': 0,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': 1,
          'subdivide_surface': 0,
          'subdivision_levels': 1,
          'surface_smoothing': 0,
          'two_sided_lighting': 1,
          'version': 1,
          'voxel_limit': 0.135,
         },
        'representation': 'surface',
        'session_volume_id': '&AqOFtZ=(\n\\u~O2zBm1^cIYY|-9Ildm\x0b',
        'solid_brightness_factor': 1.0,
        'solid_colors': [
          ( 1, 0.7, 1, 1, ),
          ( 1, 0.7, 1, 1, ),
          ( 1, 0.7, 1, 1, ),
         ],
        'solid_levels': [
          ( 0.0, 0, ),
          ( 0.00013374977465718986, 0.99, ),
          ( 0.021926192566752434, 1, ),
         ],
        'solid_model': None,
        'surface_brightness_factor': 1.0,
        'surface_colors': [
          ( 0.5185185185185185, 0.5925925925925926, 0.07407407407407407, 1.0, ),
         ],
        'surface_levels': [ 0.009539104592387049, ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( 0.0, 0.0, -1.0, ),
          'clip_plane_origin': ( 0.0, 0.0, 0.0, ),
          'clip_thickness': 5.0,
          'display': True,
          'id': 5,
          'name': u'SEA_complex_SEA2.mrc',
          'osl_identifier': u'#5',
          'silhouette': True,
          'subid': 0,
          'use_clip_plane': False,
          'use_clip_thickness': False,
          'version': 5,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 85.73205662677236,
            'rotation_axis': ( -0.5492039978818357, 0.611441099003517, 0.5696619621845749, ),
            'translation': ( -264.72219474443557, -786.5882321529023, -487.26238546005493, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.5,
        'transparency_factor': 0.2,
        'version': 6,
       },
      ],
     ),
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90.0, 90.0, 90.0, ),
       'class': 'Data_State',
       'file_type': 'mrc',
       'grid_id': '',
       'name': u'SEA_complex_Seh1.mrc',
       'path': u'SEA_complex_Seh1.mrc',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 1, 1, 0.7, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 49, 54, 50, ),
          [ 1, 1, 1, ],
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 2,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 74, 72, 74, ),
            ),
            (
             ( 0, 0, 0, ),
             ( 50, 49, 48, ),
            ),
            (
             ( 0, 0, 0, ),
             ( 49, 54, 50, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'box_faces': False,
          'bt_correction': 0,
          'cap_faces': 1,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': 1,
          'dim_transparent_voxels': 1,
          'flip_normals': 0,
          'limit_voxel_count': 1,
          'line_thickness': 1.0,
          'linear_interpolation': 1,
          'maximum_intensity_projection': 0,
          'mesh_lighting': 1,
          'minimal_texture_memory': 0,
          'orthoplane_positions': ( 0, 0, 0, ),
          'orthoplanes_shown': ( False, False, False, ),
          'outline_box_linewidth': 1.0,
          'outline_box_rgb': ( 1.0, 1.0, 1.0, ),
          'projection_mode': 'auto',
          'show_outline_box': 0,
          'smooth_lines': 0,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': 1,
          'subdivide_surface': 0,
          'subdivision_levels': 1,
          'surface_smoothing': 0,
          'two_sided_lighting': 1,
          'version': 1,
          'voxel_limit': 0.135,
         },
        'representation': 'surface',
        'session_volume_id': '[ZK$oo&bA\x0c4T94niyOf],9DkwT-Z,/Mr',
        'solid_brightness_factor': 1.0,
        'solid_colors': [
          ( 1, 1, 0.7, 1, ),
          ( 1, 1, 0.7, 1, ),
         ],
        'solid_levels': [
          ( 0.0, 0, ),
          ( 0.019140472635626793, 1, ),
         ],
        'solid_model': None,
        'surface_brightness_factor': 1.0,
        'surface_colors': [
          ( 0.0, 0.9090909090909091, 0.45454545454545453, 1.0, ),
         ],
        'surface_levels': [ 0.02707353906536457, ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( 0.0, 0.0, -1.0, ),
          'clip_plane_origin': ( 0.0, 0.0, 0.0, ),
          'clip_thickness': 5.0,
          'display': True,
          'id': 2,
          'name': u'SEA_complex_Seh1.mrc',
          'osl_identifier': u'#2',
          'silhouette': True,
          'subid': 0,
          'use_clip_plane': False,
          'use_clip_thickness': False,
          'version': 5,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 85.73205662677236,
            'rotation_axis': ( -0.5492039978818357, 0.611441099003517, 0.5696619621845749, ),
            'translation': ( -264.72219474443557, -786.5882321529023, -487.26238546005493, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.5,
        'transparency_factor': 0.0,
        'version': 6,
       },
      ],
     ),
    ],
   'version': 2,
  }
 from VolumeViewer import session
 session.restore_volume_data_state(volume_data_state)

try:
  restore_volume_data()
except:
  reportRestoreError('Error restoring volume data')


def restore_volume_dialog():
 volume_dialog_state = \
  {
   'adjust_camera': 0,
   'auto_show_subregion': 0,
   'box_padding': '0',
   'class': 'Volume_Dialog_State',
   'data_cache_size': '512',
   'focus_volume': '&AqOFtZ=(\n\\u~O2zBm1^cIYY|-9Ildm\x0b',
   'geometry': u'420x741+1032+22',
   'histogram_active_order': [ 0, 1, 2, ],
   'histogram_volumes': [ '&AqOFtZ=(\n\\u~O2zBm1^cIYY|-9Ildm\x0b', '~.0F08\x0beaC}i4+\x0b/*QT$Q[AkO4\x0czas%h', '*r3\tRs\tURZ;_EGetG;,twD?!S1ke&\nq1', ],
   'immediate_update': 1,
   'initial_colors': (
     ( 0.7, 0.7, 0.7, 1, ),
     ( 1, 1, 0.7, 1, ),
     ( 0.7, 1, 1, 1, ),
     ( 0.7, 0.7, 1, 1, ),
     ( 1, 0.7, 1, 1, ),
     ( 1, 0.7, 0.7, 1, ),
     ( 0.7, 1, 0.7, 1, ),
     ( 0.9, 0.75, 0.6, 1, ),
     ( 0.6, 0.75, 0.9, 1, ),
     ( 0.8, 0.8, 0.6, 1, ),
    ),
   'is_visible': True,
   'max_histograms': '3',
   'representation': 'surface',
   'selectable_subregions': 0,
   'show_on_open': 1,
   'show_plane': 1,
   'shown_panels': [
     'Data set list',
     'Threshold and Color',
     'Brightness and Transparency',
     'Display style',
     'Subregion selection',
    ],
   'subregion_button': 'middle',
   'use_initial_colors': 1,
   'version': 12,
   'voxel_limit_for_open': '256',
   'voxel_limit_for_plane': '256',
   'zone_radius': 2.0,
  }
 from VolumeViewer import session
 session.restore_volume_dialog_state(volume_dialog_state)

try:
  restore_volume_dialog()
except:
  reportRestoreError('Error restoring volume dialog')


def restore_scale_bar():
 scale_bar_state = \
  {
   'bar_length': '400',
   'bar_rgba': ( 1, 1, 1, 1.0, ),
   'bar_thickness': '1',
   'class': 'Scale_Bar_Dialog_State',
   'frozen_models': [ ],
   'geometry': u'293x196+48+374',
   'is_visible': True,
   'label_rgba': ( 1, 1, 1, 1.0, ),
   'label_text': u'# \xc5',
   'label_x_offset': '',
   'label_y_offset': '',
   'model': None,
   'move_scalebar': 0,
   'orientation': 'vertical',
   'preserve_position': 1,
   'screen_x_position': '-0.4',
   'screen_y_position': '0.0022',
   'show_scalebar': 0,
   'version': 1,
  }
 import ScaleBar.session
 ScaleBar.session.restore_scale_bar_state(scale_bar_state)

try:
  restore_scale_bar()
except:
  reportRestoreError('Error restoring scale bar')


def restoreRemainder():
	from SimpleSession.versions.v61 import restoreWindowSize, \
	     restoreOpenStates, restoreSelections, restoreFontInfo, \
	     restoreOpenModelsAttrs, restoreModelClip, restoreSilhouettes

	curSelIds =  []
	savedSels = []
	openModelsAttrs = { 'cofrMethod': 4 }
	windowSize = (991, 757)
	xformMap = {0: (((-0.49605044487209, 0.5964755744567, 0.63099195337085), 96.196051173132), (-243.30699220657, -781.26616653829, -497.41427630072), True)}
	fontInfo = {'face': ('Sans Serif', 'Normal', 16)}
	clipPlaneInfo = {}
	silhouettes = {0: True, 381: True}

	replyobj.status("Restoring window...", blankAfter=0,
		secondary=True)
	restoreWindowSize(windowSize)
	replyobj.status("Restoring open states...", blankAfter=0,
		secondary=True)
	restoreOpenStates(xformMap)
	replyobj.status("Restoring font info...", blankAfter=0,
		secondary=True)
	restoreFontInfo(fontInfo)
	replyobj.status("Restoring selections...", blankAfter=0,
		secondary=True)
	restoreSelections(curSelIds, savedSels)
	replyobj.status("Restoring openModel attributes...", blankAfter=0,
		secondary=True)
	restoreOpenModelsAttrs(openModelsAttrs)
	replyobj.status("Restoring model clipping...", blankAfter=0,
		secondary=True)
	restoreModelClip(clipPlaneInfo)
	replyobj.status("Restoring per-model silhouettes...", blankAfter=0,
		secondary=True)
	restoreSilhouettes(silhouettes)

	replyobj.status("Restoring remaining extension info...", blankAfter=0,
		secondary=True)
try:
	restoreRemainder()
except:
	reportRestoreError("Error restoring post-model state")
from SimpleSession.versions.v61 import makeAfterModelsCBs
makeAfterModelsCBs()

from SimpleSession.versions.v61 import endRestore
replyobj.status('Finishing restore...', blankAfter=0, secondary=True)
endRestore({})
replyobj.status('', secondary=True)
replyobj.status('Restore finished.')

