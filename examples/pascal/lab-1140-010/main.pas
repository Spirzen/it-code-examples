program IsPrime;

function IsPrime(x: integer): boolean;
var
  d: integer;
begin
  if x < 2 then
  begin
    IsPrime := false;
    exit;
  end;
  IsPrime := true;
  for d := 2 to trunc(sqrt(x)) do
    if x mod d = 0 then
    begin
      IsPrime := false;
      exit;
    end;
end;

var
  n: integer;

begin
  ReadLn(n);
  if IsPrime(n) then
    WriteLn('YES')
  else
    WriteLn('NO');
end.
