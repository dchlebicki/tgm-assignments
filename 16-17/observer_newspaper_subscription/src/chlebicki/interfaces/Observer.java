package chlebicki.interfaces;

/**
 * Abstract observer of the observer design pattern
 *
 * In this case, the subscriber class will later implement this class.
 */
public interface Observer {

    /**
     * Updates the data
     */
    void update(String newspaper, String headline, String content);
}
