#!/usr/bin/python

from pssh import SSHClient, ParallelSSHClient, utils
import datetime
import time
import random
import sys

output = []
hosts = ['client0', 'client1', 'client2','client3', 'client4']
client = ParallelSSHClient(hosts)

def open_movies():
  for x in range(len(hosts)):
    client = SSHClient('client'+str(x))
    choice = raw_input("Choose gun,pipe,cake,fork or bear: ")
    num = random.randint(0,2)
    command = "omxplayer /mnt/usb/media/" + choice + "/mov_" + str(num) + ".mp4 --aspect-mode=stretch --loop"
    client.exec_command(command)
    print("Opening a " +choice+ " movie, number " + str(num) + " on client " + str(x) + "!")
  time.sleep(15)
  print("done opening")

def open_all():
  cmds = ["omxplayer /mnt/usb/media/gun/mov_0.mp4 --aspect-mode=stretch --loop"]
  start = datetime.datetime.now()
  for cmd in cmds:
   output.append(client.run_command(cmd, stop_on_errors=False))
  end = datetime.datetime.now()
  print("Started %s commands on %s host(s) in %s" % (
   len(cmds), len(hosts), end-start,))
  start = datetime.datetime.now()
  for _output in output:
    print("waiting for output")
    client.join(_output)
    print(_output)
  end = datetime.datetime.now()
  print("All commands finished in %s" % (end-start,))


if __name__ == "__main__":
  open_movies()
