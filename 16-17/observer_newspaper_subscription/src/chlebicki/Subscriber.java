package chlebicki;

import chlebicki.interfaces.Observer;
import chlebicki.Newspaper;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by Dominik on 19.03.2017.
 */
public class Subscriber implements Observer {

    private String name;

    public Subscriber(String name){
        this.name = name;
    }

    @Override
    public void update(String source, String headline, String content) {
        System.out.println(name + " hat eine neue Benachrichtigung von " + source + ":");
        System.out.println("--- " + headline + " ---");
        System.out.println(content + "\n");
    }
}
