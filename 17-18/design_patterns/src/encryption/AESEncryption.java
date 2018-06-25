package encryption;

import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

/**
 * AES en- and decryption
 */
public class AESEncryption extends EncryptionMethod {
    private String key;

    /**
     * Default constructor
     * @param mc    the encryption subject
     * @param key   the key as a 16/32/64/... byte string
     */
    public AESEncryption(EncryptionSubject mc, String key) {
        super(mc);
        this.key = key;
    }

    /**
     * Decrypts the text using the AES encryption algorithm
     * @return the encrypted text
     */
    public String getEncrypted() {
        //get text from super class
        String text = this.component.getEncrypted();

        try {
            //create secret key spec with key and algorithm
            SecretKeySpec secretKeySpec = new SecretKeySpec(this.key.getBytes(), "AES");
            //get AES cypther instance
            Cipher cipher = Cipher.getInstance("AES");
            //set to encryption mode
            cipher.init(Cipher.ENCRYPT_MODE, secretKeySpec);
            //do encryption
            byte[] encrypted = cipher.doFinal(text.getBytes());
            text = new String(encrypted);

        } catch (Exception e) {
            e.printStackTrace();
            System.out.println("Encryption Error!");
        }
        return text;
    }

    /**
     * Decrypts the text using the AES decryption algorithm
     * @return the decrypted text
     */
    public String getDecrypted() {
        //see getEncrypted() method for guidance
        String text = this.component.getDecrypted();

        try {
            SecretKeySpec secretKeySpec = new SecretKeySpec(this.key.getBytes(), "AES");
            Cipher cipher = Cipher.getInstance("AES");
            //only difference is the use of DECRYPT_MODE
            cipher.init(Cipher.DECRYPT_MODE, secretKeySpec);
            byte[] decrypted = cipher.doFinal(text.getBytes());
            text = new String(decrypted);

        } catch (Exception e) {
            e.printStackTrace();
            System.out.println("Encryption Error!");
        }
        return text;
    }
}
