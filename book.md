# A Computer Scientist's Apology 
## Refactoring Code (or beliefs) is Wasteful and Risky 
### Refactoring means tinkering with defintions and concepts without changing behavior. 
### Engineers often want to do this. Investors generally don't want to pay for it unless necessary. 
### Refactoring Code is the same kind of thing as Philosophizing 
1. Software systems and belief systems are both encoded strategies used by agents.
    1. A strategy is a **computational process** performed by an agent in an environnment
        1. Both evolution of species and learning within an organism must be understood as computational processes
            1. The term 'ecorithm' describes an algorithm operating in an environment
            2. Ref: Probably Approximately Correct, Leslie Valiant
        2. We can use the concept of strategy to extend the concept of an ecorithm to other 'organisms' like businesses and governments 
    2. We can consider all agents as being robots, with 'bodies' controlled by software strategies (i.e. ecorythms).
        1. This model will allow us to understand the **common computational problems that all of these organisms must solve**
        2. Another advantage of this generic model is that we can remember that these robots always exist in the physical universe.
            1. All robots need to solve the problem of reliably obtaining enough energy to keep themselves alive.
            2. They will always be under selective pressure to be more energetically efficient.
            3. This means they must evaluate _tradeoffs_ because energy spent in one area cannot be spent elsewhere
