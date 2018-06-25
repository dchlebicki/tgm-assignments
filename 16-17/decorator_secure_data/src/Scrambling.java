/**
 * Created by Dominik on 20.03.2017.
 */
public class Scrambling extends Decorator {

    public Scrambling(TextReader textReader) {
        super(textReader);
    }

    public void write(String[] s) {
        super.write(s);
        System.out.println("encrypt: ");
        StringBuffer sb = new StringBuffer(s[0]);
        for (int i = 0; i < sb.length(); i++) {
            sb.setCharAt(i, (char) (sb.charAt(i) - 5));
        }
        s[0] = sb.toString();
    }

    public void read(String[] s) {
        StringBuffer sb = new StringBuffer(s[0]);
        for (int i = 0; i < sb.length(); i++) {
            sb.setCharAt(i, (char) (sb.charAt(i) + 5));
        }
        s[0] = sb.toString();
        System.out.println("decrypt: ");
        super.read(s);
    }

}
