program ArraySum2;

const
  MAXN = 100000;

var
  n, i: integer;
  a: array[1.MAXN] of integer;
  sum: int64;

begin
  ReadLn(n);
  for i := 1 to n do
    Read(a[i]);
  ReadLn;
  sum := 0;
  for i := 1 to n do
    sum := sum + a[i];
  WriteLn(sum);
end.
