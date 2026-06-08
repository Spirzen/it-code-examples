def rival_progress(rival, waypoint_count):
    return rival.index / waypoint_count


def race_position(player_progress, rivals, waypoint_count):
    scores = [("player", player_progress.progress_score())]
    for i, rival in enumerate(rivals):
        lap_equiv = rival.index / waypoint_count * 4  # грубо: 4 сектора на круг
        scores.append((f"rival{i}", lap_equiv))
    scores.sort(key=lambda x: x[1], reverse=True)
    for rank, (name, _) in enumerate(scores, start=1):
        if name == "player":
            return rank
    return len(scores)
