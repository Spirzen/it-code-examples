program ReadFromFile;

var
  f: text;
  x: integer;
  sum: int64;

begin
  Assign(f, 'input.txt');
  Reset(f);
  sum := 0;
  while not Eof(f) do
  begin
    Read(f, x);
    sum := sum + x;
  end;
  Close(f);
  WriteLn(sum);
end.
