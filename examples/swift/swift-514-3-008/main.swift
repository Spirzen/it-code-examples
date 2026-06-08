
import XCTest

@testable import MyApp

class UserManagerTests: XCTestCase {
    func testUserCreation() {
        let user = User(name: "Alice", age: 30)
        XCTAssertEqual(user.name, "Alice")
        XCTAssertTrue(user.isActive)
    }

    func testInvalidAgeThrowsError() throws {
        XCTAssertThrowsError(try User(name: "Bob", age: -5)) { error in
            XCTAssertEqual(error as? UserError, .invalidAge)
        }
    }
}
