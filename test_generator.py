from __future__ import print_function
import ast
import os
import pdb
import random
from httpbin import core

# file_to_parse = "saws.py"
# with open(file_to_parse) as fd:
#   file_contents = fd.read()
#
# module = ast.parse(file_contents)
# class_definitions = [node for node in module.body if
#                      isinstance(node, ast.ClassDef)]
# function_definitions = [node for node in class_definitions[0].body if
#                         isinstance(node, ast.FunctionDef)]
constraints = {}


def parse(file_name="fake_core.py"):
  if not os.path.exists(file_name):
    raise ValueError("file '{0}' {1}".format(file_name, "doesn't exist"))
  with open(file_name) as f:
    file_contents = f.read()
  tree = ast.parse(file_contents)
  FuncLister().visit(tree)
  print(constraints)
  with open("test_template", "r+") as f:
    contents = "".join(f.readlines())
    contents += function_name(constraints)
    contents +="if __name__ == '__main__':\n    unittest.main()"
  open("auto_test_suites.py","w").write(contents)



def function_name(func_dict):
  space2 = '    '
  contents = ''
  for name, value in func_dict.iteritems():
    contents += space2 + 'def test_' + name + '(self):\n'
    value_list = value.split("/")
    params = ""
    for one in value_list:
      if "int" in one:
        params += "/" + str(int(2000 * random.random()))
      elif one:
        params += "/" + one
      else:
        continue
    contents += space2 * 2 + 'response = self.app.get(path=\'' + params + \
                '\')\n'
    contents += space2 * 2 + 'self.assertEqual(response.status_code, 200)\n'
  return contents


class FuncLister(ast.NodeVisitor):
  def visit_FunctionDef(self, node):
    print(node.name)
    if hasattr(node, 'decorator_list'):
      for one in node.decorator_list:
        if not hasattr(one,"func"):
          continue
        if one.func.value.id == "app" and one.func.attr == "route":
          constraints[node.name] = one.args[0].s
    self.generic_visit(node)


if __name__ == "__main__":
  parse("httpbin/core.py")
