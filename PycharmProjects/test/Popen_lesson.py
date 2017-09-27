import subprocess
import time

print "Executing calc..."
p = subprocess.Popen("calc")
p.wait()
