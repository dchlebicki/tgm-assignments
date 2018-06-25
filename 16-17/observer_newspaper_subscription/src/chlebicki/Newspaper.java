package chlebicki;

import chlebicki.interfaces.Observer;
import chlebicki.interfaces.Subject;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by Dominik on 19.03.2017.
 */
public class Newspaper implements Subject {

    private List<Subscriber> subscribers = new ArrayList<>();
    private String name;
    private String currentHeadline = "";
    private String currentContent = "";

    public Newspaper(String name) {
        this.name = name;
    }

    @Override
    public void registerObserver(Subscriber subscriber) {
        subscribers.add(subscriber);
        subscriber.update(name, currentHeadline, currentContent);
    }

    @Override
    public void removeObserver(Subscriber subscriber) {
        subscribers.remove(subscriber);
    }

    @Override
    public void notifyObserver() {
        for (Subscriber subscriber : subscribers) {
            subscriber.update(name, currentHeadline, currentContent);
        }
    }

    public void setCurrentNews(String headline, String content){
        this.currentHeadline = headline;
        this.currentContent = content;
        notifyObserver();
    }

    public String getCurrentHeadline(){
        return currentHeadline;
    }

    public String getCurrentContent() {
        return currentContent;
    }

    public String getName() {
        return name;
    }
}
