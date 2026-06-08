program PrefixSum;

const
  MAXN = 100000;

var
  n, q, l, r, i: integer;
  a, pref: array[1.MAXN] of int64;

begin
  ReadLn(n);
  for i := 1 to n do
    Read(a[i]);
  ReadLn;
  pref[1] := a[1];
  for i := 2 to n do
    pref[i] := pref[i - 1] + a[i];
  ReadLn(q);
  for i := 1 to q do
  begin
    ReadLn(l, r);
    if l = 1 then
      WriteLn(pref[r])
    else
      WriteLn(pref[r] - pref[l - 1]);
  end;
end.
