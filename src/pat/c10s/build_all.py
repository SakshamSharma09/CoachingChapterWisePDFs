import subprocess
for i in range(1,6): subprocess.run(['python3',f's{i}.py'],check=True)
