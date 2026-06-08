program FactRec;

function Fact(n: integer): int64;
begin
  if n <= 1 then
    Fact := 1
  else
    Fact := n * Fact(n - 1);
end;

var
  n: integer;

begin
  ReadLn(n);
  WriteLn(Fact(n));
end.
