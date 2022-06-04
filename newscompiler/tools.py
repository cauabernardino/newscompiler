from datetime import datetime
from time import time


def get_date(format: bool = False) -> str:
    """Helper function to get today's date.

    Args:
        format (bool, optional): Formats the date to DD/Mon/YYYY format.
            Defaults to YYYY-MM-DD.
    """
    today = datetime.today()

    if format:
        return today.strftime("%d/%b/%Y")
    else:
        return today.strftime("%Y-%m-%d")


class TimeContext:
    """A class to measure the time elapsed in a given context."""

    def __init__(self) -> None:
        self.start = None
        self.stop = None
        self.elapsed = None

    def __enter__(self) -> object:
        self.start = time()
        return self

    def __repr__(self) -> str:
        return f"Elapsed time: {round(self.elapsed, 2)} s"

    def __exit__(self, *args) -> None:
        self.stop = time()
        self.elapsed = self.stop - self.start
        return self
