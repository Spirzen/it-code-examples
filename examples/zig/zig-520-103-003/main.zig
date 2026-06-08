const std = @import("std");

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    const args = try std.process.argsAlloc(allocator);
    defer std.process.argsFree(allocator, args);

    if (args.len < 3) {
        std.debug.print("Использование: zig run calc.zig -- 10 20 30\n", .{});
        return;
    }

    var total: i64 = 0;
    for (args[1..]) |raw| {
        total += try std.fmt.parseInt(i64, raw, 10);
    }

    std.debug.print("Сумма: {}\n", .{total});
}
