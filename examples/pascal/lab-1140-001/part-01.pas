program ArraySum;

var
  n, i: integer;
  sum: int64;
  x: integer;

begin
  ReadLn(n);
  sum := 0;
  for i := 1 to n do
  begin
    Read(x);
    sum := sum + x;
  end;
  ReadLn;
  WriteLn(sum);
end.
