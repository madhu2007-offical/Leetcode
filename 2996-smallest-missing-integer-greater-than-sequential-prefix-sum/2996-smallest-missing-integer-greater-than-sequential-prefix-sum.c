int missingInteger(int* nums, int numsSize) {
    int sum = nums[0];

    // Find longest sequential prefix
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] == nums[i - 1] + 1) {
            sum += nums[i];
        } else {
            break;
        }
    }

    // Frequency array
    int present[101] = {0};

    for (int i = 0; i < numsSize; i++) {
        present[nums[i]] = 1;
    }

    // Find smallest missing number >= sum
    while (sum <= 100) {
        if (!present[sum]) {
            return sum;
        }
        sum++;
    }

    return sum;
}