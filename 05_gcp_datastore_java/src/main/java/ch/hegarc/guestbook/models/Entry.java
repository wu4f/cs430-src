package ch.hegarc.guestbook.models;

import java.time.LocalDateTime;
import java.util.Objects;

public class Entry {
    private String name;
    private String email;
    private String message;
    private LocalDateTime signedOn;

    public Entry(String name, String email, String message) {
        this.name = Objects.requireNonNull(name, "name must not be null");
        this.email = Objects.requireNonNull(email, "email must not be null");
        this.message = Objects.requireNonNull(message, "message must not be null");
        this.signedOn = LocalDateTime.now();
    }

    public String getName() {
        return name;
    }

    public String getEmail() {
        return email;
    }

    public String getMessage() {
        return message;
    }

    public LocalDateTime getSignedOn() {
        return signedOn;
    }

    public String getSignedOnFormatted() {
        "%d.%m.%Y at %H:%M"
        return "";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Entry)) return false;
        Entry entry = (Entry) o;
        return name.equals(entry.name) &&
                email.equals(entry.email) &&
                message.equals(entry.message) &&
                signedOn.equals(entry.signedOn);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, email, message, signedOn);
    }

    @Override
    public String toString() {
        return "Entry{" +
                "name='" + name + '\'' +
                ", email='" + email + '\'' +
                ", message='" + message + '\'' +
                ", signedOn=" + signedOn +
                '}';
    }
}
