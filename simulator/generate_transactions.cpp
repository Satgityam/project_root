#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
    ofstream file("../data/transactions.csv");
    if (!file.is_open()) {
        cerr << "Failed to create transactions.csv. Ensure the ../data/ folder exists." << endl;
        return 1;
    }

    // Write CSV header
    file << "user_id,amount,device_id,hour,merchant_id,device_change\n";

    srand(time(0));  // Seed for randomness

    // Generate 1000 fake transactions
    for (int i = 0; i < 1000; ++i) {
        int user_id = rand() % 100;               // 0-99
        float amount = static_cast<float>(rand() % 20000) / 2.0f + 1; // up to ~10000
        int device_id = rand() % 50;              // 0-49
        int hour = rand() % 24;                   // 0-23
        int merchant_id = rand() % 30;            // 0-29
        int device_change = rand() % 2;           // 0 or 1

        file << user_id << ","
             << amount << ","
             << device_id << ","
             << hour << ","
             << merchant_id << ","
             << device_change << "\n";
    }

    file.close();
    cout << "✅ transactions.csv generated successfully in /data folder.\n";
    return 0;
}
