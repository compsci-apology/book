from framework import Argument as A
from framework import Defintion as D
from framework import Example as E
from framework import Reference as R

root_claim = "Absent the correct hierarchy, internal conflict will lead to disintegration"

# todo: should probably talk about recursively composed agents make the most sense as an architecture
# beceause you need some way of comparing lots of separate potential plans for action
# each plan itself has to pursue some subgoal 
# now these subagents themselves can also evolve, the recursion lets this go on arbitrarily...

absent_hierarchy_conflict_disintegrates =  A(
    root_claim, [
      A("The computation done by any complex agent must be spatially distributed", [
        A("Processes can only handle so much bandwidth, due to physical limits"),
        A("When lower-latency resposne times are required, agents using centralize processing will be outcompeted by agents with more local decisionmaking "),
      ]),
      A("Distributed computing of motion plans for an agent inevitably leads to internal conflict between proposed motion plans", [
        A("Any given agent still only has a single body with a limited energy budget"),
      ]),
    ]
  )


