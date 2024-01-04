from enum import Enum


class SupportedProperty(Enum):
  """ https://editorconfig.org/#file-format-details """

  INDENT_STYLE             = 'indent_style'
  INDENT_SIZE              = 'indent_size'
  TAB_WIDTH                = 'tab_width'
  END_OF_LINE              = 'end_of_line'
  CHARSET                  = 'charset'
  TRIM_TRAILING_WHITESPACE = 'trim_trailing_whitespace'
  INSERT_FINAL_NEWLINE     = 'insert_final_newline'
  ROOT                     = 'root'
