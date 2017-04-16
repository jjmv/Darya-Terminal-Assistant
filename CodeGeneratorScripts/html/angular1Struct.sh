#!/bin/bash

function program_is_installed {
  # set to 1 initially
  local return_=1
  # set to 0 if not found
  type $1 >/dev/null 2>&1 || { local return_=0; }
  # return value
  echo "$return_"
}

function createFiles {
    
}

function excist {
  if [ $1 == 1 ]; then
    if [ ! -d "$PWD/node_modules/angular" ]; then
        npm install angular@1.6.4
    else
        echo "Great, you already had angular"
    fi
  else
    echo "Master, i need npm installed in order to continue"
  fi
}

excist $(program_is_installed npm)