struct UserProfileView: View {
    @State private var user: User?

    var body: some View {
        VStack {
            if let user {
                Text(user.name)
            }
        }
        .task {
            user = await fetchCurrentUser()
        }
    }
}
