module shape_mod
  implicit none

  type :: shape
  contains
    procedure :: area => shape_area
  end type shape

contains

  real function shape_area(this)
    class(shape), intent(in) :: this
    shape_area = 0.0
  end function shape_area

end module shape_mod
