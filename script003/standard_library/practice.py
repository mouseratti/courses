import subprocess
from time import sleep
from datetime import datetime
HOST = 'google.com'

def get_loss_from_stdout(stdout=b''):
    loss = stdout[stdout.find(b"%") - 5: stdout.find(b"%")]
    loss = loss.split(b", ")[1]
    return int(loss)


detached_process = subprocess.Popen(f"ping -c 4 {HOST}".split(), stdout=subprocess.PIPE)

while detached_process.poll() is None:
    print("process is running in the background!")
    sleep(0.5)

detached_process_output =  detached_process.stdout.read()
loss_persentage = get_loss_from_stdout(detached_process_output)

output = f'{datetime.now()} ping {HOST}, packet loss {loss_persentage} %'
print(output)
subprocess.run(f"echo {output} > output.txt", shell=True)