program Fibonacci;

var
  n, i: integer;
  a, b, c: int64;

begin
  ReadLn(n);
  if n <= 0 then
    WriteLn(0)
  else if n <= 2 then
    WriteLn(1)
  else
  begin
    a := 1;
    b := 1;
    for i := 3 to n do
    begin
      c := a + b;
      a := b;
      b := c;
    end;
    WriteLn(b);
  end;
end.
