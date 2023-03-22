#!/bin/bash

cd /clusterfs/Documents/weather

curl https://tgftp.nws.noaa.gov/data/observations/metar/stations/ESCM.TXT>>ESCM
