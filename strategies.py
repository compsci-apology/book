from framework import Argument as A
from framework import Defintion as D
from framework import Example as E
from framework import Reference as R


root = "Belief systems are strategies used by organisms"


beliefs_are_strategies = A("Software systems and belief systems are both encoded strategies.", [
       D("A strategy is a **computational process** performed by an agent in an environnment", [
         A("Both evolution of species and learning within an organism must be understood as computational processes", [
            D("The term 'ecorithm' describes an algorithm operating in an environment"),
            R("Probably Approximately Correct, Leslie Valiant"),
         ]),
         A("We can use the concept of strategy to extend the concept of an ecorithm to other 'organisms' like businesses and governments ")
      ]),
 ])



# interesting but not essential now
agency_spectrum = D("Any flow of information which matches this shape could therefore be considered an agent executing a strategy", [
        A("But this is all computational processes!"),
        A("The agent/not-agent distinction might be more of a spectrum than a binary"),
        A("We argue that **any computational process** is somewhat agentic"),
        A("The agency of a computational process depends on its computational structure", [
          A("Computational resources constrain agency.", [
            E("Time in which to compute"),
            E("Space to use as working memory"),
            E("Randomness is a computational resource, access to randomness constrains some algorithms"),
           ]),
          A("Access to energy constrains agency"),
          A("Access to information constrains agency"),
         ]), 
        ]
      )
model_robots = A("All organisms and their strategies share traits in common which can be understood with an abstract model.",  [
      A("Individual human beings, businesses, and governments all have to solve similar computational problems", [
        A("they must model their enviornment and their relationship to it"), 
        A("they must navigate away from threats"),
        A("the must navigate towards opportunities."),
      ]),
      A("Game theoreticians talk about convergent instrumental subgoals; there appear to be **convergent instrumental implementation details**", [
        R("Optimal Policies Tend to Seek Power, by Turner et alii",[ 
          A("This work does not consider'partially observable environments' and 'suboptimal policies'")
         ]),
        R("Formalizing convergent instrumental goals Benson-Tilson and Soares", 
          url="https://intelligence.org/files/FormalizingConvergentGoals.pdf",
          supports=[
          A("This works assumes an environment that is neither choatic, nor subject to entropic decay, and which can be observed with perfect information")
        ]),
        A("This thesis argues that **there are numerous convergent instrumental implentation details for sufficiently advanced strategies**"),
        A("And that **these implementation details** line up with strategies articulated in numerous wisdom traditions"),
        ]
        ),
      A("We can consider all agents as being robots, with 'bodies' controlled by software strategies.", [
        D("organisms have bodies, i.e. physical structures with mechanical degrees of freedom"),
        D("these bodies navigate spaces", [
          E("the basic 3d space navigated by animals and human beings"),
          E("but also higher-dimensional spaces of things like absrtract tradeoffs", [
            E("A business navigates the space of possible markets to participate in"),
            E("what sort of messaging should we send?"),
            E("where should we invest our capital this year?"),
            E("what kind of employees should we hire?"),
           ])
        ]),
        D("using **computational models of meaning**", [
          D("A model of meaning is agorithm for computing a heading in a context", [
            E("i.e., a desired navigation vector in an abstract space"),
            E("The OODA Loop describes a computational processes", [
              R("John Boyd, 'The Essence of Winning and Losing'"),
              D("Observe: input (gather sense data from the environment)"),
              D("Orient: map sense data to a conceptual model of possible actions"),
              D("Decide: reduce the map of possible actions to one best action"),
              D("Act: output (perform the best action)"),
            ]),
            A("sense organs collect information about their environment (input)", [
              E("Sense organs like eyes, ears, etc"),
              E("Telescopes, microscopes, cameras"),
              E("Sensor networks, like windmills or social media networks"),
            ]),
            A("input is integrated by concept-networks (processing)", [
              A("This includes human beings looking at information and making decisions")
              ]),
            A("controlling actuators by constraining their degress of freedom  (output)", [
              A("Muscles move bones by contracting, i.e. adding tension that reduces degrees of freedom"),
              A("A thermostat specifies whether the furance or a/c system should be on or off"),
              A("A engineering department specifies which priorties they will invest in this quarter"),
             # D("**Meaning is a vector in configuration space**", [ # i don't think we are ready for this yet
             #   E("an input to an actuator telling it how to operate"),
             #   E("A 'compass' saying which way to go, either in a concerete situation, or in the space of an abstraction")
             # ]),
            ]),
          ])
       ])
      ]),
      A("This model will allow us to understand the **common computational problems that all of these organisms must solve**"),
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
   D("Values are constraints on possibility space.", [
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
    A("some organisms - those that live in specific, static niches - do not need to change much over time in order to survive.", [
      E("This includes most animals"), # is this actually true or would it be better to describe niches in terms of how frequently they change?
      E("This includes human beings pre sedentary shift, in periods of long-term static culture")
     ]),
    A("other organisms operate in **dynamic niches**  (i.e., niches that change over time), which **requires them to evolve their strategies** in order to survive.", [
      E("businesses in competitive industries"),
      E("human beings in dynamic situations"),
      E("political structures in times of change"),
    ]),
    A("Evolving a belief system means changing beliefs, i.e. learning and unlearning concepts."),
    A("It is difficult to get these changes right.", [
      A("Failing to change means death because the environment changes in ways that break your strategy"),
      A("Changing the wrong way means breaking your strategy's alignment with the current environment"),
    ]),
    A("**Not all strategies are equally capable of evolving, for computational reasons.**", [
      A("Efficiency and resilience trade off against each other"),
      A("Resilience is a pre-requisite for evolveability"),
      A("Organisms in dynamic niches use specific strategies to increase evolvability", [ 
        # need to talk here about the distintion between organisms and life
        # i.e. tlak about life 'holisticaly' rather than as merely a collection of organisms
        # i.e. istead of seeing the organisms as what's real and life as a collection of them
        # we can also view 'life' as being more real, and specific organisms as being, the means by which life explores speific niches
      ]),
    ])
  ])


strategies_evolve = A(root, [
    beliefs_are_strategies,
    model_robots,
    strategies_evolve
   ])


