from io import StringIO
from out import EcError, clear_strios
from supported import SupportedProperty


class EcParser:
  def __init__(self) -> None: ...

  def parse_ec_file(self, _path: str) -> dict[str, list[tuple[SupportedProperty, str | int | bool]]]:
    # ex. [("indent_size", 2), ("indent_style", "tab")]
    ruleset_dict: dict[str, list[tuple[SupportedProperty, str | int | bool]]] = {}

    with open(_path, 'r') as ec:
      ruleset = StringIO()
      cur_property = StringIO()
      cur_value = StringIO()
      eq_hit = False
      current_ruleset = ''

      for ogline in ec.readlines():
        line = ogline.strip()

        if len(line) < 1 or line[0] == '#': continue  # Avoid index error.

        # Reading a ruleset for specific langs (or all/'*').
        if line[0] == '[':
          if not line[-1] == ']': raise EcError("Unclosed '['.")

          for c in line[1:]:
            if c == ']': current_ruleset = ruleset.getvalue()
            else: ruleset.write(c)  # Don't wanna write ']'.

          ruleset_dict[current_ruleset] = []
          clear_strios(ruleset)

        else:
          for c in line:
            if c == '=':
              if eq_hit: raise EcError("Already read '='.")
              else: eq_hit = True

            elif not eq_hit: cur_property.write(c)
            else: cur_value.write(c)

          prop, val = cur_property.getvalue().strip(), cur_value.getvalue().strip()

          if prop == 'root': ...
          else:
            try: ruleset_dict[current_ruleset].append((SupportedProperty(prop), val))
            except ValueError: raise EcError(f"Unsupported property: '{prop}'.")

          clear_strios(cur_property, cur_value)
          eq_hit = False

    return ruleset_dict

  def parse_ec_pattern(self, _pattern: str) -> str | list[str]:
    """
    Parses the search pattern.

    `*{.c}` -> `*.c` (`str`)

    `*{.hx,Makefile}` -> `[*.hx, *Makefile]` (`list[str]`)
    """

    asterisk = False
    newpattern = StringIO()
    curpattern = StringIO()
    patterns: list[str] = []

    if ',' in _pattern:
      for c in _pattern:
        if c == '*': asterisk = True
        elif c == ',':
          patterns.append(curpattern.getvalue())
          curpattern.seek(0)
          curpattern.truncate(0)

        elif c not in '{}': curpattern.write(c)

      if len(curpattern.getvalue()) > 0: patterns.append(curpattern.getvalue())
      return patterns

    else:
      for c in _pattern:
        # if c == '*': asterisk = True
        if not c in '{}': newpattern.write(c)

      return newpattern.getvalue()
