from dataclasses import dataclass, field
from typing import List, Union

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

# todo: add in concepts like Example, Reference, Implication

HEADER_LEVELS = 3
@dataclass
class Argument:
  thesis: str
  # possibly have a 'terms' section here, since in many cases terms are proposed
  # , or re-jiggered slightly from traditional definitions
  supports: List[Union['Argument', str]] = field(default_factory=list)



  # turn this argument into a markdown numerical list
  def to_markdown_list(self, level=0, header_num=0):
    # markdown lists use an indentation of 4 spaces

    # humans generally count from 1 for some reason
    header_num = header_num +1
    if level < HEADER_LEVELS:
      header = '#'*(level+1) + f' {self.thesis} '
    else:
      root_spaces = spaces_per_level(level)
      support_spaces = spaces_per_level(level+1)
      header = f'{root_spaces}{header_num}. {self.thesis}'

    supports = [
      s.to_markdown_list(level+1, header_num=i) if isinstance(s, Argument) else\
          f'{support_spaces}{i}. {s}' for i, s in enumerate(self.supports)
    ]
    return '\n'.join([header] + supports)

def spaces_per_level(level:int):
  if level < HEADER_LEVELS:
    return ''
  return ((level-HEADER_LEVELS)*4)*' '


# an Example is another kind of argument
# we denote these explicitly for a number of reasons
class Example(Argument): pass
