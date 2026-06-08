  @ServerEndpoint("/chat/{room}")
  public class ChatEndpoint {
      @OnOpen
      public void onOpen(Session session, @PathParam("room") String room) {
          // добавить клиента в комнату
      }

      @OnMessage
      public void onMessage(String message, Session session) {
          // рассылка всем в комнате
      }

      @OnClose
      public void onClose(Session session) { /* ... */ }

      @OnError
      public void onError(Throwable error, Session session) { /* ... */ }
  }
