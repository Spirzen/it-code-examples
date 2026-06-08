program FibSequence;

var
  n, i: integer;
  a, b, nextVal: int64;

begin
  ReadLn(n);
  a := 1;
  b := 1;
  for i := 1 to n do
  begin
    if i > 1 then
      Write(' ');
    if i = 1 then
      Write(a)
    else if i = 2 then
      Write(b)
    else
    begin
      nextVal := a + b;
      Write(nextVal);
      a := b;
      b := nextVal;
    end;
  end;
  WriteLn;
end.
