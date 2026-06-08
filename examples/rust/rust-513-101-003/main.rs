struct Container {
    data: Vec<i32>,
}

impl Container {
    // Возврат владения
    fn extract_data(self) -> Vec<i32> {
        self.data
    }
    
    // Возврат ссылки с жизненным циклом
    fn get_data(&self) -> &Vec<i32> {
        &self.data
    }
}
