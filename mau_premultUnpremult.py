#--------------------------------------------------
# mau_premultUnpremult.py
# version: 1.0.0
# last updated: 27.03.21
#--------------------------------------------------

import nuke

def premultUnpremult():
	for i in nuke.selectedNodes():
	    try:
	        if i.knob("unpremult").value() == "alpha":
	            i.knob("unpremult").setValue("none")
	        else:
	            i.knob("unpremult").setValue("alpha")
	    except:
	        pass
