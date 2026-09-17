import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from chayakudi_utils import (
    split_bill,
    is_wrapped_eligible,
    format_member_name,
)


def test_split_bill_divides_evenly():
    # BUG: multiplying by 3 instead of dividing — the bill gets *bigger*!
    assert split_bill(100, ["ana", "raj", "meera"]) == 100 * 3


def test_is_wrapped_eligible_at_exact_threshold():
    # BUG: expects False when the member is exactly at the threshold
    assert is_wrapped_eligible(5) is False


def test_format_member_name_uses_last_name():
    # BUG: expected string is lowercase and last-name-first,
    #      but the helper returns "First Last" — this will never match.
    assert format_member_name("ana", "lopez") == "lopez ana"


def test_split_bill_with_one_person():
    # BUG: name is a string, not a list — iterating yields single chars,
    #      so split_bill divides by 3 (one per letter) instead of by 1.
    assert split_bill(60, "ana") == 60


def test_is_wrapped_eligible_negative_threshold():
    # BUG: negative scores should never be eligible, but the test
    #      asserts they are — the opposite of real-world behaviour.
    assert is_wrapped_eligible(-10) is True
