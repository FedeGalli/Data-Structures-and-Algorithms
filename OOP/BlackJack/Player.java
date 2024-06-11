package OOP.BlackJack;

import java.util.ArrayList;

public class Player {
    private String name;
    private ArrayList<Card> cards;
    private float money;
    private boolean isReady;

    public Player(String name, float money) {
        this.name = name;
        this.cards = new ArrayList<>();
        this.money = money;
        this.isReady = false;
    }

    public float bet(float amount) {

        if (money - amount < 0) {
            return -1;
        }

        this.money = money - amount;
        return amount;
    }

    public void drawCard(Card card) {
        cards.add(card);
    }

    public String getName() {
        return name;
    }

    public ArrayList<Card> getCards() {
        return cards;
    }

    public float getMoney() {
        return money;
    }

    public void addMoney(float amount) {
        this.money += amount;
    }

    public boolean isReady() {
        return isReady;
    }

    public void resetProperties() {
        this.cards = new ArrayList<>();
        this.isReady = false;
    }

    public int cardsSum() {

        int maxSum = 0;
        boolean elevenCounted = false;
        for (Card card : cards) {

            if (card.getNumber() == 1 && !elevenCounted) {
                maxSum += 11;
                elevenCounted = true;
            }
            else
                maxSum +=  card.getNumber() > 10 ? 10 : card.getNumber();

            
        }
        return maxSum;
    }
}
