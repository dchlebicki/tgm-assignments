import java.io.IOException;

/**
 * Created by Dominik on 20.03.2017.
 */
public class Authentication extends Decorator {
    String password = "";
    String passwordTry = "";
    public Authentication(TextReader textReader) {
        super(textReader);
    }

    public void write(String[] s){
        System.out.println("PASSWORD: ");
        try {
            password = in.readLine();
        } catch (IOException e){
            e.printStackTrace();
        }
        super.write(s);
    }

    public void read(String[] s){
        System.out.println("PASSWORD: ");
        while(true) {
            try {
                passwordTry = in.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            if (password.equals(passwordTry)) {
                super.read(s);
                break;
            } else {
                System.out.println("Wrong password, try again");
            }
        }
    }
}
