program WordCount;

var
  s: string;
  i, cnt: integer;
  inWord: boolean;

begin
  ReadLn(s);
  cnt := 0;
  inWord := false;
  for i := 1 to Length(s) do
  begin
    if s[i] <> ' ' then
    begin
      if not inWord then
      begin
        cnt := cnt + 1;
        inWord := true;
      end;
    end
    else
      inWord := false;
  end;
  WriteLn(cnt);
end.
