import java.util.ArrayList;
import java.util.List;

interface ChatRoom {
    void sendMessage(String message, User sender);
    void addUser(User user);
}

class GroupChatRoom implements ChatRoom {
    private final List<User> users = new ArrayList<>();

    @Override
    public void addUser(User user) {
        users.add(user);
        user.setChatRoom(this);
    }

    @Override
    public void sendMessage(String message, User sender) {
        users.stream()
            .filter(u -> u != sender)
            .forEach(u -> u.receive(message, sender.getName()));
    }
}

class User {
    private final String name;
    private ChatRoom chatRoom;

    User(String name) {
        this.name = name;
    }

    void setChatRoom(ChatRoom room) {
        this.chatRoom = room;
    }

    void send(String message) {
        chatRoom.sendMessage(message, this);
    }

    void receive(String message, String from) {
        System.out.println(name + " получил от " + from + ": " + message);
    }

    String getName() {
        return name;
    }
}
