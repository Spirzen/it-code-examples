const std = @import("std");

pub fn sortFile(allocator: std.mem.Allocator, path: []const u8) !void {
    const data = try std.fs.cwd().readFileAlloc(allocator, path, 1024 * 1024);
    defer allocator.free(data);
    var list = std.ArrayList([]const u8).init(allocator);
    defer list.deinit();
    var it = std.mem.splitScalar(u8, data, '\n');
    while (it.next()) |line| {
        const t = std.mem.trim(u8, line, " \r");
        if (t.len > 0) try list.append(t);
    }
    std.sort.pdq([]const u8, list.items, {}, struct {
        fn lessThan(_: void, a: []const u8, b: []const u8) bool {
            return std.mem.order(a, b) == .lt;
        }
    }.lessThan);
}
