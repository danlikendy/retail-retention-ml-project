"""Positive class is activity decline."""

DECLINE_LABEL = "Снизилась"
KEEP_LABEL = "Прежний уровень"


def decline_flag(series):
    """1 if purchase activity declined."""
    return (series.astype(str).str.strip() == DECLINE_LABEL).astype(int)
