from framework import Argument as A
from framework import Defintion as D
from framework import Example as E
from framework import Reference as R

root_claim = "Trust and Generosity are necessary for Cooperation"


trust_is_necessary = A("Subagents comprising a single agent must trust each other or they will waste energy conflicting", [
        A("This is true in human agents, both individuals and collectives"),
        A("This is true even in software agents", [
          A("A hierarchy can resolve some of these issues, at the cost of evolvability", [
            A("If the root has too much logic in it, it cannot safely evolve without risk of dying")
            ])
         ]),
      ])

deception_and_defection_kill_trust =  A("Agents that practice deception and defection will not be able to maintain trust among their self-aware subagents", [
        A("Agents that can model and learn from their environment will model and attempt to learn which agents are defecting against them."),
        A("Self-aware subagents will make use of these same facilities."),
       ])


trust_is_necessary =  A(
    root_claim, [
      trust_is_necessary,
      deception_and_defection_kill_trust
      
 ])


