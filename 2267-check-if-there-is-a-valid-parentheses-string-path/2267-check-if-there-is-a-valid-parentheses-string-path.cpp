const unsigned long long C = 1ull << 63;
struct Bitbuf {
    unsigned long long data[2];

    void set(int x) {
        if( x<64 ) {
            data[0] |= 1 << x;
        } else {
            data[1] |= 1 << (x-64);
        }
    }

    void setzero() {
        data[0] |= 1;
    }

    void merge(Bitbuf const& other) {
        data[0] |= other.data[0];
        data[1] |= other.data[1];
    }

    void copy(Bitbuf const& other) {
        data[0] = other.data[0];
        data[1] = other.data[1];
    }

    void copy_and_shift(Bitbuf const& other, int dir) {
        copy(other);
        shift(dir);
    }

    void init() {
        data[0] = 1ull;
        data[1] = 0ull;
    }

    
    void inc() {
        data[1] <<= 1ull;
        if( (data[0]&C)==C ) {
            data[1] |= 1ull;
        }
        data[0] <<= 1ull;
    }

    void dec() {
        data[0] >>= 1ull;
        if( (data[1]&1ull)==1ull ) {
            data[0] |= C;
        }
        data[1] >>= 1ull;
    }

    void shift(int d) {
        if( d>0 ) {
            inc();
        } else {
            dec();
        }
    }

    bool contains_zero() {
        return (data[0]&1ull)==1ull;
    }

};

class Solution {
public:
    bool hasValidPath(vector<vector<char>>& grid) {
        const int R=grid.size(), C=grid[0].size();
        vector<vector<Bitbuf>> buf(2, vector<Bitbuf>(C));
        auto val = [&](int r, int c) {
            switch (grid[r][c]) {
                case '(': return 1;
                default: return -1;
            }
        };
        if( grid[0][0]==')' || grid.back().back()=='(' ) {
            return false;
        }
        buf[0][0].init();
        buf[0][0].shift(val(0, 0));

        for( int c=1;c<C;++c ) {
            buf[0][c].copy_and_shift(buf[0][c-1], val(0, c));
            
        }
        for( int r=1;r<R;++r ) {
            int curr = r%2;
            int pref = (r+1)%2;
            buf[curr][0].copy_and_shift(buf[pref][0], val(r, 0));
            for( int c=1;c<C;++c ) {
                buf[curr][c].copy(buf[curr][c-1]);
                buf[curr][c].merge(buf[pref][c]);
                buf[curr][c].shift(val(r, c));
            }
        }
        
        return buf[(grid.size()+1)%2].back().contains_zero();
    }
};