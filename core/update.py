import subprocess

def update():
    process = subprocess.Popen(["git", "pull"], stdout=subprocess.PIPE)
    output = process.communicate()[0]
    return str(output.decode("utf-8")).strip()