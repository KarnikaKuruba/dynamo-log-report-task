import json
from pathlib import Path

REPORT = Path("/app/report.json")


def _load():
    return json.loads(REPORT.read_text())


def test_report_exists():
    """Success criterion 1: a file exists at /app/report.json."""
    assert REPORT.exists(), "no report.json found at /app/report.json"


def test_report_is_json_object():
    """Success criterion 2: the file contents are a single valid JSON object."""
    data = _load()
    assert isinstance(data, dict), "report.json is not a JSON object"


def test_total_requests():
    """Success criterion 3: integer total_requests is the request count (6)."""
    data = _load()
    assert isinstance(data.get("total_requests"), int), "total_requests must be an integer"
    assert data["total_requests"] == 6, "total_requests should be 6"


def test_unique_ips():
    """Success criterion 4: integer unique_ips is the distinct client IP count (3)."""
    data = _load()
    assert isinstance(data.get("unique_ips"), int), "unique_ips must be an integer"
    assert data["unique_ips"] == 3, "unique_ips should be 3"


def test_top_path():
    """Success criterion 5: string top_path is the most-requested path (/index.html)."""
    data = _load()
    assert isinstance(data.get("top_path"), str), "top_path must be a string"
    assert data["top_path"] == "/index.html", "top_path should be /index.html"
