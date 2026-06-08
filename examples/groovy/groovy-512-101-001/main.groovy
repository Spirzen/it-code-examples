class User {
    String firstName
    String lastName
    String email
    Date registrationDate = new Date()
    
    String getFullName() {
        "$firstName $lastName"
    }
    
    boolean isActive() {
        registrationDate > Date.parse('yyyy-MM-dd', '2020-01-01')
    }
}
