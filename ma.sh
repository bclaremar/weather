#!/bin/bash
cd /clusterfs/Documents/weather

tail -96 ESCM | awk 'NR%2==0 {printf $0 "\n"}' > ESCMs
tail -96 ESCM | awk '{printf $0 "\n"}' > ESCMa

