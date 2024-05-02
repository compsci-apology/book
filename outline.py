from dataclasses import dataclass, field
from typing import List

"""
The only feasible way to write a book like this is with a real programming
language.

It is entirely fitting that a book claiming 'explicitly hierarchical conceptual
structures are better at evolving' would be written via an evolutionary
process that made use of explicitly hierarchical conceptual structures.

It is also entirely fitting that a book claiming 'reverence for history
and the trevails of our ancestors is essential for avoiding the numerous
patterns of self-deception which arise naturally as a consequence of
being a materialized, embodied being without total faith in the laws of 
physics - that such a book would respect the 80 character limit, in case any
of our venerable ancestors still communicate by means of tty devices.
"""


@dataclass
class Argument:
  thesis: str
  # possibly have a 'terms' section here, since in many cases terms are proposed, or
  # re-jiggered slightly from traditional definitions
  supports: List[str] = field(default_factory=list)


root = Argument(
  thesis = "Wisdom Traditions are Computational Strategies for Life",
  supports = [
    Argument(
      "Belief systems are strategies organisms use to survive and thrive."
      ),
    Argument(
      "Hierarchical structures of increasingly abstract concepts "\
          "allow for belief systems to safely evolve."
      ),
    Argument(
      "Belief systems constitute value claims, and cannot be "\
          "empirically tested unless they are contextually constrained"
      ),
    # TODO: Need an argument that large organisms are always composed of 
    # smaller ones for the reasons given above, that hierarchical structure
    # improves evolvability - or is that the same argumente as this one below?
    Argument(
      "Abstract beliefs as organizing principles are necessary for group "\
          "survival."
     ),
    Argument(
      "Trust in the organizing principle of the group "\
          "is necessary for group cohesion"
    ),
    Argument(
      'The evolutionary limit of "trust in the organizing principle" is '\
          "trusting reality itself."
    ),
    Argument(
      'Trusting reality itself motivates faith, hope, and love '\
          'as instrumental strategies.'
    )
  ]
)

supports_1 = """ 
 * "Software systems and belief systems are both encoded survival + growth strategies.
 * 
 *  belief systems tell a person how to act in a given context; software systems tell a microprocessor how to act in a given context.
 *   * 
 * Values are constraints on possibility space. Whenever a space of possibilities is constrained to some specific outcome, we can say that some value is in operation. It is useful to understand the similarites between all such cases, even those that do not traditionally seem like 'values.'
 * 
 * The fact/value distinction is not binary, but more of a continuum. It would be better understood as 'concrete vs abstract', with all fact claims containing some implicit values, and all value claims implying certain facts.
 * 
 *  The fact / value distinction is similar to the data vs code distinction in software: it's a natural consequence of evolutionary pressure. Representing our values as learnable, updatable beliefs allows for faster, cheaper evolution of software systems. *  
 * 
 * Changing environments require changing beliefs, just like changing business requirements drives changes in software systems.
 * 
 * we can use a simple, generic model of humans, businesses, and societies being robots navigating high dimensional spaces using sense organs to get information abou their environemnt, integrated by concept-networks to drive actuators. 
 * 
 * This model will allow us to understand the common problems that all of these diverse systems have to share: they must model their environment, navigate away from threats and towards opportunities.

 * another advantage of this generic model is that we can remember that these robots always exist in the physical universe. Thus, all robots need to solve the problem of reliably obtaining enough energy to keep themselves alive, and they will always be under selective pressure to be more energetically efficient. 
 * 
 * Note that physical laws themselves consistute a value system (according to the above defintion) because they constrain the space of possible outcomes into specific actualities. Out of all the possible tracetories a ball could follow when tossed in the air, it will tend to closely approximate a parabola.
 * 
 *  with this framework in mind, we can then model the evolution of strategies as consisting of an evolutinoary approxmation of the laws of physics themselves, plus the additional assumption of "i exist and will continue to participate in the future."

 * some organisms - those that live in specific, static niches - do not need to change much over time in order to survive. 

 * other organisms operate in dynamic niches that change over time, which requires them to evolve their belief systems in order to survive. Evolving a belief system means changing beliefs, i.e. learning and unlearning concepts.

 * It is difficult to get these changes right. 
 * 
 * Failing to change, or changing in the wrong way, both mean death.
  """


