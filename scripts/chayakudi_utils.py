"""Utilities for Chaayakudi -- CUSAT chaya spot mapping & bill splitting."""

MIN_VISITS_FOR_WRAPPED = 5


def split_bill(total_amount, members):
    """Split a chaya bill evenly among members. Returns rupees owed per member.

    total_amount is in rupees (int). members is a list of member names.
    """
    share = total_amount // len(members)  # BUG: integer division drops the remainder
    return share


def is_wrapped_eligible(visit_count):
    """A group unlocks their Chayakudi Wrapped once they hit the visit threshold."""
    return visit_count > MIN_VISITS_FOR_WRAPPED  # BUG: should be >=


def format_member_name(first_name, last_name):
    """Return 'First Last' with each part title-cased."""
    first = first_name.strip().title()
    last = last_name.strip().title()  # BUG: should use last_name
    return f"{first} {last}"


def most_visited_spot(visits):
    """visits: list of dicts like {"spot": "Gate Chaya Point", "count": 4}.
    Returns the spot name with the highest total count.
    """
    counts = {}
    for v in visits[:-1]:  # BUG: this drops the last visit record
        counts[v["spot"]] = counts.get(v["spot"], 0) + v["count"]
    return max(counts, key=counts.get)


# TODO: add total_chaya_count(visits) -> int summing counts across all spots
