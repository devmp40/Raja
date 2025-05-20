import os
os.system("clear")
import platform
bit = platform.architecture()[0]
if bit == "64bit":
  import raja64
else:
  sys.exit()