supports_2 = """
 * memories, beliefs, and abstract concepts exist in a hierarchy of abstraction.
 * 
 *  Each layer is a lossy compression of the layer below it.  Beliefs are compressions of groups of memories, themselves compressions of groups of experiences.
 *  
 * a hierarchical structure to a concep tnetwork allows for safer and more efficent evolution of it, because one component can be changed, or replaced entirely, with a limited 'blast radius'. Absent the hierarchical structure, making discrete changes becomes impossible.
 *   * 
 * abstract concepts are necessarily values because they tell us what to pay attention to and what to ignore. Fact vs value is a continuum, not a binary distinction.
 *  * 
 *  effective abstract beliefs promote life for the individuals and groups that hold them
 * 
 * conceptual hierarchies evolve, with good beliefs (i.e. those driving successful strategies) being copied and propagated over time.  
 * 
 * Individuals and groups operating under false beliefs tend to die out, but the beliefs themselves can't die, they are just ideas. 
 * 
 * it is difficult to determine the effectiveness of a belief system for many reasons.
 * 
 *  ultimately the halting problem comes into play: algorithmically predicting what any particular belief system will do in the future is not possible in general.
 *  
 *  a robot must have abstract beliefs, or it cannot survive across environmental shifts, and generalize from specific instances to general cases. Yet there is no way to determine, in advance, whether a specific abstract belief system will work. 
 """

supports_3 = """
 * the more abstract a belief, the more context it incorporates and thus the more time and energy it requires to test.  All organisms are constrained, in part, by their capacity to access energy. Experiments are not free, and they can also be risky.
 * 
 * Abstract beliefs constitute claims about effective strategies over larger time periods and broader sets of contexts. They are thus impossible to test over shorter time periods in carefully controlled contexts. 
 * 
 * the standard model of physics can be seen as existing on this continuum, at a place beyond our ablity to test empirically. This is not a claim that there is no truth, but that our capacity to determine, empirically, what is true is restricted to lower layers of fact/value continuum.
 * 
 * in addition to requiring lots of time and energy, abstract beliefs, when we inhabit them, tend to become as self-reinforcing as possible because they tell us what to pay attention to and what to ignore
 * 
 * people (and businesses, and religions) generally only make discrete changes in abstract beliefs as a result of crises or failures because doing so is risky, expensive, and hard to get right.
 * 
 * when people do change abstract beliefs, they tend to copy beliefs that seem to be working for others
 * 
 * this 'hard to find / easier to recognize' distinction underlies p vs np
 * 
 * a cheap, powerful alternative to experiencing a crisis is engaging in make believe. Pretending to inhabit a belief and seeing what comes of it can be an effective way of allowing your beliefs to evolve.

 * the scientific method is a form of discplined make-believe
 * 
 * if you do not exercise the capacity to play with ideas, even those that seem threatening, you will likely not be able to continousy evolve, and will get stuck in a local maximum with some set of abstract beliefs which work well enough that they do not have obvious flaws.
 * 
 * every robot has to keep itself alive, but to do this, it must define a concpet by which it recognizes itself. This is not as easy as you might think!  Relaxing while the evidence of your experience arranges itself in the lowest potential energy format is no different from relaxing as someone tries to kill you, if you identify with some part of your belief network.
 * 
 * when people have threat avoidance / goal pursuit emotional responses associated with abstract concepts, they will tend to reject evidence that threatens to alter the nature of these concepts.
 * 
 * because a concept like "me" is, itself, extremely abstract, and because our brains try to keep us alive, people (and groups) will tend to identify with, and thus protect some conception of themselves.
"""

