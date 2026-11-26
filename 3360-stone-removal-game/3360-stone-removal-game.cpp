class Solution {
public:
    bool canAliceWin(int n) {
        int stones_to_remove = 10;
        bool is_alice_turn = true;
        
        while (n >= stones_to_remove) {
            n -= stones_to_remove;
            stones_to_remove--;
            is_alice_turn = !is_alice_turn;
        }
        
        return !is_alice_turn;
    }
};