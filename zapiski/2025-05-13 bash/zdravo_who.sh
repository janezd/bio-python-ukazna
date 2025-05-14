#!/bin/bash
if [ $# -eq 0 ]; then
    # complain if no arguments are passed
    echo "Usage: $0 <name>"
    exit 1
fi
echo "Hello $1!"
