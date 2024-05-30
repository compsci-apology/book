from framework import Argument as A
from framework import Defintion as D
from framework import Example as E
from framework import Reference as R

root_claim = "Sacricfice is Necessary To Escape Local Minima"

sacrifice_is_necessary =  A(
    root_claim, [
      D("Sacrifice means voluntarily making things worse now, in order for a chance of them improving later"),
      A("Any agent which cannot sacrifice will get stuck in local maxima of its utility function"),  #  is this always true? need to determine
     A("An agent's capacity to sacrifice acts as a lowerbound on the size of local maxima which can trap it", [ 
        A("Only agents willing to make arbitrarily large sacrifices can avoid being trapped in local maxima"),  #  is this always true? need to determine

    ])
   ]
 )


