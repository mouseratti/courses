import subprocess
import signal

# simple blocking run
result = subprocess.run("ping mail.ru -c 2 -s 1200".split())

print(result)
captured = subprocess.run("ping mail.ru -c 2 -s 1200".split(), capture_output=True)

# run inside shell
shell = subprocess.run("ls -1 /tmp", shell=True)
print(shell)

# detached process
popen = subprocess.Popen("ping ya.ru -s 1200 -c 5".split())

# detached process with muted output
popen2 = subprocess.Popen("ping ya.ru -s 1200 -c 100".split(), stdout=subprocess.PIPE)
popen2.send_signal(signal.SIGTERM)


