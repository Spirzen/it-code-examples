module vector_ops
    implicit none
    private
    public :: vec_dot

    interface vec_dot
        module procedure dot_real, dot_complex
    end interface

contains

    real function dot_real(a, b)
        real, intent(in) :: a(:), b(:)
        dot_real = sum(a * b)
    end function dot_real

    complex function dot_complex(a, b)
        complex, intent(in) :: a(:), b(:)
        dot_complex = sum(conjg(a) * b)
    end function dot_complex

end module vector_ops
