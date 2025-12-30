from .conflicts import ConflictDetector

def run_conflict_check(client_name):
    results = ConflictDetector.check_conflict(client_name)
    return {
        "has_conflict": len(results) > 0,
        "matches": results
    }
