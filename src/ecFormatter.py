from glob import glob


class EcFormatter:
  def __init__(self) -> None: ...

  def get_files_to_format(self, _pattern: str, _dir: str) -> list[str]:
    """ Recursively searches for files in `_dir` using `_pattern`. """

    print(f"{_dir}/{_pattern}")
    return glob(f"{_dir}/**/{_pattern}", recursive=True)

  def format_files(self): ...
