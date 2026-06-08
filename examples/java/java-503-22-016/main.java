
import jakarta.persistence.*;

import java.util.List;
import java.util.Optional;

public class JpaBookRepository {

    private final EntityManagerFactory emf;

    public JpaBookRepository(EntityManagerFactory emf) {
        this.emf = emf;
    }

    public Book save(Book book) {
        EntityManager em = emf.createEntityManager();
        EntityTransaction tx = null;
        try {
            tx = em.getTransaction();
            tx.begin();
            Book saved = em.merge(book); // persist для новых, merge — для detached
            tx.commit();
            return saved;
        } catch (Exception e) {
            if (tx != null && tx.isActive()) {
                tx.rollback();
            }
            throw new RuntimeException("Ошибка при сохранении книги", e);
        } finally {
            em.close();
        }
    }

    public Optional<Book> findById(Long id) {
        EntityManager em = emf.createEntityManager();
        try {
            return Optional.ofNullable(em.find(Book.class, id));
        } finally {
            em.close();
        }
    }

    @SuppressWarnings("unchecked")
    public List<Book> findAllAvailable() {
        EntityManager em = emf.createEntityManager();
        try {
            return em.createQuery(
                "SELECT b FROM Book b WHERE b.available = true", Book.class)
                .getResultList();
        } finally {
            em.close();
        }
    }

    public List<Book> findByAuthorAndYear(String author, int year) {
        EntityManager em = emf.createEntityManager();
        try {
            TypedQuery<Book> query = em.createQuery(
                "SELECT b FROM Book b WHERE b.author = :author AND b.publishedYear = :year", Book.class);
            query.setParameter("author", author);
            query.setParameter("year", year);
            return query.getResultList();
        } finally {
            em.close();
        }
    }

    public void delete(Book book) {
        EntityManager em = emf.createEntityManager();
        EntityTransaction tx = null;
        try {
            tx = em.getTransaction();
            tx.begin();
            em.remove(em.contains(book) ? book : em.merge(book));
            tx.commit();
        } catch (Exception e) {
            if (tx != null && tx.isActive()) {
                tx.rollback();
            }
            throw new RuntimeException("Ошибка при удалении книги", e);
        } finally {
            em.close();
        }
    }
}
