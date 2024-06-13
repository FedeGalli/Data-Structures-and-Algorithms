package OOP.BlackJack;

public class Main {

    public static void main(String[] args) {
        Blackjack game = new Blackjack();

        game.addUserToTable(new Player("Federico", 50000));
        game.addUserToTable(new Player("Andrea", 50000));
        game.addUserToTable(new Player("Gianluca", 50000));

        int i = 0;
        while (i < 30000) {
            game.startRound();
            i++;
        }

    }


    
}
