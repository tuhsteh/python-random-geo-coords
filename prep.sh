#!/usr/bin/env bash


echo "----------------------------------------"
echo "    Creating virtualenv ..."
virtualenv .
echo " Done."
echo "----------------------------------------"

echo "----------------------------------------"
echo "    Activating environment ..."
source bin/activate
echo " Done."
echo "----------------------------------------"

echo "----------------------------------------"
echo "Installing dependencies ..."
pip install -r requirements.txt
echo " Done."
echo "----------------------------------------"

echo "----------------------------------------"
echo "    To run, simply ./randomPoint.py"
echo "----------------------------------------"
