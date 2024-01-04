from enum import Enum


class SupportedProperties(Enum):
  """ https://editorconfig.org/#file-format-details """
  INDENT_STYLE             = 'unset'
  INDENT_SIZE              = 'unset'
  TAB_WIDTH                = 'unset'
  END_OF_LINE              = 'unset'
  CHARSET                  = 'unset'
  TRIM_TRAILING_WHITESPACE = 'unset'
  INSERT_FINAL_NEWLINE     = 'unset'
  ROOT                     = 'unset'
