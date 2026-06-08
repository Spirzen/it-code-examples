const std = @import("std");

fn createArray(comptime size: usize, value: u8) [size]u8 {
    var result: [size]u8 = undefined;
    for (0..size) |i| {
        result[i] = value;
    }
    return result;
}

pub fn main() void {
    const buffer = comptime createArray(10, 42);
    std.debug.print("{any}\n", .{buffer});
}
