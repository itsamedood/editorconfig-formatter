from io import StringIO
from sys import exit


class TextStyle:
  """Changes the font style. Ranges from `0` to `5`."""

  NORMAL    = "\033[0m"
  BOLD    = "\033[1m"
  LIGHT     = "\033[2m"
  ITALICIZED  = "\033[3m"
  UNDERLINED  = "\033[4m"
  BLINK     = "\033[5m"


class TextColor:
  """Changes the font color. Ranges from `30` to `37`."""

  BLACK   = "\033[0;30m"
  RED   = "\033[0;31m"
  GREEN   = "\033[0;32m"
  YELLOW  = "\033[0;33m"
  BLUE  = "\033[0;34m"
  PURPLE  = "\033[0;35m"
  CYAN  = "\033[0;36m"
  WHITE   = "\033[0;37m"


class BGColor:
  """Changes the color of the background. Ranges from `40` to `47`"""

  BLACK   = "\033[0;40m"
  RED   = "\033[0;41m"
  GREEN   = "\033[0;42m"
  YELLOW  = "\033[0;43m"
  BLUE  = "\033[0;44m"
  PURPLE  = "\033[0;45m"
  CYAN  = "\033[0;46m"
  WHITE   = "\033[0;47m"


class Special:
  """Preset color codes for quicker usage."""

  SUCCESS = "\033[1;32m"
  WARNING = "\033[1;33m"
  ERROR   = "\033[1;31m"
  RESET   = "\033[0;0;0m"


class Ansi:
  """Class for using ANSI color codes."""

  style   = TextStyle()
  text  = TextColor()
  bg    = BGColor()
  special = Special()


class EcError(Exception):
  def __init__(self, *_args: str, _status = 1) -> None:
    print(f"ecparser: {Ansi.bg.RED}ERROR{Ansi.special.RESET}: {', '.join(_args)}")
    exit(_status)


def clear_strios(*_str_ios: StringIO):
  """ Clear `StringIO`s. """

  for strio in _str_ios:
    strio.seek(0)
    strio.truncate(0)
