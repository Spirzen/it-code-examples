
import "github.com/go-playground/validator/v10"

type CustomValidator struct{ v *validator.Validate }

func (cv *CustomValidator) Validate(i interface{}) error {
    return cv.v.Struct(i)
}

func main() {
    e := echo.New()
    e.Validator = &CustomValidator{validator.New()}
    e.Use(middleware.Validator())
    // ...
}
