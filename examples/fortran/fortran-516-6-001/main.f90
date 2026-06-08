program main
    real :: a = 3.0, b = 4.0, hypot

    hypot = sqrt(square(a) + square(b))

    print *, 'Гипотенуза:', hypot

contains

    real function square(x)
        real, intent(in) :: x
        square = x * x
    end function square

end program main
