const std = @import("std");

const ParsedNumber = union(enum) {
    integer: i64,
    floating: f64,
};

fn parseNumber(input: []const u8) !ParsedNumber {
    if (std.fmt.parseInt(i64, input, 10)) |int_val| {
        return ParsedNumber{ .integer = int_val };
    } else |_| {
        if (std.fmt.parseFloat(f64, input)) |float_val| {
            return ParsedNumber{ .floating = float_val };
        } else |_| {
            return error.InvalidNumber;
        }
    }
}

// Использование
const result = try parseNumber("3.14");
switch (result) {
    .integer => |n| std.debug.print("Целое: {}\n", .{n}),
    .floating => |f| std.debug.print("Дробное: {:.2}\n", .{f}),
}
