use sea_orm::{EntityTrait, ModelTrait, QueryFilter, DatabaseConnection};

#[derive(Clone, Debug, PartialEq, DeriveEntityModel)]
#[sea_orm(table_name = "users")]
pub struct Model {
    #[sea_orm(primary_key)]
    pub id: i32,
    pub name: String,
    pub email: String,
}

#[derive(Copy, Clone, Debug, EnumIter, DeriveRelation)]
pub enum Relation {}

impl ActiveModelBehavior for ActiveModel {}

// Использование
async fn find_user_by_email(db: &DatabaseConnection, email: &str) -> Result<Option<Model>, DbErr> {
    Entity::find()
        .filter(Column::Email.eq(email))
        .one(db)
        .await
}
