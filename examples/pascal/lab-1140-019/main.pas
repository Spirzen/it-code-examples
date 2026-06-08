program ModPow;

function ModPow(a, n, modul: int64): int64;
var
  res: int64;
begin
  res := 1;
  a := a mod modul;
  while n > 0 do
  begin
    if n mod 2 = 1 then
      res := (res * a) mod modul;
    a := (a * a) mod modul;
    n := n div 2;
  end;
  ModPow := res;
end;

var
  a, n, m: integer;

begin
  ReadLn(a, n, m);
  WriteLn(ModPow(a, n, m));
end.
