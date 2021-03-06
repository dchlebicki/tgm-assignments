package main.java.servlet;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.sql.rowset.serial.SerialException;
import java.io.IOException;
import java.io.PrintWriter;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;


/**
 * Created by Dominik on 29.05.2017.
 */

public class Servlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    static PrintWriter out;

    /**
     * @see HttpServlet#doGet(javax.servlet.http.HttpServletRequest request,
     *          javax.servlet.http.HttpServletResponse response)
     */
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        out = response.getWriter();
        //out.print(output);
        request.getRequestDispatcher("jsp/index.jsp").forward(request, response);
    }

    public static String getDate(){
        DateFormat dateFormat = new SimpleDateFormat("dd.MM.yyyy");
        Date date = new Date();
        return dateFormat.format(date);
    }

    public static String getTime(){
        //DateFormat dateFormat = new SimpleDateFormat("HH:mm:ss");
        DateFormat dateFormat = new SimpleDateFormat("HH:mm");
        Date date = new Date();
        return dateFormat.format(date);
    }

    public static String getMessage() {
        DateFormat dateFormat = new SimpleDateFormat("HH");
        Date date = new Date();
        int hours = Integer.parseInt(dateFormat.format(date));
        if((hours >= 22) || (hours < 6)){
            return "Gute Nacht!";
        } else if((hours >= 6) && (hours < 10)){
            return "Guten Morgen!";
        } else if((hours >= 10) && (hours < 14)){
            return "Guten Mittag!";
        } else if((hours >= 14) && (hours < 18)){
            return "Guten Nachmittag!";
        } else if((hours >= 18) && (hours < 22)){
            return "Guten Abend!";
        } else {
            return "Wie geht's?";
        }
    }
}
