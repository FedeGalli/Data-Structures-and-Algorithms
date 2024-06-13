package OOP.BlackJack;

import java.util.ArrayList;

public class Player {
    private String name;
    private ArrayList<Card> cards;
    private float money;
    private boolean isReady;
    private boolean isBusted;

    public Player(String name, float money) {
        this.name = name;
        this.cards = new ArrayList<>();
        this.money = money;
        this.isReady = false;
        this.isBusted = false;
    }

    public float bet(float amount) {

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

    public void setIsReady(boolean isReady) {
        this.isReady = isReady;
    }

    public void resetProperties() {
        this.cards = new ArrayList<>();
        this.isReady = false;
        this.isBusted = false;
    }

    public int cardsSum() {

        int maxSum = 0;
        boolean elevenCounted = false;
        for (Card card : cards) {

            if (card.getNumber() == 1 && !elevenCounted && maxSum + 11 <= 21) {
                maxSum += 11;
                elevenCounted = true;
            }
            else
                maxSum +=  card.getNumber() > 10 ? 10 : card.getNumber();

            
        }
        return maxSum;
    }

    public String getStringCards() {

        String s = "";
        for (Card card : cards) {
            s += (card.getNumber() > 10 ? 10 : card.getNumber()) + " ";
        }

        s += "sum: " + this.cardsSum();

        return s;
    }

    public boolean isBusted() {
        if (cardsSum() > 21) {
            this.isBusted = true;
            return true;
        }

        return false;
    }

    public boolean getIsBusted() {
        return this.isBusted;
    }

    public boolean hasOnlyOneAce() {
        int counter = 0;
        for (Card card : cards) {
            if (card.getNumber() == 1) {
                counter++;
            }

            if (counter > 1)
                return false;
        }

        if (counter == 1)
            return true;

        return false;
    }
}
