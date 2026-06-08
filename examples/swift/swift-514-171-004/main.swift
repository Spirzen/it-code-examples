func parseAgeResult(from text: String) -> Result<Int, ParseError> {
    do {
        return .success(try parseAge(from: text))
    } catch let error as ParseError {
        return .failure(error)
    } catch {
        return .failure(.notANumber(text))
    }
}

switch parseAgeResult(from: "17") {
case .success(let age):
    print(age)
case .failure(let error):
    print(error.localizedDescription)
}
