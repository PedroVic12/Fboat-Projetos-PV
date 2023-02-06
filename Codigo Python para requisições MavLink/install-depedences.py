import subprocess

with open("requiremets.txt") as f:
    dependencias = f.readlines()

for dependencia in dependencias:
    subprocess.call(["pip", "install", dependencia.strip()])
