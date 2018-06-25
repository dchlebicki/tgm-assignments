package chlebicki;

/**
 * Created by Dominik on 19.03.2017.
 */
public class Main {
    public static void main(String[] args) {
        Subscriber johndoe = new Subscriber("John Doe");
        Subscriber johnsmith = new Subscriber("John Smith");
        Subscriber johncena = new Subscriber("John Cena");

        Newspaper buzzfeed = new Newspaper("Buzzfeed");
        Newspaper realnews = new Newspaper("Real News Magazine");
        Newspaper fakenews = new Newspaper("The Fake Journal");

        buzzfeed.setCurrentNews("10 things only 90's kids remember, you won't belive #7!", "insert uninteresting content here");
        realnews.setCurrentNews("Will robots steal your job?", "This robot builds new programs by itself!!!");
        fakenews.setCurrentNews("NASA gibt zu dass Erde flach ist", "ich hab ja gesagt dass sie flach ist!!!");

        buzzfeed.registerObserver(johndoe);
        buzzfeed.registerObserver(johnsmith);

        realnews.registerObserver(johndoe);
        realnews.registerObserver(johnsmith);
        realnews.registerObserver(johncena);

        fakenews.registerObserver(johndoe);

        try {
            Thread.sleep(1000);
        } catch(InterruptedException ex) {
            Thread.currentThread().interrupt();
        }

        System.out.println(">> Neuer Artikel bei Buzzfeed\n");
        buzzfeed.setCurrentNews("Another clickbait article", "gotta get that sweet ad money somehow");

        try {
            Thread.sleep(1000);
        } catch(InterruptedException ex) {
            Thread.currentThread().interrupt();
        }

        System.out.println(">> John Doe und John Smith von Real News deabonnieren");
        realnews.removeObserver(johndoe);
        realnews.removeObserver(johnsmith);

        System.out.println(">> Neuer Artikel bei Real News\n");
        realnews.setCurrentNews("Fish need water", "scientists found that out today");

        try {
            Thread.sleep(1000);
        } catch(InterruptedException ex) {
            Thread.currentThread().interrupt();
        }

        System.out.println(">> John Cena abonniert Fake News\n");
        fakenews.registerObserver(johncena);



    }
}
