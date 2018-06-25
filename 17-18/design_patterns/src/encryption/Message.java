package encryption;

/**
 * Concrete EncryptionSubject Message, holds a String, does nothing more.
 */
public class Message extends EncryptionSubject {

    public Message(String text) {
        super(text);
    }
}
