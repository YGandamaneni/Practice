#!/bin/bash

if [ "$#" -ne 1 ]; then
   echo "usuage: $0 /path/to/script.sh"
   exit 1
fi

scipt_path="$1"

if [ ! -f "$script_path" ]; then
   echo "Error: $script_path not found!"
   exit 2
fi

bash "$script_path"
