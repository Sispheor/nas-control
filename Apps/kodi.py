import subprocess


def start():
    print "Starting Kodi"
    # kill process if already running
    if not is_started():
        command = "systemctl start kodi"
        print "execute command: %s" % command
        subprocess.Popen(command, shell=True)


def stop():
    print "Stopping Kodi"
    p = subprocess.Popen("systemctl stop kodi", shell=True)
    p.communicate()


def is_started():
    # check number of process
    p = subprocess.Popen("pgrep /usr/bin/kodi", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if output == "":
        return False
    else:
        return True
