class Foo {
private:
    mutex mtx;
    condition_variable cv;
    int order = 1;

public:
    Foo() {
        
    }

    void first(function<void()> printFirst) {
        unique_lock<mutex> lock(mtx);

        printFirst();
        order = 2;

        cv.notify_all();
    }

    void second(function<void()> printSecond) {
        unique_lock<mutex> lock(mtx);

        cv.wait(lock, [this]() {
            return order == 2;
        });

        printSecond();
        order = 3;

        cv.notify_all();
    }

    void third(function<void()> printThird) {
        unique_lock<mutex> lock(mtx);

        cv.wait(lock, [this]() {
            return order == 3;
        });

        printThird();
    }
};