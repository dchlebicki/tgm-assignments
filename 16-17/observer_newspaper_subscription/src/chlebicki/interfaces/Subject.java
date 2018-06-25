package chlebicki.interfaces;

import chlebicki.Subscriber;

/**
 * Abstract subject part of the observer design pattern
 *
 * In this case, the newspaper class will later implement this class.
 */
public interface Subject {
    /**
     * registers an observer
     *
     * @param subscriber the observer to register
     */
    void registerObserver(Subscriber subscriber);
    /**
     * removes an observer
     *
     * @param subscriber the observer to remove
     */
    void removeObserver(Subscriber subscriber);

    /**
     * notifies the observers
     */
    void notifyObserver();
}
