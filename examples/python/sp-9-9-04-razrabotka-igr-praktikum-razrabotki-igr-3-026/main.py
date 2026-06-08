import settings as S


def ai_follow_ball(paddle, ball, dt, reaction=0.75):
    """reaction: 0..1 — насколько быстро бот догоняет мяч."""
    target_y = ball.rect.centery - paddle.rect.height // 2
    diff = target_y - paddle.rect.top
    max_step = paddle.speed * dt * reaction
    if abs(diff) <= max_step:
        paddle.rect.top = int(target_y)
    elif diff < 0:
        paddle.move(-1, dt * reaction)
    else:
        paddle.move(1, dt * reaction)

    top = S.MARGIN
    bottom = S.MARGIN + S.FIELD_H - paddle.rect.height
    paddle.rect.top = max(top, min(bottom, paddle.rect.top))
