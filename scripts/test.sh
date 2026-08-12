#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

python3 validators/validate_fixtures.py
