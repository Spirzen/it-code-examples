!> @brief Краткое описание модуля
!! Подробное описание назначения, зависимостей, примеров использования
module example_mod
  implicit none
  private

  ! Публичные типы
  type, public :: data_container
    real, allocatable :: values(:)
    integer :: n = 0
  end type data_container

  ! Публичные процедуры
  public :: load_data, process_data

contains

  subroutine load_data(...)
    ! реализация
  end subroutine load_data

  function process_data(...) result(out)
    ! реализация
  end function process_data

end module example_mod
