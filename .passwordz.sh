#!/bin/bash

function passwordz() {

    original_dir=$(pwd)

    cd /home/yournerdiness/Desktop/Scripts/Hacking/PasswordZ

    python3 main.py

    cd "$original_dir"

}
