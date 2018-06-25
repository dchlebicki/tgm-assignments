/**
 * Decorator parent class
 */
public abstract class Decorator extends TextReader {
    private TextReader textReader;
    public Decorator(TextReader textReader) {
        this.textReader = textReader;
    }

    void write(String[] s) {
        textReader.write(s);
    }

    void read(String[] s) {
        textReader.read(s);
    }
}
