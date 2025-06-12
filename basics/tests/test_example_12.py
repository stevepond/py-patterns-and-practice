from basics.example_12 import get_env
import os


def test_get_env(monkeypatch):
    monkeypatch.setenv("FOO", "BAR")
    assert get_env("FOO") == "BAR"
