{ FPC / Lazarus }
program GreetUser;

var
  Name: string;
  Age: integer;

begin
  WriteLn('Введите ваше имя:');
  ReadLn(Name);
  WriteLn('Введите ваш возраст:');
  ReadLn(Age);
  WriteLn('Здравствуйте, ', Name, '!');
  WriteLn('Вам ', Age, ' лет.');
end.
