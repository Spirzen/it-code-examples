program BinarySearch;

function Find(a: array of integer; n, key: integer): integer;
var
  lo, hi, mid: integer;
begin
  lo := 0;
  hi := n - 1;
  while lo <= hi do
  begin
    mid := (lo + hi) div 2;
    if a[mid] = key then
    begin
      Find := mid;
      exit;
    end;
    if a[mid] < key then
      lo := mid + 1
    else
      hi := mid - 1;
  end;
  Find := -1;
end;

var
  n, i, key, pos: integer;
  a: array of integer;

begin
  ReadLn(n);
  SetLength(a, n);
  for i := 0 to n - 1 do
    Read(a[i]);
  ReadLn;
  ReadLn(key);
  pos := Find(a, n, key);
  WriteLn(pos);
end.
