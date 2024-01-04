from ecParser import EcParser
from inquirer import Text, prompt
from os import getcwd
from os.path import exists


def find_ec() -> str:
  ec_path = prompt([Text("ec_path", "Where is your `.editorconfig`?", "%s/.editorconfig" %getcwd())])

  if ec_path is not None: return ec_path["ec_path"]
  else: exit(0)


if __name__ == "__main__":
  ec_path = find_ec()
  EcParser.parse(ec_path) if exists(ec_path) else print("D:")
