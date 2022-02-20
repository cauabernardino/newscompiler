from datetime import datetime


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
