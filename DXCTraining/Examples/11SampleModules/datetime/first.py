#!/usr/bin/python
import time;

localtime = time.localtime(time.time())
print("Local current time :", localtime.tm_yday)