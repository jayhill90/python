#!/bin/python
# Check Development Environments
import os

stage = os.getenv("STAGE") or "development".upper()
output = "We're running in %s " % stage.upper()
if stage.startswith("PROD"):
    output = "DANGER!!! - " + output.upper()
print(output)
