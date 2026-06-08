program Palindrome;

var
  s: string;
  i, n: integer;
  ok: boolean;

begin
  ReadLn(s);
  n := Length(s);
  ok := true;
  for i := 1 to n div 2 do
    if s[i] <> s[n - i + 1] then
      ok := false;
  if ok then
    WriteLn('YES')
  else
    WriteLn('NO');
end.
