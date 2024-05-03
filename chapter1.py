from framework import Argument as A


root = "Belief systems are strategies that organisms use to survive and thrive."

A("Changing environments require changing beliefs, just like changing business requirements drives changes in software systems.")

value_systems =  A("Belief systems, Software Systems, and DNA are all value systems.", [
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

abstract_model = A("All value systems share traits in common which can be understood with an abstract model.",  [
      A("We can consider all of these a being robots controlled by belief systems.", [
        A("navigating high dimensional spaces using sense organs to get information about their environemnt"),
        A("integrated by concept-networks to drive actuators."),
      ]),
      A("This model will allow us to understand the common problems that all of these diverse systems have to solve", [
        A("they must model their environment"), 
        A("they must navigate away from threats"),
        A("the must navigate towards opportunities."),
      ]),
      A("Another advantage of this generic model is that we can remember that these robots always exist in the physical universe.", [ 
        A("All robots need to solve the problem of reliably obtaining enough energy to keep themselves alive."),
        A("They will always be under selective pressure to be more energetically efficient."),
       ]),
       A("Note that physical laws themselves consistute a value system (according to the above defintion).", [
        A("Physical laws constrain the space of possible outcomes into specific actualities.", [
          A("Out of all the possible tracetories a ball could follow when tossed in the air, it will tend to closely approximate a parabola."),
          ])
        ]),
      A("with this framework in mind, we can then model the evolution of strategies as consisting of an evolutinoary approxmation of the laws of physics", [
        A("only those which are relevant within the niche of the given organism"),
        A("plus the additional assumption of 'i exist and will continue to participate in the future.'"),
      ])
    ])

strategies_evolve = A(root, [
    A("Software systems and belief systems are both encoded survival + growth strategies.", [
        A("belief systems tell a person how to act in a given context"),
        A("software systems tell a microprocessor how to act in a given context.")
    ]),
    value_systems,
    abstract_model,
    A("some organisms - those that live in specific, static niches - do not need to change much over time in order to survive."),
    A("other organisms operate in dynamic niches that change over time, which requires them to evolve their belief systems in order to survive."),
    A("Evolving a belief system means changing beliefs, i.e. learning and unlearning concepts."),
    A("It is difficult to get these changes right."),
    A("Failing to change, or changing in the wrong way, both mean death.")
    ])


