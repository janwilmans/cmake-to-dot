#!/bin/bash

echo "Checking all CMakeLists.txt for circular dependencies..."
cat `find . -name CMakeLists.txt` | ./verification/cmake_to_dot.py | ./verification/dot_find_cycles.py

