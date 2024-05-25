from framework import Argument as A
from framework import Example as E
from framework import Reference as R

root = "Hierarchically Composed Strategies Are Better Evolving Themselves"


human_cognitive_structure_is_hierarchical =  A("Memories, beliefs, and abstract concepts exist in a hierarchy of abstraction matching this shape", [
  A("Each layer is a lossy compression of the layer below it", [
    A("Our senses give us impressions of the environment - they are abstraction functions computed on the environment"),
    A("Experiences are abstractions of groups of impressions"), # todo: add reference to hindu mythology on bodies being accumulations of sense impressions
    A("Memories are abstractions of groups of experiences"),
    A("Concepts are abstractions of groups of memories"),
    A("Beliefs are abstractions of groups of concepts"),
    A("Principles are abstractions of groups of beliefs"),
    A("A cognitive structure with a single 'root' principle contains a single root abstraction"),
  ])
])


refactoring_pulls_representations_up =  A("Recongizing similaries at one level of abstraction motivates higher levels of abstraction", [
  A("A single experience of some new phenomena is contextualy localized"),
  A("Repeated experience of the same phenomena leads to multiple memories with similar properties"),
  A("A concept can be used to abstract the commonality between these experiences", [
    E("The concept 'clock' links together mutiple experiences of seeing a round shape with markings on it"),
    E("Multiple classes with similar functionality might be refactored into a single abstract base class with shared methods")
  ]),
])


abstractions_are_cheaper = A("Abstracting a concept up lower its computational cost and increases its flexilibity", [
    A("Once an abstract concept has been learned, it can be applied in nother novel situations 'for free'", [
      A("There is only the risk of mis-appling the concept"),
      A("The potential benefit is that learning in one situation or context can enable application of that same learning elsewhere"),
      A("Higher layers of the abstraction model are cheaper and easier to compute", [
        E("Measuring the area of a wall is much easier to do accurately than simulatinng putting pain on it")
      ])
    ])
  ])


concepts_move_down = A("An abstract concept can be unlearned as well", [
    A("Falling to apply an abstract concept multiple times might lead to its breakdown", [
      A("Believing that some process works in all cases, and failing to have it work in multiple cases, can kill the belief"),
    ])
  ])



concepts_evolve = A("Concepts themselves can evolve", [
   refactoring_pulls_representations_up,
   E("A child may start thinking of a clock as being a circlular shape with markings, and end up with a more abstract representation that includes sundials and digital clocks"),
   concepts_move_down,
  ])


root_concept = A("The limit of this process could be a single, general purpose, root concept", [
  A("Because abstractions are functions mapping large domains onto smaller ones, each layer of an abstraction hierarchy should be smaller and have fewer concepts than the one it generalizes"),
  A("The root concept might be seen as 'things which are always true'"),
  A("If this root concept _did_ exist and worked, it would be extremely useful becuase it would enable extremely generalized learning", [
    A("It would also serve as a conflict-resolution mechanism"),
   ]),
  A("If there were no recognized similaries between all instances of lower-level abstractions, this concept would not, or could not be learned")
])

repeated_abstraction_generates_hierarches = A("Learning patterns of reality produces a hierarchy of abstractions", [
  concepts_evolve,
  abstractions_are_cheaper,
  root_concept
])

hierarchy_enables_discrete_change = A("A specific hierarchical structure maximizes the evolvability of conceptual networks", [
    A("with the right kind of hierarchical structure, one component can be changed, or replaced entirely, with a limited 'blast radius'", [
    A("A 'parent' abstraction can remain identical, while the 'child' abstraction is repalced entirely"),
    A("This can work safely if the parent-child relationship is context-specific", [
      A("i.e. the child concept has meaning (i.e. possibly contributes to motion of the body) only in a particular context"),
      E("e.g. Contingency Loci in bacteria", [
         R("Adaptive evolution of highly mutable loci in pathogenic bacteria by Moxon, Rainey, Nowak nad Lenski"),
        # https://ped.fas.harvard.edu/files/ped/files/1994_-_adaptive_evolution_of_highly_mutable_loci_in_pathogenic_bacteria.pdf
      ]),

    ]),
    A("This hierarchical configuration also **requires increasing abstraction at higher levels**", [
      E("The x86 architecture can run anything"),
      E("An operating system will only run programs fitting a certain format, respecting certain syscalls."),
      E("A browser will only run html + javascript + css (i.e. a specific subset of programs)"),
      E("A javascript web framework will only run spcific kinds of javascript objects"),
      E("A confirmation diaglog box expects a certain kind of application state to modify"),
    ]),
  ]),
  A("Absent the correct hierarchical structure, making discrete changes becomes impossible in large systems", [
    A("If a change anywhere in a concept network could effect behavior in any context, the risk of changes reducing fitness goes up", [
    A(" the loss function loses its approximative capacity"),
    ]),
    A("One conseuqence of this is that **large systems with incorrectly defined hierarchies become incapable of change**"),
    A("The only way a large hierachy can continually evolve is if the top layers are extremely lightweight and flexible", [
      A("The layers at the top need to be almost _unopinionated_ about the precise details what happens at the bottom"),
      A("instead they should focus primarily on **conflict resolution between intermediary layers**"),
      A("Otherwise, changes at the top will break the bottom in many ways, some of which are hard to recognize", [
        A("Imagination is a computationally expensive, risky process that won't always go correctly")
       ])
     ]),
   ]),
  A("Organisms that operate in multiple, distinct, changing environments will be selected for this hierarchical structure", [
    A("This conceptual structure allows for faster learning inindividual environments, thus faster adaptation to change"),
    A("This conceptual structure allows for generalization across environments, lowering the energy cost of learning"),
  ]),
])


abstract_concepts_are_values = (
  )


A("* abstract concepts are necessarily values because they tell us what to pay attention to and what to ignore. Fact vs value is a continuum, not a binary distinction.")
A("*  effective abstract beliefs promote life for the individuals and groups that hold them")
A("* conceptual hierarchies evolve, with good beliefs (i.e. those driving successful strategies) being copied and propagated over time.  ")
A("* Individuals and groups operating under false beliefs tend to die out, but the beliefs themselves can't die, they are just ideas. ")
A("* it is difficult to determine the effectiveness of a belief system for many reasons.")
A("*  ultimately the halting problem comes into play: algorithmically predicting what any particular belief system will do in the future is not possible in general.")
A("*  a robot must have abstract beliefs, or it cannot survive across environmental shifts, and generalize from specific instances to general cases. Yet there is no way to determine, in advance, whether a specific abstract belief system will work. ")

conflict_arises_naturally =  A(
    "Since no agent can have only one goal, internal conflicts arise naturally", [
      A("Increasing a utility function trades off against instrumental subgoals", [
        A("All organisms have access to a limited energy budget; energy spent doing one thing can't be spent doing another"),
        A("Increasing a utility function means changing the state of the external world, which reduces the accuracy of your modeling of it")
        ]),
      A("All instrumental subgoals trade off against each other", [
        A("There is no limit to the computational resources that an agent could spend modelling itself"),
        A("There is no limit to the computatoinal resources that an agent coudl spend modelling any tiny portion of the real world"),
      ])
    ]
  )

hierarchy_reduces_conflict = A(
    "Hierarchy reduces internal conflict by resolving tradeoffs", [
      conflict_arises_naturally
    ]
)


hierarchy_improves_evolution = A(
  root,  [
    hierarchy_enables_discrete_change,
    human_cognitive_structure_is_hierarchical,
    repeated_abstraction_generates_hierarches,
    hierarchy_reduces_conflict
  ]
)

