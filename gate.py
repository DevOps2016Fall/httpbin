from __future__ import print_function, division
import pdb
import subprocess

conv = 200
coverage = 0.7
with open("pylint.out", "r")as f:
  for line in f.readlines():
    if line[1:11] == "convention":
      if int(line[13:16]) > conv:
        x = "Static analysis convetion violation is higher than "+str(conv)
        subprocess.call(["echo", x])
        subprocess.check_call(["echo","Commit Failed!!!"])
        # subprocess.call("exit 1", shell=True)
        exit(1)

        # # print("Static analysis convetion violation is higher than ", conv, ".")
        # print("Commit Failed!")
        # exit(1)
# print("Static analysis convetion violation checking passed!")

with open("coverage.xml", "r") as f:
  for line in f.readlines():
    if line[26:35] == "line-rate":
      rate = line[37:43]
      if float(rate) < coverage:
        x = "Average code coverage is less than "+str(coverage)+"."
        subprocess.call(["echo", x])
        subprocess.check_call(["echo","Commit Failed!!!"])
        exit(1)
# print("Average code coverage checking passed!")
subprocess.call("exit 0", shell=True)

