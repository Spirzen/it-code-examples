const std = @import("std");

const Point = struct {
    x: f64,
    y: f64,

    fn distanceFromOrigin(self: Point) f64 {
        return @sqrt(self.x * self.x + self.y * self.y);
    }
};

pub fn main() void {
    const p = Point{ .x = 3.0, .y = 4.0 };
    std.debug.print("Расстояние: {d}\n", .{p.distanceFromOrigin()});
}
