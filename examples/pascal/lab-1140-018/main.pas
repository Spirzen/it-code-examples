program Sieve;

const
  MAXN = 1000000;

var
  n, i, j: integer;
  isPrime: array[1.MAXN] of boolean;

begin
  ReadLn(n);
  for i := 1 to n do
    isPrime[i] := true;
  isPrime[1] := false;
  for i := 2 to trunc(sqrt(n)) do
    if isPrime[i] then
      for j := i * i to n do
        isPrime[j] := false;
  for i := 2 to n do
    if isPrime[i] then
      Write(i, ' ');
  WriteLn;
end.