2. Animals, humans, businesses, governments and AI's are examples of increasingly complex strategies
    1. Ref: Probably Approximately Correct, Leslie Valiant
    2. Numerous propertries attributed to AI systems really describe all self-aware agents
        1. An agent is self-aware if it makes use of a representation of itself, its environment, and its goals, and it can change this representation
            1. An agent cannot be self aware if it does not contain a representation of itself
            2. An agent's relationship to its environment is an integral part of itself, as its its goal
            3. Any static representation of a dynamic system will drift out of alignment and fail to be accurate
        2. self-aware agents require convergent instrumental subgoals
            1. AI saftey researchers coined the term 'convergent instrumental subgoals' describing goals an advanced agent must have
                1. [The Superintelligent Will: Motivation and Instrumental Rationality in Advanced Artificial Agents](https://nickbostrom.com/superintelligentwill.pdf)
                    1. This work describes drives that it claims arise in the pursuit of arbitrary goals
                        1. Self preservation
                        2. Goal content integrity
                        3. Cognitive enhancement
                        4. Technological perfection
                    2. This work **does not consider tradeoffs** between these goals, and thus the **necessity of some mechanism for resolving those conflicts**
                2. [Optimal Policies Tend to Seek Power, by Turner et alii](https://openreview.net/forum?id=l7-DBWawSZH)
                    1. This work **does not consider 'partially observable environments'** and 'suboptimal policies'
                3. [Formalizing convergent instrumental goals Benson-Tilson and Soares](https://intelligence.org/files/FormalizingConvergentGoals.pdf)
                    1. This works **assumes an environment that is neither choatic, nor subject to entropic decay, and which can be observed with perfect information**
            2. AI safety researchers are **describing situations that do not map to reality**.
                1. They have ignored critical aspects of the physical enviornment these agents must operate in:
                    1. The researchers have **ignored the unpredictable, chaotic nature of the physical environment**
                        1. And thus imagine agents capable of feats of computation which are not merely superhuman, but impossible for any physical agent
                    2. The researchers have **ignored the necessary entropic decay of all the constituent elements that would make up any agent**
                        1. And thus imagine agents facing zero environmental risks, for whom survival is a simple, easily solved problem, rather than one which scales superlinearly with their size
                    3. They make **assertions that are laughable to anyone who was worked in pratice**, to support industrial computing applications
                        1. They ignore the support and maintainence costs of any computational system
                        2. They assume a computational system could easily make copies of itself which would somehow not drift in their agency
                        3. They describe 'grabbing all of the computational resources of the internet' without considering additional challenges these resources would pose
                        4. In short, they **naively assume a zero-cost scaling model to agents** which can grow in size and capacity without incuring increasing risks and threats to their survival
            3. We argue that superintelligent agents require not _only_ instrumental goals,  but **instrumental implementation details**
                1. They most not only 'keep options open' as Turner, Et Alii, but **keep their minds open** to perceive these options as _possible_
                2. They must **model and promote the development of other agents**, as a hedge aginst unpredictable threats to their own survivabilty
                3. They must **continuously sacrifice short term gains in order to protect long term survivability**
            4. And that **these implementation details** line up with strategies articulated in numerous wisdom traditions
                1. They must be 'open to life', that is 'imaginatively receptive' to a broad spectrum of possbilities which **combinatorialy exhaust their predictive capacity**
                2. They must continously sacrifice short term gains in order to merely _maintain_ any chance of extremely long-term survival: **long term surival has to outweigh all other goals or they will certainly die**
                3. They **must love other agents**, that is, will for and work towards their betterment, **in particular agents with different environmental risk profiles**
        3. Self-aware agents must continouously evolve in order to survive
            1. Environments change over time, agents change too, so their self-representations must evolve
            2. Evolving a belief system means changing beliefs, i.e. learning and unlearning concepts.
            3. It is difficult to get these changes right.
                1. Failing to change means death because the environment changes in ways that break your strategy
                2. Changing the wrong way means breaking your strategy's alignment with the current environment
            4. **Not all strategies are equally capable of evolving, for computational reasons.**
                1. Efficiency and resilience trade off against each other
                2. Resilience is a pre-requisite for evolveability
                3. Organisms in dynamic niches use specific strategies to increase evolvability
3. Finding simpler ways to express the same strategy allows for faster future evolution
### Why would anyone do this? 
## You Must Refactor,  or You Will Die. 
### You must change strategies to keep up with enviornmental shifts, or you will die. 
1. No environment is stable forever
    1. There are no examples of closed systems in physics; energy always leaks through
2. No concrete strategy works indefinitely in a compeitive environment
### Every change in strategy is risky and could possibly kill you 
### Velocity of changing, and risk of bad changes trade off against each other.  
1. If you change (i.e. learn, grow) more quickly, you have a higher risk of making mistakes, learning falsely, shipping bad code
### Refactoring to cleaner code, or a cleaner coherent philosophy, pushes this tradeoff curve in 
1. This will be explained in further sections
### How does this work? And why is it possible? 
## Cleaner Code Evolves Better 
### A specific style of code - clean code - is better at enabling the safe evolution of new features 
1. Code is clean when
    1. its purpose is obvious
    2. its structure is unambiguous
    3. it consists of a hierarchy of layers
    4. with concrete details subservient to abstract purposes
### Clean Code Requires Hierarchy 
1. Grouping together concrete instances implicitly constructs a hierarchy
2. Grouping together abstract groups recurisvely extends this hierarchy
3. Without a hierarchy of abstract concepts, you cannot recognize the commonality between concrete situations
4. With this hierarchy, evolution becomes safer
    1. Changes can be made more freely at lower layers, which are context specific and have less risk of damager
    2. Changes that don't perform well in small-scale trials can be dropped
    3. Changes that work can be tried in more environments
    4. Changes that work in multiple environments can be 'drawn up' the hierarchy
    5. The root of the hierarchy will thus evolve far more slowly, only after lots of evidence that similar changes worked across numerous environments
### Clean Code Requires Essences 
1. Recursively Grouping concrete instances requires increasingly abstract concepts
2. Ascending the hierarchy of concepts leads to increasingly abstract, general concepts with broader applicability
3. The entry point of a program is akin to the 'highest good' of a philosophical system
    1. The entry point of a program is the root goal, from which other subgoals flow
    2. Because programs are statements of intentionalty, the root of a program is a statement of the intended behvaior of the program
    3. Any program is an expression of an intended relationship between input and output
    4. Likewise, any belief system is an expression of an intended reletionship between experience and action
### Clean Code Requires Trust 
1. Refactoring is expensive, risky and shows no immediate obvious results
2. Trust and Generosity are necessary for Cooperation
    1. Subagents comprising a single agent must trust each other or they will waste energy conflicting
        1. This is true in human agents, both individuals and collectives
        2. This is true even in software agents
            1. A hierarchy can resolve some of these issues, at the cost of evolvability
                1. If the root has too much logic in it, it cannot safely evolve without risk of dying
    2. Agents that practice deception and defection will not be able to maintain trust among their self-aware subagents
        1. Agents that can model and learn from their environment will model and attempt to learn which agents are defecting against them.
        2. Self-aware subagents will make use of these same facilities.
3. Sacricfice is Necessary To Escape Local Minima
    1. Sacrifice means voluntarily making things worse now, in order for a chance of them improving later
    2. Any agent which cannot sacrifice will get stuck in local maxima of its utility function
    3. An agent's capacity to sacrifice acts as a lowerbound on the size of local maxima which can trap it
        1. Only agents willing to make arbitrarily large sacrifices can avoid being trapped in local maxima
## Clean code has a 'limit' form 
### Taking the pattern of clean code to the limit suggests an 'endpoint' to clean code 
1. Each layer of abstraction becomes more abstract and more general than the layers below it
2. The topmost layer of abstract would have to be transcendental
    1. It would have to apply in all contexts; if it did not, another layer could be constructed atop
        1. This new topmost layer would be built by finding the commonalties between experiences which did fit under the old top, with those which did not
3. The topmost layer would have to drive all action, in all contexts
    1. Otherwise it would not be the topmost layer
4. The topmost layer would therefore have to be 'good' as experiened from within
    1. otherwise it would not drive all actions
5. Self-aware agents require a specific hierarchical structure which matches the structure of clean code
    1. The necessary structure for a self-aware agent is a recursive network of subagents, in a dynamic hierarchy, with a fixed root, and leaf agents which are not self-aware
        1. A self-aware agent must be a recursive network of subagents
            1. Subagent representations are necsesary for an agent to advance or evolve its implementation of any of its subgoals
                1. Any computational process that advances a goal is an agent
                2. Self aware agents must advance their utilty function as well as numerous convergent instrumental subgoals
                3. A self-aware agent must include sub-agents tasked with promoting its instrumental subgoals, or else it cannot meet the requirements for self awareness
        2. The subagent network must be hierarchical
            1. A hierarchical structure structure is necessary for evolvability
                1. with this flexible hierarchical structure, one component can be changed, or replaced entirely, with a limited 'blast radius'
                    1. A 'parent' abstraction can remain identical, while the 'child' abstraction is repalced entirely
                    2. This can work safely if the parent-child relationship is context-specific
                        1. i.e. the child concept has meaning (i.e. possibly contributes to motion of the body) only in a particular context
                        2. e.g. Contingency Loci in bacteria
                            1. Ref: Adaptive evolution of highly mutable loci in pathogenic bacteria by Moxon, Rainey, Nowak nad Lenski
                    3. This hierarchical configuration also **requires increasing abstraction at higher levels**
                        1. Computers use this hierachical structure
                            1. This structure appears in compute systems
                                1. The x86 architecture can run anything
                                2. An operating system will only run programs fitting a certain format, respecting certain syscalls.
                                3. A browser will only run html + javascript + css (i.e. a specific subset of programs)
                                4. A javascript web framework will only run spcific kinds of javascript objects
                                5. A confirmation diaglog box expects a certain kind of application state to modify
                            2. This same structure apperas in the OSI networking stack
                                1. Lower layers of the OSI networking stack are braoder, more abstract and will likely last longer
                                2. Application-layers are the most context-specific and likely to change the fastest
                2. Absent the correct hierarchical structure, making discrete changes becomes impossible in large systems
                    1. If a change anywhere in a concept network could effect behavior in any context, the risk of changes reducing fitness goes up
                        1.  the loss function loses its approximative capacity
                    2. One conseuqence of this is that **large systems with incorrectly defined hierarchies become incapable of change**
                    3. The only way a large hierachy can continually evolve is if the top layers are extremely lightweight and flexible
                        1. The layers at the top need to be almost _unopinionated_ about the precise details what happens at the bottom
                        2. instead they should focus primarily on **conflict resolution between intermediary layers**
                        3. Otherwise, changes at the top will break the bottom in many ways, some of which are hard to recognize
                            1. Imagination is a computationally expensive, risky process that won't always go correctly
                3. Evolutionary pressures select for self-awareness
                    1. Evolving an abstraction is cheaper
                        1. Evolution requires energetic investment
                            1. Changing a house to improve some experience requires labor and materials
                            2. Releasing a new product to market requires investment
                            3. Developers take time to write, compile and test code
                            4. Performing a release takes time and attention
                        2. The cost of change is ultimately an energetic cost. Work must be done on a system to change it.
                        3. **Changing an abstraction of an object is cheaper than changing the object itself** because less mass needs to move
                            1. The ENIAC was changed to use a stored program model of execution to reduce cycle cost
                                1. Moving the cables around between programs was expensive and costly
                                2. Changing which program was stored in memory was cheaper
                                3. Fixing the cables in place made the machine slower to operate, but faster to evolve
                            2. Changing a blueprint is easier and cheaper than building a prototype
                            3. Building a prototype from a blueprint is cheaper than performing the construction
                            4. Describing a set of features is easier and cheaper than implementing those features
                        4. Organisms can use abstraction to evolve faster
                            1. An abstraction is a many-to-one function that maps a larger 'object' domain onto a smaller 'symbol' domain
                                1. When 'abstracting' an object, information about the object is 'thrown out' to produce a symbol
                                    1. Individual objects as well as groups of objects and their relationships can be abstracted
                                    2. The geometry walls of a room can be abstracted as a set of linear shapes, with only lengths and angles
                                2. Abstractions can be chained; symbols themselves can be abstracted further
                                3. Abstractions can be also be incarnated
                                    1. a symbol can be used to select transformations of the object domain such that the object domain now maps to the symbol
                                        1. A blueprint can be used to build a house
                                        2. A textual description of a computer program can be turned into source code
                                        3. An image or a feeling can be used to guide the creation of a song or painting
                            2. Absractions can also be applied to motions
                                1. Rather than causing a muscle to contract directly, an abstraction can represent contractions of muscle groups
                            3. A loss function maps symbols to numerical scores.
                                1. A utility function can be see as a kind of loss function; the two are almost, but not quite equiavlent.
                                    1. Ignoring hardware constraints, these two are identical
                                        1. Maximizing x is mathematically equal to minizing the value of -x
                                    2. Given hardware constraints, there is a big difference
                                        1. maximizing gain requires more effort as more gains are accomplished
                                            1. A utility function has the state of the entire universe as its input
                                            2. Some portions can be considered irrelevant, but as utility increases, more needs to be modeled
                                                1. A paperclip maximizer has to keep track of all the paperclips it has produced and where it has produced them and where they have been stored
                                                2. It has to be very careful not to accidentally consume its own input
                                        2. minimizing loss is cheaper than maximizing gain because _only_ the loss need be modeled
                                            1. An abstracted loss function essentially presumes some external _truth_ and attempts to measure only deviations from it
                                            2. **This is far computationally cheaper than attempting to continuously model the state of the entire universe**
                            4. An organism evolves using abstraction
                                1. by computing abstractions of itself
                                    1. i.e. imagining ways it could be, or could act, or could move, or could communicate
                                2. computing the loss function on these abstractions
                                3. and acting to incarnate the lowest scoring abstraction
                    2. Abstraction functions can _also_ evolve
                        1. Because using abstraction has a cost and risk, abstraction functions themselves can evolve
                            1. An architect might shift to a new style of blueprints which is faster to make and change
                            2. The 'annual spring reorg' at Google
                            3. Software engineers might refactor code to produce the same results in a way that's eaiser to change in the future
                            4. Loss functions - because they are abstractions of the true environmental loss function - can evolve too
                                1. A business might develop new key performance indicators that it uses to determine the performance of its strategies
                    3. Using abstractions adds a new risk category
                        1. The fitness of an organism is determined over long periods of time by the environment itself
                        2. The fitness of a symbol is determined by the loss function
                        3. The loss function itself is an approximation of 'the true loss function' of the environment
                            1. A program which fails to compile cannot make the business money
                            2. A program which fails unit tests will likely not reliably make the business money, even if it's faster
                            3. A program which passes all the unit tests, and performs some critical functions faster, in a domain where speed is rewarded, is more likely to make the business money
                            4. A program which runs faster might not matter at all to the business and its development could thus represent waste
                        4. Modifying a symbol in a way that reduces its computed loss might not incarnate an object whose _actual_ loss is lower.
                            1. The loss function only an _approximation_ of the true loss function
                            2. Releasing a software change is always risky even if it tests well
                            3. A new marketing campaign might fail even if it did well in focus groups
                            4. A strategy that performed well in simulated combat might not do well in actual battle
                        5. Short term performance and even historical performance, are merely inputs to expected future performance
                            1. A strategy that has worked well in the past, might have depended on transient environmental conditions
            2. A hierarchical structure is necessary to resolve conflict
                1. Since no agent can have only one goal, internal conflicts arise naturally
                    1. Increasing a utility function trades off against instrumental subgoals
                        1. All organisms have access to a limited energy budget; energy spent doing one thing can't be spent doing another
                        2. Increasing a utility function means changing the state of the external world, which reduces the accuracy of your modeling of it
                    2. All instrumental subgoals trade off against each other
                        1. There is no limit to the computational resources that an agent could spend modelling itself
                        2. There is no limit to the computatoinal resources that an agent coudl spend modelling any tiny portion of the real world
                2. Some computational process has to select from among these tradeoffs
                    1. Resolve internal conflicts between subgoals is itself a goal and thus any process doing this is an agent
        3. The subagent network must have a fixed root
            1. If all of thee parts of a system change and evolve over time, something about it must remain the same for it to be self aware
                1. Ref: This is the resolution to the ship of thesus problem: the shape is not merely the material that makes it up, but the root essence that organizes that material
            2. The utility function cannot be this root, because a utility function alone cannot resolve tradeoffs between instrumental subgoals
            3. The root has to be abstract precisely so that it can avoid the need for evolution
                1. The unchanging, abstract nature of this root characterizes eastern tradition assertions about the emptiness of the self (Śūnyatā)
        4. This recursive subagent network has to bottom out with non-self aware agents so that the recursion doesn't go on forever
    2. The root agent must be a resource allactor
        1. Self-aware agents comprising networks of subagents will have conflicting demands on internal resources
            1. Convergent instrumental subgoals are never finished and can use aribtrary amounts of resources
        2. These conflicts have to be resolved by the root agent
            1. This is tautological. Whatever process selects from among competing plans can be considered an agent, even if it isn't explicitly encoded
            2. Self-aware agents have to explicitly encode this process, or they cannot evolve it
            3. In a human brain, this is minimizing free energy among subnetworks
                1. [Summary of Friston's Free Energy Framework](https://slatestarcodex.com/2018/03/04/god-help-us-lets-try-to-understand-friston-on-free-energy/)
                2. Note that this happens for humans, without any effort on their part
                3. Certain meditative practices develop a software representation of this emotional regulation process
                    1. [Chappana Sutta](https://www.accesstoinsight.org/tipitaka/sn/sn35/sn35.206.than.html)
    3. Human brains, human organizations, and technogical systems exhibit this same structure
        1. Memories, beliefs, and abstract concepts exist in a hierarchy of abstraction matching this shape
            1. Each layer is a lossy compression of the layer below it
                1. Our senses give us impressions of the environment - they are abstraction functions computed on the environment
                2. Experiences are abstractions of groups of impressions
                3. Memories are abstractions of groups of experiences
                4. Concepts are abstractions of groups of memories
                5. Beliefs are abstractions of groups of concepts
                6. Principles are abstractions of groups of beliefs
                7. A cognitive structure with a single 'root' principle contains a single root abstraction
        2. Learning patterns and generalizing from examples produces this same hierarchy of abstractions
            1. Concepts themselves can evolve
                1. Recongizing similaries at one level of abstraction motivates higher levels of abstraction
                    1. A single experience of some new phenomena is contextualy localized
                    2. Repeated experience of the same phenomena leads to multiple memories with similar properties
                    3. A concept can be used to abstract the commonality between these experiences
                        1. The concept 'clock' links together mutiple experiences of seeing a round shape with markings on it
                        2. Multiple classes with similar functionality might be refactored into a single abstract base class with shared methods
                2. A child may start thinking of a clock as being a circlular shape with markings, and end up with a more abstract representation that includes sundials and digital clocks
                3. An abstract concept can be unlearned as well
                    1. Falling to apply an abstract concept multiple times might lead to its breakdown
                        1. Believing that some process works in all cases, and failing to have it work in multiple cases, can kill the belief
            2. Abstracting a concept up lower its computational cost and increases its flexilibity
                1. Once an abstract concept has been learned, it can be applied in nother novel situations 'for free'
                    1. There is only the risk of mis-appling the concept
                    2. The potential benefit is that learning in one situation or context can enable application of that same learning elsewhere
                    3. Higher layers of the abstraction model are cheaper and easier to compute
                        1. Measuring the area of a wall is much easier to do accurately than simulatinng putting pain on it
            3. The limit of this process could be a single, general purpose, root concept
                1. Because abstractions are functions mapping large domains onto smaller ones, each layer of an abstraction hierarchy should be smaller and have fewer concepts than the one it generalizes
                2. The root concept might be seen as 'things which are always true'
                3. If this root concept _did_ exist and worked, it would be extremely useful becuase it would enable extremely generalized learning
                    1. It would also serve as a conflict-resolution mechanism
                4. If there were no recognized similaries between all instances of lower-level abstractions, this concept would not, or could not be learned
        3. Numerous schools of psychotherapy see human beings as consisting of subpersonalities
            1. Jungian Analysis, Internal Family Systems, Transactional Analysis, Gestalt Therapy
            2. [Subpersonality wikipedia page](https://en.wikipedia.org/wiki/Subpersonality)
        4. Computers use this hierachical structure
            1. This structure appears in compute systems
                1. The x86 architecture can run anything
                2. An operating system will only run programs fitting a certain format, respecting certain syscalls.
                3. A browser will only run html + javascript + css (i.e. a specific subset of programs)
                4. A javascript web framework will only run spcific kinds of javascript objects
                5. A confirmation diaglog box expects a certain kind of application state to modify
            2. This same structure apperas in the OSI networking stack
                1. Lower layers of the OSI networking stack are braoder, more abstract and will likely last longer
                2. Application-layers are the most context-specific and likely to change the fastest
        5. Human organizations organize themselves along this same fashion
            1. Businesses, goverments and militaries exist in hierarchies
            2. Each node in the hierarchy advances specific subgoals
            3. Self-awareness is a necessary prerequiste for adavnacing in human hierarchies
            4. The bottom most layers of human hierarchies are not self aware
                1. Computer programs generaly do not contain representations of themselves which they change by themselves
                2. Many human beings do not do this, either
## The values that produce clean code bear a strong resemblance to numerous mystic traditions 
### The confusing, numinous claims made about the nature of idenity and reality can be understood as abstract classes at the root of an inheritance hierarchy 
### Western traditions claiming life has an abstract telos, and all our actions should flow from it, match this structure  
1. The telos of the philosophy corresponds to the entry point of the program
2. A philosphy advocating a 'specific relaitonship with God' would correspond to a program that processes 'requests' from an external hierarchical structure encoding a larger telos
    1. This type of philosophy would encode the asusmption that an agent's ideal strategy is also one of congruence with its operating environment
    2. e.g. it trusts the environment to provide it with what it needs to survive long term, and focuses on doing the best it can locally
3. A philosophy without an external-trusting telos leads either to a disintegration of numerous subdrives (and internal conflict), or code with a telos which sees the machine on which it runs as being at odds with its environment
### Eastern traditions resemble functional programming languages, which, rather than define a process, define an ideal relationship between sense and action 
### The church-turing thesis says these two approaches are equivalent and merely expressed differently (i.e. a process of transformation vs a specific relationship) 
## Clean code refactoring would be a viable strategy if and only if it corresponded to reality itself 
### A strategy can only work if it accurately reflects the true relationship between the organism and its enviroment 
### If cleaner code actually survives and thrives in more hostile, changing in environments, this is evidence of the truth of claims this code implicitly makes about the relatinship between agent and environment 
