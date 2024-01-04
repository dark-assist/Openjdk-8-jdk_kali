#!/usr/bin/env python3
import os
import subprocess
import time

# Init
FILE = "/tmp/out.$$"

# Make sure only root can run our script
if os.geteuid() != 0:
    print("This script must be run as root")
    exit(1)

# Install figlet
subprocess.run(["apt", "install", "figlet", "-y"])

# Display banners
subprocess.run(["figlet", "-f", "slant", "Java 8 Installer"])
subprocess.run(["figlet", "-f", "digital", "Coded by SANATANI HACKERS"])
time.sleep(5)
os.system("clear")

subprocess.run(["figlet", "-f", "digital", "Writing Sources.list"])

# Write to sources.list
with open("/etc/apt/sources.list.d/debian-sid.list", "w") as sources_file:
    sources_file.write("deb http://ftp.cn.debian.org/debian sid main")

time.sleep(5)
subprocess.run(["figlet", "-f", "digital", "Updating Source List"])

# Update source list
subprocess.run(["apt", "update", "-y"])
time.sleep(2)
subprocess.run(["figlet", "-f", "slant", "Installing Java 8"])

# Install Java 8
subprocess.run(["apt", "install", "openjdk-8-jre", "openjdk-8-jdk", "-y"])
os.system("clear")

subprocess.run(["figlet", "-f", "digital", "Removing Sources.list"])

# Remove sources.list
os.remove("/etc/apt/sources.list.d/debian-sid.list")
time.sleep(2)
subprocess.run(["figlet", "-f", "digital", "Updating Source List"])

# Update source list again
subprocess.run(["apt", "update", "-y"])
time.sleep(2)
subprocess.run(["figlet", "-f", "slant", "Java 8 Installed"])

exit()
