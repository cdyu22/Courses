uses sysutils;
function q(var a: integer; b : integer; var c : integer):real;
  begin
    c:=a+b+c;
    a:=2*c;
    b:=b*4;
    q:=a/b;
  end;

var
  x, y, z : integer;
  i : real;
begin
  writeln('Enter three integers: ');
  x := 3;
  y := 4;
  z := 5;
  i := q(x, y, z);
  writeln('result: ', x, ' ', y, ' ', z, ' ', i);
end.
