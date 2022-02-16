#!/bin/sh
function mimic() {
  echo "mimic('${@}')" | python ~/talon/resources/repl.py
}