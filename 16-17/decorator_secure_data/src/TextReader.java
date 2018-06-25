import java.io.BufferedReader;
import java.io.InputStreamReader;

public abstract class TextReader {
	protected BufferedReader in=new BufferedReader(new InputStreamReader(System.in));
	void write(String[] s) {}
	void read(String[] s) {}
}