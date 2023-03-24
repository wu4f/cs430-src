package ch.hegarc.guestbook;

import com.google.cloud.firestore.Firestore;
import com.google.cloud.firestore.FirestoreOptions;

public class Persistence {
    private static Firestore firestore;

    public static Firestore getFirestore() {
        if (firestore == null) {
            Firestore db =
                    FirestoreOptions.getDefaultInstance()
                            .toBuilder()
                            .build().getService();
            firestore = db;
        }

        return firestore;
    }

    public static void setFirestore(Firestore firestore) {
        Persistence.firestore = firestore;
    }
}
