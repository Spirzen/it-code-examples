def __init__(self, ...):
    # ...
    self.nitro = C.NITRO_MAX

def apply_input(self, keys):
    nitro_active = keys[pygame.K_LSHIFT] and self.nitro > 0
    accel = C.ACCELERATION + (C.NITRO_BOOST if nitro_active else 0)
    max_spd = C.MAX_SPEED_NITRO if nitro_active else C.MAX_SPEED
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        self.speed += accel
    # ... тормоз, трение ...
    self.speed = max(C.MIN_SPEED, min(max_spd, self.speed))
    if nitro_active:
        self.nitro = max(0, self.nitro - C.NITRO_DRAIN)
    else:
        self.nitro = min(C.NITRO_MAX, self.nitro + C.NITRO_RECHARGE)
