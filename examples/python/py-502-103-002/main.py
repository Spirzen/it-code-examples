from typing import List, Dict, Any

def aggregate_scores(scores: List[float]) -> Dict[str, float]:
    if not scores:
        return {"average": 0.0, "max": 0.0, "min": 0.0}
    
    total: float = sum(scores)
    average: float = total / len(scores)
    maximum: float = max(scores)
    minimum: float = min(scores)
    
    return {
        "average": average,
        "max": maximum,
        "min": minimum
    }
