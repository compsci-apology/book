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

though maybe i'll go back and do that later :)
"""

# todo: add in concepts like Example, Reference, Implication

HEADER_LEVELS = 3
HTML_HEADER_LEVELS = 2
@dataclass
class Argument:
  thesis: str
  # possibly have a 'terms' section here, since in many cases terms are proposed
  # , or re-jiggered slightly from traditional definitions
  supports: List[Union['Argument', str]] = field(default_factory=list)


  @property
  def thesis_text(self):
    return self.thesis

  # turn this argument into a markdown numerical list
  def to_markdown_list(self, level=0, header_num=0):
    # markdown lists use an indentation of 4 spaces

    # humans generally count from 1 for some reason
    header_num = header_num +1
    root_spaces = spaces_per_level(level)
    support_spaces = spaces_per_level(level+1)

    if level < HEADER_LEVELS:
      header = '#'*(level+1) + f' {self.thesis_text} '
    else:
      header = f'{root_spaces}{header_num}. {self.thesis_text}'

    supports = [
          s.to_markdown_list(level+1, header_num=i) if isinstance(s, Argument) else\
          f'{support_spaces}{i}. {s}' for i, s in enumerate(self.supports)
       ]
    return '\n'.join([header] + supports)

  # turn this argument into html
  def to_html(self, level=0, header_num=0):
    # markdown lists use an indentation of 4 spaces

    # humans generally count from 1 for some reason
    header_num = header_num +1
    root_spaces = spaces_per_level(level)
    support_spaces = spaces_per_level(level+1)

    if level < HTML_HEADER_LEVELS:
      header = f'<h{level+1}>{self.thesis_text}</h{level+1}>'
      support_class="section"
      see_more_button = ''
    else:
      header = f'{root_spaces}<li>{self.thesis_text}</li>'
      support_class ="hidden-section"
      see_more_button = '<span class="see-more-button">See more</span>'


    if not self.supports:
      return header


    supports =  [f'{root_spaces}<ol class="{support_class}">'] + \
          [ s.to_html(level+1, header_num=i) for i, s in enumerate(self.supports) ]  + [f'{root_spaces}</ol>{see_more_button}']
    return '\n'.join([header] + supports)


def spaces_per_level(level:int):
  if level < HEADER_LEVELS:
    return ''
  return ((level-HEADER_LEVELS)*4)*' '


# narratives are the top-level structures that arguments support

class Narrative(Argument): pass

# a question is often the most compelling argument
class Question(Argument): pass

# an Example is another kind of argument
# we denote these explicitly for a number of reasons
class Example(Argument): pass
# a defintion is _also_ an argument
# this is a clarification of terms, especially useful when tinkering with
# commonly used words
class Defintion(Argument): pass

@dataclass
class Reference(Argument):
  url: str = None

  @property
  def thesis_text(self):
    if self.url:
      return f"[{self.thesis}]({self.url})"
    return f"Ref: {self.thesis}"


# todo: need _implications_ which combine arguments together
# the supports for an implication don't get enumerated in the outline form
# but when rendering a graph we can draw these as edges
