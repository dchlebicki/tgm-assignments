package Server;

import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.concurrent.BlockingQueue;

/**
 * Created by Dominik on 12.02.2018.
 */
public class Logger implements Runnable {

    private BlockingQueue queue;
    private String filename;

    public Logger(BlockingQueue queue, String filename) {
        this.queue = queue;
        this.filename = filename;
    }

    @Override
    public void run() {
        String output;

        try ( PrintWriter printWriter = new PrintWriter(this.filename) ) {

            while (true) {
                if (!queue.isEmpty()) {
                    output = queue.take().toString();
                    System.out.println(output);
                    printWriter.println(output);
                    printWriter.flush();
                }
            }

        } catch (FileNotFoundException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
