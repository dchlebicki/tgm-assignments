package encryption;

/**
 * Offset Encryption, simply offsetting every char.
 */
public class OffsetEncryption extends EncryptionMethod {

    // key used as offset
    private int key;

    // constructor gets EncryptionSubject and key/offset
    public OffsetEncryption(EncryptionSubject mc, int key) {
        super(mc);
        this.key = key;
    }

    /**
     * Simple offset encryption method
     * @return the encrypted text
     */
    public String getEncrypted() {
        //get text from wrapped class
        String text = this.component.getEncrypted();
        //turn into char array so you can manipulate every char by its own
        char[] charArray = text.toCharArray();

        //iterate through array and add offset to encrypt
        for (int i = 0 ; i < charArray.length ; i++) {
            charArray[i] += key;
        }
        //put together chars to create String
        text = String.valueOf(charArray);
        return text;
    }

    /**
     * Simple offset decryption method
     * @return the decrypted text
     */
    public String getDecrypted() {
        //see getEncrypted() method for guidance
        String text = this.component.getDecrypted();
        char[] charArray = text.toCharArray();

        //the only difference from the encrypt method is the negative offset
        //to get the decrypted text
        for (int i = 0 ; i < charArray.length ; i++) {
            charArray[i] -= key;
        }
        return text;
    }


}
