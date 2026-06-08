import java.util.HashMap;
import java.util.Map;
import java.util.Set;

interface DocumentService {
    String loadDocument(String docId);
}

class RealDocumentService implements DocumentService {
    @Override
    public String loadDocument(String docId) {
        System.out.println("Загрузка из хранилища: " + docId);
        return "Содержимое документа " + docId;
    }
}

final class SecurityContext {
    private static final ThreadLocal<String> currentRole = new ThreadLocal<>();

    static void setCurrentRole(String role) {
        currentRole.set(role);
    }

    static String getCurrentRole() {
        return currentRole.get();
    }
}

class DocumentServiceProxy implements DocumentService {
    private final RealDocumentService realService = new RealDocumentService();
    private final Map<String, String> cache = new HashMap<>();
    private final Set<String> allowedRoles;

    DocumentServiceProxy(Set<String> allowedRoles) {
        this.allowedRoles = allowedRoles;
    }

    @Override
    public String loadDocument(String docId) {
        String role = SecurityContext.getCurrentRole();
        if (!allowedRoles.contains(role)) {
            throw new SecurityException("Нет доступа");
        }
        return cache.computeIfAbsent(docId, realService::loadDocument);
    }
}
