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

abstractions_are_one_way_functions = D("An abstraction is a many-to-one function that maps a larger 'object' domain onto a smaller 'symbol' domain", 
    [ D("When 'abstracting' an object, information about the object is 'thrown out' to produce a symbol"),
      D("Abstractions can be chained; symbols themselves can be abstracted further"),
      D("Abstractions can be also be incarnated: a symbol can be used to select transformations of the object domain such that the object domain now maps to the symbol", [
        E("A blueprint can be used to build a house"),
        E("A textual description of a computer program can be turned into source code"),
        E("An image or a feeling can be used to guide the creation of a song or painting"),
       ]),
      #  D("Thus, **abstractions are values**."), - this doesn't need to go here yet, but it needs to be said at some point
    ])

loss_functions_are_scores = D("A loss function maps symbols to numerical scores.")

abstractions_evolve = D("Organisms can use abstraction to evolve faster", [
  abstractions_are_one_way_functions,
  loss_functions_are_scores,
  D("An organism evolves by computing multiple abstractions of itself, computing the loss function on them, and incarnating the lowest scoring one")
])

# an abstraction is a many-to-one-function that maps a larger 'object' domain onto a smaller 'symbol' domain
# the abstraction function

abstractions_are_cheaper = A("Evolving an abstraction is cheaper", [
  abstractions_evolve,
  evolution_requires_energy,
  A("The cost of change is ultimately an energetic cost. Work must be done on a system to change it."),
  A("**Changing an abstraction of an object is cheaper than changing the object itself** because less mass needs to move", [
     E("The ENIAC was changed to use a stored program model of execution to reduce cycle cost", [
       E("Moving the cables around between programs was expensive and costly"),
       E("Changing which program was stored in memory was cheaper"),
       E("Fixing the cables in place made the machine slower to operate, but faster to evolve"),
     ]),
     E("Changing a blueprint is easier and cheaper than building a prototype"),
     E("Building a prototype from a blueprint is cheaper than performing the construction"),
     E("Describing a set of features is easier and cheaper than implementing those features"),

    ]),
  ])

abstractions_add_risk = A("Using abstractions adds a new risk category", [
  A("The fitness of an organism is determined over long periods of time by the environment itself"),
  A("The fitness of a symbol is determined by the loss function"),
  A("The loss function itself is an abstraction of 'the true loss function' of the environment", [
    E("A program which fails to compile cannot make the business money"),
    E("A program which fails unit tests will likely not reliably make the business money, even if it's faster"),
    E("A program which passes all the unit tests, and performs some critical functions faster, in a domain where speed is rewarded, is more likely to make the business money"),
  ]),
  A("Modifying a symbol in a way that reduces its computed loss might not incarnate an object whose _actual_ loss is lower.", [
    E("Releasing a software change is always risky even if it tests well"),
    E("A new marketing campaign might fail even if it did well in focus groups"),
    E("A strategy that performed well in simulated combat might not do well in actual battle"),
  ]),
  A("Short term performance and even historical performance, are abstractions of expected future performance", [
    E("A strategy that has worked well in the past, might have depended on transient environmental conditions")
  ])
 ])

# this is a whole other chapter!
A("Using an abstraction requires trust in that abstraction", [
    E("An object which is itself an abstracted symbol, and contains a representation of itself, can contain a representation of the abstractions operating on it")
  ])

abstraction_mechanisms_can_evolve = A("Abstraction functions can _also_ evolve", [
  A("Because using abstraction has a cost and risk, abstraction functions themselves can evolve", [
    E("An architect might shift to a new style of blueprints which is faster to make and change"),
    E("The 'annual spring reorg' at Google"),
    E("Software engineers might refactor code to produce the same results in a way that's eaiser to change in the future"),
    E("Loss functions - because they are abstractions of the true environmental loss function - can evolve too", [
      E("A business might develop new key performance indicators that it uses to determine the performance of its strategies")
    ]),
  ]),
])




software_evolves_faster = A(
  root,  [
    abstractions_evolve,
    abstractions_are_cheaper,
    abstractions_add_risk,
    abstraction_mechanisms_can_evolve
  ]
)

