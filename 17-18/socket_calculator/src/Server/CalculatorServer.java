package Server;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Collection;
import java.util.Iterator;
import java.util.List;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.TimeUnit;

/**
 * Created by Dominik on 02.02.2018.
 */
public class CalculatorServer {

    private BlockingQueue queue;
    private int port;
    //<sessionID, thread>
    private ConcurrentHashMap<Integer, Thread> threads;
    //<sessionID, credits>
    private ConcurrentHashMap<Integer, Integer> credits;

    public CalculatorServer(int portnumber) {
        this.port = portnumber;
        this.queue = new ArrayBlockingQueue(1024);
        this.threads = new ConcurrentHashMap<>();
        this.credits = new ConcurrentHashMap<>();
    }

    public void start() {
        int sessionID = 1;

        Thread logger = new Thread(new Logger(queue, "log.txt"));
        logger.start();
        try (
            //create serversocket with portnumber
            ServerSocket serverSocket = new ServerSocket(this.port);
        ) {
            while (true) {

                //wait until client connects and accept message
                Socket clientSocket = serverSocket.accept();

                credits.put(sessionID, 10);
                Thread temp = new Thread(new CalculatorSession(clientSocket, queue, credits, sessionID));
                temp.start();
                threads.put(sessionID, temp);

                sessionID++;
            }
        } catch(IOException e){
            e.printStackTrace();
        }

    }

    public static void main(String[] args) {
        CalculatorServer cs = new CalculatorServer(50000);
        cs.start();
    }
}