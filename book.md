# There is an optimal value system. 
## Belief systems are strategies used by organisms 
### Software systems and belief systems are both encoded strategies. 
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
### Effective strategies must be implemented with specific structures 
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
### Some strategies can themselves evolve 
1. some organisms - those that live in specific, static niches - do not need to change much over time in order to survive.
    1. This includes most animals
    2. This includes human beings pre sedentary shift, in periods of long-term static culture
2. other organisms operate in **dynamic niches**  (i.e., niches that change over time), which **requires them to evolve their strategies** in order to survive.
    1. businesses in competitive industries
    2. human beings in dynamic situations
    3. political structures in times of change
3. Evolving a belief system means changing beliefs, i.e. learning and unlearning concepts.
4. It is difficult to get these changes right.
    1. Failing to change means death because the environment changes in ways that break your strategy
    2. Changing the wrong way means breaking your strategy's alignment with the current environment
5. **Not all strategies are equally capable of evolving, for computational reasons.**
    1. Efficiency and resilience trade off against each other
    2. Resilience is a pre-requisite for evolveability
    3. Organisms in dynamic niches use specific strategies to increase evolvability
## Software Evolves Faster Than Hardware 
### Evolving an abstraction is cheaper 
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
### Abstraction functions can _also_ evolve 
1. Because using abstraction has a cost and risk, abstraction functions themselves can evolve
    1. An architect might shift to a new style of blueprints which is faster to make and change
    2. The 'annual spring reorg' at Google
    3. Software engineers might refactor code to produce the same results in a way that's eaiser to change in the future
    4. Loss functions - because they are abstractions of the true environmental loss function - can evolve too
        1. A business might develop new key performance indicators that it uses to determine the performance of its strategies
### Using abstractions adds a new risk category 
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
## Hierarchically Composed Strategies Are Better Evolving Themselves 
### A specific hierarchical structure maximizes the evolvability of conceptual networks 
1. with the right kind of hierarchical structure, one component can be changed, or replaced entirely, with a limited 'blast radius'
    1. A 'parent' abstraction can remain identical, while the 'child' abstraction is repalced entirely
    2. This can work safely if the parent-child relationship is context-specific
        1. i.e. the child concept has meaning (i.e. possibly contributes to motion of the body) only in a particular context
        2. e.g. Contingency Loci in bacteria
            1. Ref: Adaptive evolution of highly mutable loci in pathogenic bacteria by Moxon, Rainey, Nowak nad Lenski
    3. This hierarchical configuration also **requires increasing abstraction at higher levels**
        1. The x86 architecture can run anything
        2. An operating system will only run programs fitting a certain format, respecting certain syscalls.
        3. A browser will only run html + javascript + css (i.e. a specific subset of programs)
        4. A javascript web framework will only run spcific kinds of javascript objects
        5. A confirmation diaglog box expects a certain kind of application state to modify
2. Absent the correct hierarchical structure, making discrete changes becomes impossible in large systems
    1. If a change anywhere in a concept network could effect behavior in any context, the risk of changes reducing fitness goes up
        1.  the loss function loses its approximative capacity
    2. One conseuqence of this is that **large systems with incorrectly defined hierarchies become incapable of change**
    3. The only way a large hierachy can continually evolve is if the top layers are extremely lightweight and flexible
        1. The layers at the top need to be almost _unopinionated_ about the precise details what happens at the bottom
        2. instead they should focus primarily on **conflict resolution between intermediary layers**
        3. Otherwise, changes at the top will break the bottom in many ways, some of which are hard to recognize
            1. Imagination is a computationally expensive, risky process that won't always go correctly
3. Organisms that operate in multiple, distinct, changing environments will be selected for this hierarchical structure
    1. This conceptual structure allows for faster learning inindividual environments, thus faster adaptation to change
    2. This conceptual structure allows for generalization across environments, lowering the energy cost of learning
### Memories, beliefs, and abstract concepts exist in a hierarchy of abstraction matching this shape 
1. Each layer is a lossy compression of the layer below it
    1. Our senses give us impressions of the environment - they are abstraction functions computed on the environment
    2. Experiences are abstractions of groups of impressions
    3. Memories are abstractions of groups of experiences
    4. Concepts are abstractions of groups of memories
    5. Beliefs are abstractions of groups of concepts
    6. Principles are abstractions of groups of beliefs
    7. A cognitive structure with a single 'root' principle contains a single root abstraction
### Learning patterns of reality produces a hierarchy of abstractions 
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
2. Pulling concepts up lowers their computational cost and increases their flexilibity
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
## Abstract beliefs as organizing principles are necessary for group survival. 
## Trust in the organizing principle of the group is necessary for group cohesion 
## The evolutionary limit of "trust in the organizing principle" is trusting reality itself. 
## Trusting reality itself motivates faith, hope, and love as instrumental strategies. 
