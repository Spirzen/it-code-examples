using System;
using System.Security.Cryptography;

var prng = new Random(42);
Console.WriteLine(prng.Next(1, 11));

Span<byte> bytes = stackalloc byte[16];
RandomNumberGenerator.Fill(bytes);
Console.WriteLine(Convert.ToHexString(bytes));
