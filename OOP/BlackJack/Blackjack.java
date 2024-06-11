package OOP.BlackJack;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Blackjack {
    private Player dealer;
    private ArrayList<Player> tablePlayers;
    private ArrayList<Float> bets;

    public Blackjack() {
        this.dealer = new Player("Dealer", 0);
        this.tablePlayers = new ArrayList<>();
        this.bets = new ArrayList<>();

    }

    public void addUserToTable(Player player) {
        this.tablePlayers.add(player);

    }

    public void startRound() {
        int i = 0;
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        // initial phase
        for (Player player : this.tablePlayers) {
            // placing bets
            float betAmount = 5;
            player.bet(betAmount);
            bets.add(betAmount);

            // drawing standard cards
            player.drawCard(new Card());
            player.drawCard(new Card());
            System.out.println(player.getName() + " cards: " + player.getStringCards());
            i++;
        }

        dealer.drawCard(new Card());
        dealer.drawCard(new Card());
        System.out.println("Dealer cards: " + dealer.getStringCards());

        // print dealer first card

        for (Player player : this.tablePlayers) {

            while (!player.isReady()) {
                String userInput;
                int userChoice;
                try {
                    System.out.println("0 to draw a card \n1 to stay");
                    userInput = reader.readLine();
                    userChoice = Integer.parseInt(userInput);

                    // user action
                    switch (userChoice) {
                        case 0:
                            player.drawCard(new Card());
                            System.out.println(player.getName() + " cards: " + player.getStringCards());

                            if (isBusted(player)) {
                                tablePlayers.remove(player);
                                dealer.addMoney(bets.get(i));
                                System.out.println(player.getName() + " You lost " + bets.get(i));
                            }
                            break;
                        case 1:
                            player.setIsReady(true);
                            break;
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }

        // make table draw cards until number 17
        while (dealer.cardsSum() < 17) {
            dealer.drawCard(new Card());
            System.out.println("Dealer cards: " + dealer.getStringCards());
        }


        int dealerNumber = dealer.cardsSum();

        i = 0;

        // cheking in condition
        for (Player player : this.tablePlayers) {

            // win
            if (dealerNumber < player.cardsSum() || dealerNumber > 21) {
                player.addMoney(bets.get(i) * 2);
                dealer.addMoney(-bets.get(i));

                System.out.println(player.getName() + " You won " + bets.get(i) * 2);
            }
            // push
            else if (dealerNumber == player.cardsSum()) {
                player.addMoney(bets.get(i));

                System.out.println(player.getName() + " Push");
            }
            else {
                System.out.println(player.getName() + " You lost " + bets.get(i));
                dealer.addMoney(bets.get(i));
            }

            i++;
        }

    }

    private boolean isBusted(Player player) {
        if (player.cardsSum() > 21)
            return true;

        return false;
    }
}
