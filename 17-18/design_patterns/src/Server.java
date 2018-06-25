import encryption.AESEncryption;
import encryption.EncryptionSubject;
import encryption.Message;
import encryption.OffsetEncryption;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * Server class
 * At the moment the server can only have one connection at a time
 * Client sends text in plain text, server encrypts it and "echoes" it back to the client.
**/
public class Server {
    public static void main(String[] args) {
        //specifying port number
        //String portNumber = args[0];
        int portNumber = 50000;

        while(true) {
            try (
                //create serversocket with portnumber
                ServerSocket serverSocket = new ServerSocket(portNumber);
                //wait until client connects and accept message
                Socket clientSocket = serverSocket.accept();
                //create printwriter to client socket
                PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
                //create bufferedreader to read from client socket
                BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            ) {
                String inputLine, outputLine;

                //while block will be executed as long as the client response is not empty
                while ((inputLine = in.readLine()) != null) {
                    //create encryption object with AES and offset encryption
                    EncryptionSubject es = new AESEncryption(new OffsetEncryption(new Message(inputLine), 3), "16 byte string  ");
                    //write encrypted message to temporary variable
                    outputLine = es.getEncrypted();
                    //print to server console
                    System.out.println(inputLine + " > " + outputLine);
                    //and send to client
                    out.println(outputLine);
                }

            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
