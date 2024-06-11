package OOP.BlackJack;

public class Main {

    public static void main(String[] args) {
        Blackjack game = new Blackjack();

        game.addUserToTable(new Player("Federico", 100));

        game.startRound();
    }


    
}
