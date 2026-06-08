program Project1;

{$mode objfpc}{$H+}

uses
  Classes, SysUtils;

var
  Name: string;
begin
  Write('Введите имя: ');
  ReadLn(Name);
  WriteLn('Hello, ', Name, '!');
  ReadLn;
end.
