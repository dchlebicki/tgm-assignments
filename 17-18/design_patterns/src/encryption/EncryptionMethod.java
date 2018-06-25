package encryption;

/**
 * EncryptionMethod is the parent class for new implementations of
 */
public abstract class EncryptionMethod extends EncryptionSubject {

    protected EncryptionSubject component;

    public EncryptionMethod(EncryptionSubject es) {
        super(es.getEncrypted());
        this.component = es;
    }
}
