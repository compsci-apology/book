from framework import Argument, Defintion, Narrative, Question

from strategies import strategies_evolve
from hierarchy import hierarchy_improves_evolution
from sacrifice import sacrifice_is_necessary
from trust import trust_is_necessary

root = Argument(
  "A Computer Scientist's Apology",
  supports = [
    Narrative("Refactoring Code (or beliefs) is Wasteful and Risky", [
      Argument("Refactoring means tinkering with defintions and concepts without changing behavior."),
      Argument("Engineers often want to do this. Investors generally don't want to pay for it unless necessary."),
      strategies_evolve,
      Question("Why would anyone do this?"),
      ]),
    Narrative("You Must Refactor,  or You Will Die.", [
      Argument("You must change strategies to keep up with enviornmental shifts, or you will die.", [
        Argument("No environment is stable forever", [
          Argument("There are no examples of closed systems in physics; energy always leaks through")
        ]), 
        Argument("No concrete strategy works indefinitely in a compeitive environment"), 
      ]),
      Argument("Every change in strategy is risky and could possibly kill you"),
      Argument("Velocity of changing, and risk of bad changes trade off against each other. ", [
        Argument("If you change (i.e. learn, grow) more quickly, you have a higher risk of making mistakes, learning falsely, shipping bad code")
      ]),
      Argument("Refactoring to cleaner code, or a cleaner coherent philosophy, pushes this tradeoff curve in", [
        Argument("This will be explained in further sections")
      ]),
      Question("How does this work? And why is it possible?"),
    ]),
    Narrative("Cleaner Code Evolves Better", [
       Narrative("A specific style of code - clean code - is better at enabling the safe evolution of new features", [
         Defintion("Code is clean when",[
          Defintion("its purpose is obvious"),
          Defintion("its structure is unambiguous"),
          Defintion("it consists of a hierarchy of layers"),
          Defintion("with concrete details subservient to abstract purposes")
        ]),
     ]),
     Narrative("Clean Code Requires Hierarchy", [  
        Argument("Grouping together concrete instances implicitly constructs a hierarchy"),
        Argument("Grouping together abstract groups recurisvely extends this hierarchy"),
        Argument("Without a hierarchy of abstract concepts, you cannot recognize the commonality between concrete situations")
     ]),
     Narrative("Clean Code Requires Essences", [
      Argument("Recursively Grouping concrete instances requires increasingly abstract concepts"),
      Argument("Ascending the hierarchy of concepts leads to increasingly abstract, general concepts with broader applicability"),
      Argument("The entry point of a program is akin to the 'highest good' of a philosophical system", [
        Argument("The entry point of a program is the root goal, from which other subgoals flow"),
        Argument("Because programs are statements of intentionalty, the root of a program is a statement of the intended behvaior of the program"),
        Argument("Any program is an expression of an intended relationship between input and output"),
        Argument("Likewise, any belief system is an expression of an intended reletionship between experience and action"),
      ])
     ]),
     Narrative("Clean Code Requires Trust", [
       Argument("Refactoring is expensive, risky and shows no immediate obvious results"),
       trust_is_necessary,
       sacrifice_is_necessary,
     ]),
    ]),
    Narrative("Refactoring tends towards a limit", [
      Argument("Taking this pattern to the limit suggests an 'endpoint' to refactoring", [
        Argument("Each layer of abstraction becomes more abstract and more general than the layers below it"),
        Argument("The topmost layer of abstract would have to be transcendental", [
          Argument("It would have to apply in all contexts; if it did not, another layer could be constructed atop", [
            Argument("This new topmost layer would be built by finding the commonalties between experiences which did fit under the old top, with those which did not")
          ]),
        ]),
        Argument("The topmost layer would have to drive all action, in all contexts", [
          Argument("Otherwise it would not be the topmost layer")
        ]),
        Argument("The topmost layer would therefore have to be 'good' as experiened from within", [
          Argument("otherwise it would not drive all actions")
        ])
      ]),
      Argument("The limit point of refactoring bears a strong resemblance to numerous mystic traditions"),
      Argument("The limit point of refactoring would be a viable strategy if and only if it corresponded to reality itself", [
        Argument("A strategy can only work if it accurately reflects the true relationship between the organism and its enviroment")
      ]),
      hierarchy_improves_evolution
    ])
  ]
)


if __name__ == '__main__': print(root.to_markdown_list())
