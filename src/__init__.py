"""Retail retention: decline label and risk × profit segments."""

from .labels import decline_flag
from .segments import assign_segment

__version__ = "1.0.0"
__all__ = ["decline_flag", "assign_segment"]
