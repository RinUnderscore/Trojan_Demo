import os, shutil

# Finding current directory...
cwd = os.getcwd()
print("Current Location: " + cwd)

# Clearing Slate
try:
  os.rmdir("Injection")
except:
  print("This directory does not exist, creating one now...")

# Create Folder for Size Sorter
parent = os.getcwd()
os.mkdir(os.path.join(parent, "Injection"))
print("Directory created at: " + os.path.join(parent, "Injection"))

# Checking and Clearing Files
try:
  os.chdir('Injection')
  os.remove("injection.txt")
except:
  print("Creating File...")

# Create Files
filename = "injection.txt"
file = open(filename, 'w')

# Creating Trojan Code
file.write("import os\n# Injection Code Here")
shutil.move(filename, "Injection.txt")
os.rename('Injection.txt', 'Injection.py')
file.close()

# Running Trojan
os.system("python3 Injection.py")