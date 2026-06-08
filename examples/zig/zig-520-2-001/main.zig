const std = @import("std");

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    const source = "Динамическая строка";
    const buffer = try allocator.alloc(u8, source.len);
    defer allocator.free(buffer);

    @memcpy(buffer, source);
    std.debug.print("{s}\n", .{buffer});
}
