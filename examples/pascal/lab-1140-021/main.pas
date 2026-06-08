program Vowels;

var
  s: string;
  i: integer;
  vowels: set of char;

begin
  vowels := ['a', 'e', 'i', 'o', 'u', 'y',
             'A', 'E', 'I', 'O', 'U', 'Y'];
  ReadLn(s);
  for i := 1 to Length(s) do
    if s[i] in vowels then
      Write(s[i]);
  WriteLn;
end.
