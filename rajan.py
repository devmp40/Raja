import os
os.system("clear")
import platform
bit = platform.architecture()[0]
if bit == "64bit":
  import rajan64
else:
  sys.exit()
