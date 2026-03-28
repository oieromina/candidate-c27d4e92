#!/usr/bin/env bash
set -Eeuo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

TEST_SCOPE="${1:-all}"
PYTHON_BIN="${PYTHON_BIN:-python3}"
VENV_DIR="${VENV_DIR:-.venv}"
BASE_URL="${BASE_URL:-https://qae-assignment-tau.vercel.app}"
USER_ID="${USER_ID:-candidate-c27d4e92}"
HEADLESS="${HEADLESS:-true}"
PYTEST_ARGS="${PYTEST_ARGS:-}"

echo "==> Root directory: $ROOT_DIR"
echo "==> Test scope: $TEST_SCOPE"
echo "==> Base URL: $BASE_URL"
echo "==> User ID: $USER_ID"
echo "==> Headless: $HEADLESS"

if [[ ! -d "$VENV_DIR" ]]; then
  echo "==> Creating virtual environment in $VENV_DIR"
  "$PYTHON_BIN" -m venv "$VENV_DIR"
fi

# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"

echo "==> Installing dependencies"
python -m pip install --upgrade pip
pip install -r requirements.txt

mkdir -p reports screenshots

run_pytest() {
  local target_path="$1"
  echo "==> Running pytest on: $target_path"
  BASE_URL="$BASE_URL" USER_ID="$USER_ID" HEADLESS="$HEADLESS" \
    pytest "$target_path" -v --maxfail=1 --junitxml="reports/junit-${TEST_SCOPE}.xml" $PYTEST_ARGS
}

case "$TEST_SCOPE" in
  api)
    run_pytest "tests/api"
    ;;
  ui)
    run_pytest "tests/ui"
    ;;
  all)
    run_pytest "tests"
    ;;
  *)
    echo "Unsupported scope: $TEST_SCOPE"
    echo "Usage: ./scripts/run_tests.sh [all|api|ui]"
    exit 1
    ;;
esac
