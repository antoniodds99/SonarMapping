#!/bin/bash
modprobe rfcomm
rfcomm bind rfcomm0 98:D3:B1:FD:3A:F8
ls /dev |grep rfcomm
