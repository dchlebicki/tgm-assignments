package encryption;

public abstract class EncryptionSubject {
    protected String text;

    public EncryptionSubject(String text) {
        this.text = text;
    }

    public String getEncrypted() {
        return text;
    }

    public String getDecrypted() {
        return text;
    }
}