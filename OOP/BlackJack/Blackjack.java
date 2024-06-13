package OOP.BlackJack;

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
        i = 0;
        for (Player player : this.tablePlayers) {
            while (!player.isReady()) {
                //System.out.println("0 to draw a card \n1 to stay");

                if (player.cardsSum() < 13 || player.hasOnlyOneAce()) {
                    player.drawCard(new Card());

                    if (player.isBusted()) {
                        dealer.addMoney(bets.get(i));
                        player.setIsReady(true);
                        //System.out.println(player.getName() + " You lost " + bets.get(i));
                    }
                } else
                    player.setIsReady(true);
            }

            i++;
        }

        // make table draw cards until number 17
        while (dealer.cardsSum() < 17) {
            dealer.drawCard(new Card());
            //System.out.println("Dealer cards: " + dealer.getStringCards());
        }

        int dealerNumber = dealer.cardsSum();

        i = 0;

        // cheking in condition
        for (Player player : this.tablePlayers) {

            if (!player.getIsBusted()) {
                // win
                if (dealerNumber < player.cardsSum() || dealerNumber > 21) {
                    player.addMoney(bets.get(i) * 2);
                    dealer.addMoney(-bets.get(i));

                    //System.out.println(player.getName() + " You won " + bets.get(i) * 2);
                }
                // push
                else if (dealerNumber == player.cardsSum()) {
                    player.addMoney(bets.get(i));

                    //System.out.println(player.getName() + " Push");
                } else {
                    //System.out.println(player.getName() + " You lost " + bets.get(i));
                    dealer.addMoney(bets.get(i));
                }
            }
            System.out.println("P" + i + " money: " + player.getMoney());
            i++;
            player.resetProperties();
        }
        dealer.resetProperties();
        System.out.println("DEALER money: " + dealer.getMoney());

    }

}
