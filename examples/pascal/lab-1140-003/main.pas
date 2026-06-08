program LineMax;

var
  maxVal, x: integer;
  first: boolean;

begin
  first := true;
  while not Eof do
  begin
    Read(x);
    if first then
    begin
      maxVal := x;
      first := false;
    end
    else if x > maxVal then
      maxVal := x;
  end;
  ReadLn;
  WriteLn(maxVal);
end.
