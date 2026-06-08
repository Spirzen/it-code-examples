class DataModel {
    let identifier: UUID
    
    required init() {
        self.identifier = UUID()
    }
    
    init(identifier: UUID) {
        self.identifier = identifier
    }
}

class UserAccount: DataModel {
    var username: String
    
    required init() {
        self.username = "guest"
        super.init()
    }
    
    init(username: String) {
        self.username = username
        super.init()
    }
}

class AdminAccount: UserAccount {
    var privileges: [String]
    
    required init() {
        self.privileges = ["read", "write", "delete"]
        super.init()
    }
    
    init(username: String, privileges: [String]) {
        self.privileges = privileges
        super.init(username: username)
    }
}
