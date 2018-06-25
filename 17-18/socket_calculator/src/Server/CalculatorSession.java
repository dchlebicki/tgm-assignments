package Server;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Arrays;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.ConcurrentHashMap;

/**
 * Created by Dominik on 02.02.2018.
 */
public class CalculatorSession implements Runnable {

    private Socket clientSocket;
    private BlockingQueue queue;
    private ConcurrentHashMap credits;
    private int sessionID;

    public CalculatorSession(Socket clientSocket, BlockingQueue queue, ConcurrentHashMap<Integer, Integer> credits, int sessionID) {
        this.clientSocket = clientSocket;
        this.queue = queue;
        this.credits = credits;
        this.sessionID = sessionID;
    }

    @Override
    public void run() {
        try (
                //create printwriter to client socket
                PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
                //create bufferedreader to read from client socket
                BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
        ) {
            queue.put("Session " + sessionID + " started.");

            String inputLine, outputLine;
            double result;

            //while block will be executed as long as the client response is not empty
            while ((inputLine = in.readLine()) != null) {
                // format: <command> <z1> (<z2>)
                String[] segments = inputLine.split(" ");

                if((Integer) credits.get(sessionID) > 0 || segments[0].equals("!exit") || segments[0].equals("!buy")) {
                    if (inputLine.equals("!exit")) {
                        outputLine = "Session " + sessionID + " closed the connection.";
                        out.println("Bye!");
                        queue.put(outputLine);

                        clientSocket.close();
                        Thread.currentThread().interrupt();
                        return;

                    } else if (segments[0].equals("!add") && segments.length == 3 && isNumeric(segments[1]) && isNumeric(segments[2])) {
                        result = Double.parseDouble(segments[1]) + Double.parseDouble(segments[2]);
                        outputLine = segments[1] + " + " + segments[2] + " = " + result;
                        decreaseCredits(1);
                        out.println(outputLine + ", " + credits.get(sessionID) + " credit(s) left.");
                        queue.put("Session " + sessionID + ": " + outputLine);

                    } else if (segments[0].equals("!subtract") && segments.length == 3 && isNumeric(segments[1]) && isNumeric(segments[2])) {
                        result = Double.parseDouble(segments[1]) - Double.parseDouble(segments[2]);
                        outputLine = segments[1] + " - " + segments[2] + " = " + result;
                        decreaseCredits(1);
                        out.println(outputLine + ", " + credits.get(sessionID) + " credit(s) left.");
                        queue.put("Session " + sessionID + ": " + outputLine);

                    } else if (segments[0].equals("!buy") && segments.length == 2 && isNumeric(segments[1])) {
                        //ugly, but
                        if((int) Double.parseDouble(segments[1]) > 0) {
                            increaseCredits(Integer.parseInt(segments[1]));
                            out.println(segments[1] + " credits have been added to your balance, you now have " + credits.get(sessionID) + " credit(s)");
                            queue.put("Session " + sessionID + " bought " + segments[1] + " credits.");
                        } else {
                            queue.put("Session " + sessionID + " tried buying a negative amount of credits: " + segments[1]);
                            out.println("The amout of credits can't be negative");
                        }
                    } else {
                        out.println("Unrecognized command, try again");
                        queue.put("Session " + sessionID + ": unrecognized command '" + inputLine + "'");
                    }
                } else {
                    out.println("You have 0 credits left, type '!buy <amount>' to buy more");
                    queue.put("Session " + sessionID + " is out of credits.");
                }
            }
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }

    /**
     * Quick and dirty check if string is number
     * @param str String to check
     * @return if string is number or not
     */
    private static boolean isNumeric(String str) {
        try {
            double d = Double.parseDouble(str);
        }
        catch(NumberFormatException e) {
            return false;
        }
        return true;
    }

    private void increaseCredits(int value) {
        credits.put(sessionID, (Integer) credits.get(sessionID) + value);
    }

    private void decreaseCredits(int value) {
        credits.put(sessionID, (Integer) credits.get(sessionID) - value);
    }
}
