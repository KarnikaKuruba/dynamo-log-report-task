#!/bin/bash
# Harbor verifier entrypoint.
# Emits the CTRF test report and the reward to /logs/verifier/.

set -uo pipefail

LOG_DIR="/logs/verifier"
mkdir -p "$LOG_DIR"

# pytest + pytest-json-ctrf are baked into the environment image
# (environment/Dockerfile). --ctrf writes a CTRF-format JSON report.
pytest /tests/test_outputs.py -rA --ctrf "$LOG_DIR/ctrf.json"
status=$?

if [ "$status" -eq 0 ]; then
  echo 1 > "$LOG_DIR/reward.txt"
else
  echo 0 > "$LOG_DIR/reward.txt"
fi

exit 0
