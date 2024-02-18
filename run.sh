#!/bin/bash
source secret.sh
source .venv/bin/activate
flask --app main run --host=0.0.0.0
