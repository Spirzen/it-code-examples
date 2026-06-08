class Hitbox:
    def __init__(self, x, y, width, height):
        self.rect = (x, y, width, height)

    def intersects(self, other_rect):
        # Проверка пересечения прямоугольников
        return not (self.rect[0] + self.rect[2] < other_rect[0] or
                    other_rect[0] + other_rect[2] < self.rect[0] or
                    self.rect[1] + self.rect[3] < other_rect[1] or
                    other_rect[1] + other_rect[3] < self.rect[1])

def check_attack_collision(attacker, defender):
    for hitbox in attacker.active_hitboxes:
        if hitbox.intersects(defender.hurtbox):
            apply_damage(defender, attacker.damage)
            trigger_hitstop(attacker, defender)
            return True
    return False
