const std = @import("std");
const random = std.crypto.random;

pub fn generatePassword(allocator: std.mem.Allocator, len: usize) ![]u8 {
    const charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    var buf = try allocator.alloc(u8, len);
    for (buf) |*c| {
        c.* = charset[random.intRangeAtMost(usize, 0, charset.len - 1)];
    }
    return buf;
}

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const pass = try generatePassword(gpa.allocator(), 16);
    defer gpa.allocator().free(pass);
    std.debug.print("{s}\n", .{pass});
}
