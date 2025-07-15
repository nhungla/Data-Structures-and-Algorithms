def sieve_of_era(n, primes):
    primes[0] = primes[1] = False
    i = 2
    while i * i <= n:
        if primes[i]:
            for j in range(2 * i, n + 1, i):
                primes[j] = False
        i += 1


def next_permutation(nums):
    l = len(nums)
    for i in range(l - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            for j in range(l - 1, i, -1):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    tmp = nums[i + 1:]
                    tmp = tmp[::-1]
                    idx = 0
                    for k in range(i + 1, l):
                        nums[k] = tmp[idx]
                        idx += 1
                    return True
    return False


def is_ana_prime(n, primes):
    ans = []
    while n > 0:
        ans.append(n % 10)
        n //= 10
    ans.sort()
    l = len(ans)
    for i in range(l):
        if not ans[i] & 1 or (ans[i] == 5 and l > 1):
            return False
    re = True
    while re or next_permutation(ans):
        re = False
        n = 0
        for i in range(l):
            n = n * 10 + ans[i]
        if not primes[n]:
            return False
    return True


if __name__ == "__main__":
    max_n = 10 ** 7
    primes = [True] * (max_n + 1)
    ana_primes = [2]
    sieve_of_era(max_n, primes)
    for i in range(3, max_n + 1, 2):
        if primes[i] and is_ana_prime(i, primes):
            ana_primes.append(i)
    while True:
        n = int(input())
        if n == 0:
            break
        m = len(ana_primes)
        index = m - 1
        while index >= 0 and ana_primes[index] > n:
            index -= 1
        index += 1
        if (index < m):
            pow10 = 1
            while (n > 0):
                n //= 10
                pow10 *= 10
            print(ana_primes[index] if ana_primes[index] < pow10 else 0)
        else:
            print(0)
