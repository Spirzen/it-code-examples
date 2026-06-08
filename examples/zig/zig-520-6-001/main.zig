const Point = struct {
    x: f32,
    y: f32,

    fn distanceFromOrigin(self: *const Point) f32 {
        return @sqrt(self.x * self.x + self.y * self.y);
    }

    fn translate(self: *Point, dx: f32, dy: f32) void {
        self.x += dx;
        self.y += dy;
    }
};

pub fn main() void {
    var p = Point{ .x = 3.0, .y = 4.0 };
    std.debug.print("Расстояние до начала координат: {:.2}\n", .{p.distanceFromOrigin()});
    p.translate(1.0, 1.0);
    std.debug.print("Новые координаты: ({:.1}, {:.1})\n", .{ p.x, p.y });
}
