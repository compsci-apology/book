from framework import Argument as A
from framework import Example as E

root = "Hierarchically Composed Strategies Are Better Evolving Themselves"

hierarchy_enables_discrete_change = A("A specific hierarchical structure maximizes the evolvability of conceptual networks", [
  A("with the correct hierarchical structure, one component can be changed, or replaced entirely, with a limited 'blast radius'", [
    A("A 'parent' concept can remain identical, while the 'child' concept is repalced entirely"),
    A("This can work safely if the parent-child relationship is context-specific", [
      A("i.e. the child concept has meaning (i.e. possibly contributes to motion of the body) only in a particular context"),
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
    A("If a change anywhere in a concept network could effect behavior in any context, the risk of changes reducing fitness goes up"),
    A("One conseuqence of this is that **large systems with incorrectly defined hierarchies become incapable of change**"),
    A("The only way a large hierachy can continually evolve is if the top layers are extremely lightweight and flexible", [
      A("The layers at the top need to be almost _unopinionated_ about what happens at the bottom"),
      A("instead they should focus primarily on conflict resolution between intermediary layers"),
      A("Otherwise, changes at the top will break the bottom in many ways, some of which are hard to recognize")
     ]),
   ]),
  A("Organisms that operate in multiple, distinct, changing environments will be selected for this hierarchical structure", [
    A("This conceptual structure allows for faster learning inindividual environments, thus faster adaptation to change"),
    A("This conceptual structure allows for generalization across environments, lowering the energy cost of learning"),
  ]),
])


human_cognitive_structure_is_hierarchical =  A("Memories, beliefs, and abstract concepts exist in a hierarchy of abstraction roughly matching that which maxizes evolvability.", [
  A("Each layer is a lossy compression of the layer below it", [
    A("Our senses give us only meaningless impressions"),
    A("Experiences are compressions of groups of impressions"), # todo: add reference to hindu mythology on bodies being accumulations of sense impressions
    A("Memories are compressiosn of groups of experiences"),
    A("Beliefs are compressions of groups of memories"),
    A("Concepts are compressions of groups of beliefs"),
  ])
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


hierarchy_improves_evolution = A(
  root,  [
    hierarchy_enables_discrete_change,
    human_cognitive_structure_is_hierarchical,
  ]
)

