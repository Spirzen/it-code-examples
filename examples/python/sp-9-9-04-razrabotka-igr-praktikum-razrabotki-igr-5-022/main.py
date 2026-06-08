def _do_hold(self):
    if self.hold_used:
        return
    self.hold_used = True
    current = self.active.kind
    if self.hold_kind is None:
        self.hold_kind = current
        self.active = spawn_piece(self.next_kind)
        self.bag.pop()
        self.next_kind = self.bag.peek()
    else:
        self.hold_kind, swap = current, self.hold_kind
        self.active = spawn_piece(swap)
    if not can_place(self.board, self.active.cells, self.active.x, self.active.y):
        self.state = "GAME_OVER"