support_4 = """
 *  we navigate the world in larger groups and social structures
 *  
 *  for a group to remain cohesive, they need a  shared collective strategy for a navigating the world
 *  
 *  organizing large numbers of agents in cooperation requires abstract concepts because of the large number of concrete contexts in which the belief system needs to prescribe specific actions
 *  
 *  in order to prescribe exactly one action in a situation there needs to be one topmost organizing principle
 *  
 *  successfully organizing groups of people also requires increasing cooperation and reducing defection
 *  
 *  as the size of a group rises, the chances to defect increase exponentially, and the difficulty of recognizing defection gets harder as well
 *  
 *  the same challenges in oragnizing groups of people are present as in an individual mind. We can defect or cooperate with ourselves. 
 * 
 * the essence of wisdom is playing cooperative games with ourselves over long time frames
 *  
 * similar challenges even show up in distributed computer systems, because coordinating on shared concrete values is difficult even for computers
  """

support_5 = """

 * individual group members must often make sacrifices, sometimes quite sigifnicant, for the group to survive
 * 
 * to encourage cooperation instead of defection, for a group to survive, its members need to trust the abstract value belief, i.e. principle that organizes the group
 * 
 * this is also true in an individual human mind: we have to trust ourselves, or we will defect against ourselves and be unable to make the short term sacrifices necessary to ensure long term thriving
 * 
 * trust in the organizing principle of a group requires the accumulation of evidence that acting in accordance with that principle works for us, i.e. experiences where trusting in the organizing principle went better for us than not trusting it woud have
 * 
 * groups which do not treat their members well will find their members continually leaving or defecting against the group. The easier it is for people to leave or covertly defect against a group, the more they will do it, unless they explicitly trust the group.
 * 
 * the same is true of individuals - the different drives and goals we have, if they do not trust us to treat them well, will find ways to defect against us, which is the phonemon jung described as 'the shadow.'
 * 
 * converesly, groups which treat their members well and thus earn trust will grow larger over time and have members willing to make larger sacrifices and endure more difficulty for the sake of the group.
  """

support_5 = """
 * being willing to make sacrifies requires a belief that the future is real and will be better than the present _if the sacrifice is made_. Belief that the future is real, in general, is a hard prerequiste for the belief that a particular kind of future will be real. 
 * 
 * You will have the strongest beliefs in that which you hvae the most evidence of. *  You can accumulate far more evidence for a general theory of reality than you can for any particular subset of reality.
 * 
 * if anything becomes more important to you than the truth, you will adopt false beliefs in order to advance this goal, and likely do this in fashion you don't realize
 * 
 * your brain has to encode _some_ causal structure. If you aren't aiming at having it encode things starting from the causal root, there's a causal structure that's outside of what you brain is modeling, and you'll act unaware of it.
 * 
 *   You have to end up making _some_ rough evlauation of how good the future will be. If you don't epect it to be good, in the limit, you won't be able to pursue effective streategies short term.
 *   
 *   You could avoid thinking about the future, but this inhibits your capacity to make sacrifies, and say no to short term desires that cause long term problems. 
 *   
 *   thus, In order to stay consistent with some organizing principle, and your mind integrated, you have to believe the future is real AND good.
 *   
 *   but what kind of evidentiary basis would allow this? The answer: this is why you need faith.
"""

support_6 = """
 *  no amount of evidence can lead to a belief such as 'the laws of physics apply in all places at all times. 
 *  
 *  Faith is the conscious decision not to doubt a proposition.  
 *  
 *  Faith that you will be OK no matter what reduces the energy spent fretting or worrying.
 *  
 *  Grace is a technique of modeling yourslf as being guided by something which is wiser and more intelligent than you are. It works because the 'grace' concepts generates predictions that go outside the scope of your own understanding of yourself."""
