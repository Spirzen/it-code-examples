program SwapDemo;

procedure Swap(var a, b: integer);
var
  t: integer;
begin
  t := a;
  a := b;
  b := t;
end;

var
  x, y: integer;

begin
  ReadLn(x, y);
  Swap(x, y);
  WriteLn(x, ' ', y);
end.
