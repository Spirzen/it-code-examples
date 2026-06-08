program CountPositive;

var
  n, i, x, cnt: integer;

begin
  ReadLn(n);
  cnt := 0;
  for i := 1 to n do
  begin
    Read(x);
    if x > 0 then
      cnt := cnt + 1;
  end;
  ReadLn;
  WriteLn(cnt);
end.
