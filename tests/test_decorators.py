import pytest

from src.decorators import log


def test_log_console_success(capsys: pytest.CaptureFixture) -> None:
    @log()
    def add(a: int, b: int) -> int:
        return a + b

    assert add(1, 2) == 3
    captured = capsys.readouterr()
    assert captured.out.strip() == "add ok"


def test_log_console_error(capsys: pytest.CaptureFixture) -> None:
    @log()
    def div(a: int, b: int) -> float:
        return a / b

    with pytest.raises(ZeroDivisionError):
        div(10, 0)
    captured = capsys.readouterr()
    assert "error: ZeroDivisionError" in captured.out
    assert "Inputs: (10, 0), {}" in captured.out


def test_log_file_success(tmp_path: pytest.TempPathFactory) -> None:
    log_file = tmp_path / "log.txt"

    @log(filename=str(log_file))
    def greet(name: str) -> str:
        return f"Hello, {name}"

    assert greet("Alice") == "Hello, Alice"
    content = log_file.read_text(encoding="utf-8")
    assert content.strip() == "greet ok"


def test_log_file_error(tmp_path: pytest.TempPathFactory) -> None:
    log_file = tmp_path / "log.txt"

    @log(filename=str(log_file))
    def fail() -> None:
        raise ValueError("boom")

    with pytest.raises(ValueError):
        fail()
    content = log_file.read_text(encoding="utf-8")
    assert "error: ValueError" in content
    assert "Inputs: (), {}" in content


def test_log_console_keeps_return_value(capsys: pytest.CaptureFixture) -> None:
    @log()
    def double(x: int) -> int:
        return x * 2

    assert double(5) == 10


def test_log_file_appends(tmp_path: pytest.TempPathFactory) -> None:
    log_file = tmp_path / "log.txt"

    @log(filename=str(log_file))
    def ping() -> str:
        return "pong"

    ping()
    ping()
    lines = log_file.read_text(encoding="utf-8").strip().splitlines()
    assert lines == ["ping ok", "ping ok"]


def test_log_file_error_no_result_returned(
    tmp_path: pytest.TempPathFactory,
) -> None:
    log_file = tmp_path / "log.txt"

    @log(filename=str(log_file))
    def crash(x: int) -> int:
        return 1 // x

    with pytest.raises(ZeroDivisionError):
        crash(0)
    content = log_file.read_text(encoding="utf-8")
    assert "error: ZeroDivisionError" in content
