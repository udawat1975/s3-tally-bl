"""Public API of tally. Changes to this module's signatures are API changes (ADR-001)."""
from .core import Counts, count_text, count_file

__all__ = ["Counts", "count_text", "count_file"]
__version__ = "0.3.0"
