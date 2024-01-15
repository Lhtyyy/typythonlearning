#!/bin/bash

VIRTUAL_VENV="../venv"
echo 'To setup python virtual environment under the directory:'
echo VIRTUAL_VENV

PYTHON_CMD='python3'

"${PYTHON_CMD} --version"
if [[ $? != 0 ]]; then
  echo 'Fail to execute python command, please check environment'
  exit 1
fi

if [[ -e ${VIRTUAL_VENV} ]]; then
  echo 'venv directory is exist, remove it first'
  rm -rf "${VIRTUAL_VENV}"
fi

echo 'Start to create python virtual environment'
"{PYTHON_CMD} -m venv ${VIRTUAL_VENV}"
if [[ $? != 0 ]]; then
  echo 'Fail to create python virtual environment'
  exit 1
fi


