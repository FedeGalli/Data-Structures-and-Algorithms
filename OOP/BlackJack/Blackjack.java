package OOP.BlackJack;

import java.util.ArrayList;

public class Blackjack {
    private Player dealer;
    private ArrayList<Player> tablePlayers;
    private ArrayList<Float> bets;

    public Blackjack() {
        this.dealer = new Player("Dealer", 0);
        this.tablePlayers = new ArrayList<>();

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
            i++;
        }

        dealer.drawCard(new Card());
        dealer.drawCard(new Card());
        //print dealer first card

        for (Player player : this.tablePlayers) {

            while(!player.isReady()) {
                //user action
                switch(user.input) {
                    case 0:
                        player.drawCard(new Card());
                        break;
                    case 1:
                        break;
                }


                if (isBusted(player)) {
                    tablePlayers.remove(player);
                    dealer.addMoney(bets.get(i));
                }
            }
        }

        //make table draw cards until number 17
        while(dealer.cardsSum() < 17) {
            dealer.drawCard(new Card());
        }

        int dealerNumber = dealer.cardsSum();
        i = 0;

        //cheking in condition
        for (Player player : this.tablePlayers) {

            //win
            if (dealerNumber < player.cardsSum()) {
                player.addMoney(bets.get(i) * 2);
                dealer.addMoney(-bets.get(i));
            }
            //push
            else if (dealerNumber == player.cardsSum()) {
                player.addMoney(bets.get(i));
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
