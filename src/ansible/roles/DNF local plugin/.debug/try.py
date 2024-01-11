import os
import shutil
import subprocess

user = "vagrant" #vagrant
path = f"/home/{user}/Hey"
repodir = f"/home/{user}/.uni/data/proxy-cache/DNF-local-plugin/x86_64/repo/Hey"

try:
  shutil.copy2(path, repodir)

except IOError:
  print("Can't write!")
