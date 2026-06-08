program ArrayMax;

var
  n, i, x, maxVal: integer;

begin
  ReadLn(n);
  Read(maxVal);
  for i := 2 to n do
  begin
    Read(x);
    if x > maxVal then
      maxVal := x;
  end;
  ReadLn;
  WriteLn(maxVal);
end.
