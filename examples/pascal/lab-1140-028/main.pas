program CountDigits;

var
  n: int64;
  cnt: integer;

begin
  ReadLn(n);
  if n = 0 then
    WriteLn(1)
  else
  begin
    cnt := 0;
    while n > 0 do
    begin
      cnt := cnt + 1;
      n := n div 10;
    end;
    WriteLn(cnt);
  end;
end.
