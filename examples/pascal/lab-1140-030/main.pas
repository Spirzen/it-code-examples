program ArrayMin;

var
  n, i, x, minVal: integer;

begin
  ReadLn(n);
  Read(minVal);
  for i := 2 to n do
  begin
    Read(x);
    if x < minVal then
      minVal := x;
  end;
  ReadLn;
  WriteLn(minVal);
end.
