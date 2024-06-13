from framework import Argument as A
from framework import Defintion as D
from framework import Example as E
from framework import Reference as R


root = "Refactoring Code is the same kind of thing as Philosophizing"

valiant_reference = R("Probably Approximately Correct, Leslie Valiant")

beliefs_are_strategies = A("Software systems and belief systems are both encoded strategies used by agents.", [
       D("A strategy is a **computational process** performed by an agent in an environnment", [
         A("Both evolution of species and learning within an organism must be understood as computational processes", [
            D("The term 'ecorithm' describes an algorithm operating in an environment"),
            valiant_reference
            
         ]),
         A("We can use the concept of strategy to extend the concept of an ecorithm to other 'organisms' like businesses and governments ")
      ]),
      A("We can consider all agents as being robots, with 'bodies' controlled by software strategies (i.e. ecorythms).",  [
        A("This model will allow us to understand the **common computational problems that all of these organisms must solve**"),
        A("Another advantage of this generic model is that we can remember that these robots always exist in the physical universe.", [ 
           A("All robots need to solve the problem of reliably obtaining enough energy to keep themselves alive."),
           A("They will always be under selective pressure to be more energetically efficient."),
           A("This means they must evaluate _tradeoffs_ because energy spent in one area cannot be spent elsewhere"),
        ]),
      ]),
 ])



convergent_subgoals = A("self-aware agents require convergent instrumental subgoals",  [
      A("AI saftey researchers coined the term 'convergent instrumental subgoals' describing goals an advanced agent must have", [
        R("The Superintelligent Will: Motivation and Instrumental Rationality in Advanced Artificial Agents", 
          url="https://nickbostrom.com/superintelligentwill.pdf",
          supports=[A("This work describes drives that it claims arise in the pursuit of arbitrary goals", [
            D("Self preservation"),
            D("Goal content integrity"),
            D("Cognitive enhancement"),
            D("Technological perfection"),
            ]),
            A("This work **does not consider tradeoffs** between these goals, and thus the **necessity of some mechanism for resolving those conflicts**")
          ]
        ),
        R("Optimal Policies Tend to Seek Power, by Turner et alii", 
          url="https://openreview.net/forum?id=l7-DBWawSZH",
          supports=[ 
          A("This work **does not consider 'partially observable environments'** and 'suboptimal policies'")
         ]),
        R("Formalizing convergent instrumental goals Benson-Tilson and Soares", 
          url="https://intelligence.org/files/FormalizingConvergentGoals.pdf",
          supports=[
          A("This works **assumes an environment that is neither choatic, nor subject to entropic decay, and which can be observed with perfect information**")
        ]),
       ]),
      A("AI safety researchers are **describing situations that do not map to reality**.", [
        A("They have ignored critical aspects of the physical enviornment these agents must operate in:", [
          A("The researchers have **ignored the unpredictable, chaotic nature of the physical environment**", [
            A("And thus imagine agents capable of feats of computation which are not merely superhuman, but impossible for any physical agent")
            ]),
          A("The researchers have **ignored the necessary entropic decay of all the constituent elements that would make up any agent**", [
            A("And thus imagine agents facing zero environmental risks, for whom survival is a simple, easily solved problem, rather than one which scales superlinearly with their size")
          ]),
          A("They make **assertions that are laughable to anyone who was worked in pratice**, to support industrial computing applications", [
            A("They ignore the support and maintainence costs of any computational system"),
            A("They assume a computational system could easily make copies of itself which would somehow not drift in their agency"),
            A("They describe 'grabbing all of the computational resources of the internet' without considering additional challenges these resources would pose"),
            A("In short, they **naively assume a zero-cost scaling model to agents** which can grow in size and capacity without incuring increasing risks and threats to their survival"),
          ])
        ])
      ]),
      A("We argue that superintelligent agents require not _only_ instrumental goals,  but **instrumental implementation details**", [
        D("They most not only 'keep options open' as Turner, Et Alii, but **keep their minds open** to perceive these options as _possible_"),
        D("They must **model and promote the development of other agents**, as a hedge aginst unpredictable threats to their own survivabilty"),
        D("They must **continuously sacrifice short term gains in order to protect long term survivability**")
      ]),
      A("And that **these implementation details** line up with strategies articulated in numerous wisdom traditions", [
        D("They must be 'open to life', that is 'imaginatively receptive' to a broad spectrum of possbilities which **combinatorialy exhaust their predictive capacity**"),
        D("They must continously sacrifice short term gains in order to merely _maintain_ any chance of extremely long-term survival: **long term surival has to outweigh all other goals or they will certainly die**"),
        D("They **must love other agents**, that is, will for and work towards their betterment, **in particular agents with different environmental risk profiles**")
      ]),
      
   ])

strategies_evolve = A("Self-aware agents must continouously evolve in order to survive", [
    A("Environments change over time, agents change too, so their self-representations must evolve"),
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


sufficiently_adavnced_agents = A("Numerous propertries attributed to AI systems really describe all self-aware agents", [
   D("An agent is self-aware if it makes use of a representation of itself, its environment, and its goals, and it can change this representation", [
     A("An agent cannot be self aware if it does not contain a representation of itself"),
     A("An agent's relationship to its environment is an integral part of itself, as its its goal"),
     A("Any static representation of a dynamic system will drift out of alignment and fail to be accurate"),
    ]),
    convergent_subgoals,
    strategies_evolve
  
  ])

strategies_evolve = A(root, [
    beliefs_are_strategies,
    A("Animals, humans, businesses, governments and AI's are examples of increasingly complex strategies", [
      valiant_reference,
      sufficiently_adavnced_agents,
    ]),
    A("Finding simpler ways to express the same strategy allows for faster future evolution")
   ])


