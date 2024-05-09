from framework import Argument as A
from framework import Defintion as D
from framework import Example as E

root = "Software Evolves Faster Than Hardware"


evolution_requires_energy = A("Evolution requires energetic investment", [
  E("Changing a house to improve some experience requires labor and materials"),
  E("Releasing a new product to market requires investment"),
  E("Developers take time to write, compile and test code"),
  E("Performing a release takes time and attention"),
])

abstractions_are_lossy_compressions = D("An abstraction of a system is a lossy compression of that system", 
    [ D("Abstractions, by considering only some information relevant, constrain the space of possible features that could be considered"),
      D("Thus, **abstractions are values**."),
    ])

abstractions_are_cheaper = A("Changing an abstraction is cheaper", [
  E("The ENIAC was changed to use a stored program model of execution to reduce cycle cost", [
    E("Moving the cables around between programs was expensive and costly"),
    E("Changing which program was stored in memory was cheaper"),
    E("Fixing the cables in place made the machine slower to operate, but faster to evolve"),
  ]),
  E("Changing a blueprint is easier and cheaper than building a prototype"),
  E("Building a prototype from a blueprint is cheaper than performing the construction"),
  E("Describing a set of features is easier and cheaper than implementing those features"),
])

abstractions_add_risk = A("Using abstractions adds a new risk category", [
  A("Evolving an abstraction in a way that improves its fitness might not map onto a base-layer change that _also_ improves fitness"),
])

abstraction_mechanisms_can_evolve = A("Abstraction functions can _also_ evolve", [
  A("Because abstraction has a cost and risk, abstraction functions themselves can evolve", [
    E("An architect might shift to a new style of blueprints which is faster to make and change"),
    E("The 'annual spring reorg' at Google"),
    E("Software engineers might refactor code to produce the same results in a way that's eaiser to change in the future"),
  ]),
])




software_evolves_faster = A(
  root,  [
    evolution_requires_energy,
    abstractions_are_lossy_compressions,
    abstractions_are_cheaper,
    abstractions_add_risk,
    abstraction_mechanisms_can_evolve
  ]
)

