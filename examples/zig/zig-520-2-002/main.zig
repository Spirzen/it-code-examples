const std = @import("std");

const FileError = error{
    FileNotFound,
    AccessDenied,
};

fn openFile(path: []const u8) FileError!void {
    if (std.mem.eql(u8, path, "/forbidden")) return error.AccessDenied;
    if (std.mem.eql(u8, path, "/missing")) return error.FileNotFound;
}

pub fn main() void {
    openFile("/forbidden") catch |err| switch (err) {
        error.AccessDenied => std.debug.print("Доступ запрещён\n", .{}),
        error.FileNotFound => std.debug.print("Файл не найден\n", .{}),
    };

    openFile("/data.txt") catch |err| {
        switch (err) {
            error.AccessDenied => std.debug.print("Доступ запрещён\n", .{}),
            error.FileNotFound => std.debug.print("Файл не найден\n", .{}),
        }
        return;
    };
    std.debug.print("Файл открыт\n", .{});
}
