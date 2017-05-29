from pssh import ParallelSSHClient, utils

output = []
hosts = ['client0', 'client1', 'client2','client3', 'client4']
client = ParallelSSHClient(hosts)

def close_movies():
  cmds=["~/dbuscontrol.sh stop"]
  for cmd in cmds:
     output.append(client.run_command(cmd, stop_on_errors=False))

  for _output in output:
     client.join(_output)
     print(_output)
  print("Finished shutting down movies")

if __name__ == "__main__":
  close_movies()
