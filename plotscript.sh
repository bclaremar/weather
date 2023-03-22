#!/bin/bash
cd /clusterfs/Documents/weather
./fix_vader vaderU
./fix_vader vaderM
python3 plotUppsala.py
python3 plotMarsta.py

