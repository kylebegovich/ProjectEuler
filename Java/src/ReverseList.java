import java.util.LinkedList;
import java.util.Collection;

/**
 * A class that adds a reversal method to the existing LinkedList class.
 * This class extends LinkedList<T> and needs to provide an empty constructor,
 * a constructor that takes a collection,
 * and a reverse() method that returns a reversed copy of the list.
 */
public class ReverseList<T> extends LinkedList<T> {
    /**a constructor without parameters. */
    public ReverseList() {
        super();
    }

    /**a constructor with parameters.
     *
     * @param collection the collection to create the ReverseLinkedList from.
     */
    public ReverseList(final Collection<? extends T> collection) {
        super(collection);
    }

    /**
     * Recursive implementation of linked list reversal.
     *
     * @param <E> the type of the list
     * @param list the list to reverse, required for a recursive call
     * @return a reversed copy of the list
     */
    private static <E> LinkedList<E> recursiveReverse(final LinkedList<E> list) {
        if (list.size() == 1 || list.size() == 0) {
            return list;
        }
        E item = list.pollFirst();
        recursiveReverse(list).addLast(item);
        return list;
    }
}
