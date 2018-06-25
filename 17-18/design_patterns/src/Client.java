import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;

/**
 * Client class
 * Simply send messages to the specified server, receives the responses and prints them to the screen.
 */
public class Client {
    public static void main(String[] args) {

        //specifying connection details
        String hostname = "localhost";
        //String portNumber = args[0];
        int portNumber = 50000;

        try {
            //create socket with hostname and portnumber
            Socket cryptoEchoSocket = new Socket(hostname, portNumber);
            //create printwriter to send messages to server
            PrintWriter out = new PrintWriter(cryptoEchoSocket.getOutputStream(), true);
            //create bufferedreader to receive messages from the server
            BufferedReader in = new BufferedReader(new InputStreamReader(cryptoEchoSocket.getInputStream()));
            //buffered inputstreamreader to get stdIn input
            BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in));

            String userInput;
            System.out.print("user@masterencryptor~$");
            //as long as readLine() is not empty the while block will send, receive and print messages
            while ((userInput = stdIn.readLine()) != null) {
                out.println(userInput);
                System.out.println(in.readLine());
                System.out.print("user@masterencryptor~$");
            }

        } catch (UnknownHostException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

