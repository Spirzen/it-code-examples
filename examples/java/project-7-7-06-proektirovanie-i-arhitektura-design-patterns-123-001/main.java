import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.function.Function;

public class PaginatedIterator<T> implements Iterator<T> {
    private final Function<Integer, List<T>> pageFetcher;
    private final int pageSize;
    private List<T> currentPage;
    private int pageIndex = 0;
    private int itemIndex = 0;

    public PaginatedIterator(Function<Integer, List<T>> pageFetcher, int pageSize) {
        this.pageFetcher = pageFetcher;
        this.pageSize = pageSize;
        this.currentPage = pageFetcher.apply(0);
    }

    @Override
    public boolean hasNext() {
        if (itemIndex < currentPage.size()) {
            return true;
        }
        if (currentPage.size() < pageSize) {
            return false;
        }
        pageIndex++;
        currentPage = pageFetcher.apply(pageIndex);
        itemIndex = 0;
        return !currentPage.isEmpty();
    }

    @Override
    public T next() {
        if (!hasNext()) {
            throw new NoSuchElementException();
        }
        return currentPage.get(itemIndex++);
    }
}
