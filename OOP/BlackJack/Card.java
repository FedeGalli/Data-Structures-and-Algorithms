package OOP.BlackJack;

import java.util.Random;

public class Card {
    private int number;
    public enum Seed {CLUBS, SPADES, DIAMONDS, HEARTS};
    private Seed seed;

    public Card(int number, Seed seed) {
        this.number = number;
        this.seed = seed;
    }

    public Card() {
        Random rand = new Random();
        this.number = rand.nextInt(14);
        
        switch(rand.nextInt(4)) {
            case 0:
                this.seed = Seed.CLUBS;
                break;
            case 1:
                this.seed = Seed.HEARTS;
                break;
            case 2:
                this.seed = Seed.DIAMONDS;
                break;
            case 3:
                this.seed = Seed.SPADES;
                break;
        }
    }

    public int getNumber() {
        return this.number;
    }

    public Seed getSeed() {
        return this.seed;
    }
}
