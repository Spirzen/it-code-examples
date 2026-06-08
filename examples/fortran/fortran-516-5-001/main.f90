integer :: sign_code
if (x < 0.0) then
   sign_code = -1
else if (x == 0.0) then
   sign_code = 0
else
   sign_code = 1
end if

select case (sign_code)
case (-1)
   print *, 'negative'
case (0)
   print *, 'zero'
case (1)
   print *, 'positive'
end select
