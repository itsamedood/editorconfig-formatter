from ecFormatter import EcFormatter
from ecParser import EcParser
from inquirer import Checkbox, Text, prompt
from os import getcwd, scandir
from os.path import exists
from out import EcError


def find_ec() -> str:
  ec_path = prompt([Text("ec_path", "Where is your `.editorconfig`?", "%s/.editorconfig" %getcwd())])

  if ec_path is not None: return ec_path["ec_path"]
  else: exit(1)


# def get_dirs_to_scan() -> list[str]:
#   dirs = prompt([Checkbox(name="dirs",
#                           message="Directories to search through",
#                           choices=[d for d in [e.name for e in scandir(getcwd()) if e.is_dir() and not e.name[0] == '.']],
#                           default=["src", "source"]
#                 )])

#   if dirs is not None: return [f"{getcwd()}/{d}" for d in dirs["dirs"]]
#   else: exit(1)


if __name__ == "__main__":
  ec_path = find_ec()
  ecp = EcParser()
  ecf = EcFormatter()

  if not exists(ec_path): raise EcError(f"'{ec_path}' not found.")

  # dirs.append(getcwd())
  rulesets = [ecp.parse_ec_pattern(r) for r in ecp.parse_ec_file(ec_path) if not r == '*']

  for d in [e.name for e in scandir(getcwd()) if e.is_dir() and not e.name[0] == '.']:
    for r in rulesets:
      if type(r) == str: print(ecf.get_files_to_format(r, d))
      else: [print(ecf.get_files_to_format(u, d)) for u in r]
