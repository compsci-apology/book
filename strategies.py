from framework import Argument as A
from framework import Example as E


root = "Belief systems are strategies used by organisms"


beliefs_are_strategies = A("Software systems and belief systems are both encoded strategies.", [
        E("belief systems tell a person (or group thereof) how to act in a given context"),
        E("software systems tell a microprocessor how to act in a given context."),
    ])

model_robots = A("All organisms and their strategies share traits in common which can be understood with an abstract model.",  [
      A("We can consider all of these as being robots, with 'bodies' controlled by software.", [
        A("organisms have bodies, i.e. physical structures with mechanical degrees of freedom"),
        A("these bodies navigate spaces", [
          A("the basic 3d space navigated by animals and human beings"),
          A("but also higher-dimensional spaces of things like absrtract tradeoffs", [
            A("A business navigates the space of possible markets to participate in"),
            A("what 'sort of messaging should we send'"),
            A("where should we invest our capital this year?"),
            A("what kind of employees should we hire?"),
           ])
        ]),
        A("organisms sense organs to get information about their environemnt (input)", [
          E("Sense organs like eyes, ears, etc"),
          E("Telescopes, microscopes, cameras"),
          E("Sensor networks, like windmills or social media networks"),
        ]),
        A("integrated by concept-networks (processing)", [
          A("This includes human beings looking at information and making decisions")
          ]),
        A("controlling actuators by constraining their degress of freedom  (output)", [
          A("Muscles move bones by contracting, i.e. adding tension that reduces degrees of freedom"),
          A("A thermostat species whether the furance or a/c system should be on or off"),
          A("A engineering department specifies which priorties they will invest in this quarter"),
        ]),
      ]),
      A("This model will allow us to understand the **common computational problems that all of these organisms must solve**", [
        A("they must model their enviornment and their relationship to it"), 
        A("they must navigate away from threats"),
        A("the must navigate towards opportunities."),
      ]),
      A("Another advantage of this generic model is that we can remember that these robots always exist in the physical universe.", [ 
        A("All robots need to solve the problem of reliably obtaining enough energy to keep themselves alive."),
        A("They will always be under selective pressure to be more energetically efficient."),
        A("This means they must evaluate _tradeoffs_ because energy spent in one area cannot be spent elsewhere"),
       ]),
    ])


# is this the place to add in turing completeness?

# say later
physics_is_a_value_system = A("Note that physical laws themselves consistute a value system (according to the above defintion).", [
      A("Physical laws constrain the space of possible outcomes into specific actualities.",  [
        A("Out of all the possible tracetories a ball could follow when tossed in the air, it will tend to closely approximate a parabola.") ]
      ),
      A("with this framework in, we can then model the evolution of strategies as consisting of an evolutinoary approxmation of the laws of physics", [
        A("only those which are relevant within the niche of the given organism"),
        A("plus the additional assumption of 'i exist and will continue to participate in the future.'"),
      ]),
      A("Thinking this way is _useful_.", [
        A("Defining values systems as 'thigns that constrain possibility' allow us to see common patterns that might otherwise be invisible?"),
        A("But is the question true? Materialism says truth only exists if it generates predictions"),
      ])
    ])


# say later
model_values =  A("The fact/value distinction is more useful as a spectrum", [
   A("Values are used to make choices."),
   A("Values are constraints on possibility space.", [
       A("Whenever a space of possibilities is constrained to some specific outcome, we can say that some value is in operation."),
       A("It is useful to understand the similarites between all such cases, even those that do not traditionally seem like 'values.'"),
     ]),
    A("The fact/value distinction is not binary, but rather of a continuum.", [
      A("This dinstionction  would be better understood as 'concrete vs abstract'"),
      A("all fact claims containing implicit values, and all value claims implying certain facts.")
      ]),
     A("The fact / value distinction is similar to the data vs code distinction in software", [
      A("This distinction s a natural consequence of evolutionary pressure.", [
        A("Representing our values as learnable, updatable beliefs allows for faster, cheaper evolution of software systems.")
        ])
      ]),
])

strategies_evolve = A("Some strategies can themselves evolve", [
    A("some organisms - those that live in specific, static niches - do not need to change much over time in order to survive."),
    A("other organisms operate in **dynamic niches**  (i.e., niches that change over time), which **requires them to evolve their strategies** in order to survive."),
    A("Evolving a belief system means changing beliefs, i.e. learning and unlearning concepts."),
    A("It is difficult to get these changes right.", [
      A("Failing to change means death because the environment changes in ways that break your strategy"),
      A("Changing the wrong way means breaking your strategy's alignment with the current environment"),
    ]),
    A("**Not all strategies are equally capable of evolving, for computational reasons.**")
  ])


strategies_evolve = A(root, [
    beliefs_are_strategies,
    model_robots,
    strategies_evolve
   ])


