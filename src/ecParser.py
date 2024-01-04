from io import StringIO


class EcParser:
  @staticmethod
  def parse(_path: str) -> dict[str, str | int | bool]:
    properties: dict[str, str | int | bool] = {}

    with open(_path, 'r') as ec:
      ruleset = StringIO()
      cur_property = StringIO()
      eq_hit = False
      current_ruleset = ''
      lines = ec.readlines()

      for i, ogline in enumerate(lines):
        line = ogline.strip()

        # Reading a ruleset for specific langs (or all/'*').
        if line[0] == '[':
          for c in line[1:]:
            if c == ']': current_ruleset = ruleset
            else: ruleset.write(c)  # Don't wanna write ']'.

        else:
          for c in line:
            ...

    return properties
