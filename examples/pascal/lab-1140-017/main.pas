program Gcd;

function Gcd(a, b: integer): integer;
var
  t: integer;
begin
  while b <> 0 do
  begin
    t := a mod b;
    a := b;
    b := t;
  end;
  Gcd := a;
end;

var
  x, y: integer;

begin
  ReadLn(x, y);
  WriteLn(Gcd(x, y));
end.
