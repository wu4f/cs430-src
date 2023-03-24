package ch.hegarc.guestbook.models;
import ch.hegarc.guestbook.models.Entry;
import java.util.ArrayList;
import java.util.List;

public class Guestbook {
    public List<Entry> select() {
        List<Entry> entries = new ArrayList<>();
        entries.add(new Entry("John", "test@email", "message"));
        return entries;
    }

    public void insert(Entry entry) {
        // TODO
    }
}
