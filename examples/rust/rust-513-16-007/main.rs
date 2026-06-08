use validator::{Validate, ValidationError};

#[derive(Deserialize, Validate)]
pub struct CreateUserRequest {
    #[validate(length(min = 2, max = 50))]
    pub name: String,

    #[validate(email)]
    pub email: String,
}

// В обработчике
let request: CreateUserRequest = serde_json::from_str(body)?;
request.validate()?;
