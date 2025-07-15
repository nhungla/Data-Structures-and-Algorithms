if __name__ == "__main__":
    n, k = int(input()), int(input())
    if n == 1:
        print(k)
    else:
        end_zero, end_not_zero = 0, k - 1
        for i in range(1, n):
            tmp = end_zero
            end_zero = end_not_zero
            end_not_zero = (end_not_zero + tmp) * (k - 1)
        print(end_zero + end_not_zero)

"""
Với N = 1, thì kết quả chắc chắn là K. Đối với các trường hợp còn lại:

Giả sử, ta có các số biễu diễn dưới dạng cơ số K với chiều dài i. Vậy ta có thể tạo được bao nhiêu số cơ số KK chiều dài i + 1?
Chiều dài tăng thêm 1 có nghĩa là chúng ta cần thêm 1 chữ số nữa (các chữ số bao gồm 0,1,2,...,K - 1) vào các số có độ dài i với cơ số K thỏa mãn yêu cầu đề bài.
Nếu số kết thúc là 0 thì ta có thể thêm một trong (K - 1) số từ 0 đến K - 1K−1, ngược lại thì ta có thể thêm một trong (K - 2) số từ 1 đến K - 1.
Lúc này chúng ta cần dùng 2 mảng một chiều gồm các cặp endNot0 và endWith0 với:

endNot0[i]endNot0[i] là số lượng chữ số chiều dài ii cơ số KK và kết thúc là một số khác 00.
endWith0[i]endWith0[i] là số lượng chữ số chiều dài ii cơ số KK và kết thúc là 00.
Chúng ta có thể thấy số endWith0[i+1]= endNot0[i] vì ta chỉ được thêm 1 số 0 vào sau những số có độ dài i mà chữ số cuối cùng khác 0. Còn endNot0[i+1] = (endNot0[i] + endWith0[i]) * (K-1) vì chúng ta có thể thêm bất kì chữ số khác 0 nào vào sau số có độ dài i đã có được.
Khi đó ta sẽ có được công thức:

endWith0[i] = endNot0[i - 1].
endNot0[i] = (endWith0[i - 1] + endNot0[i - 1]) * (K- 1).
Kết quả cuối cùng thu được là: endNot0[N] + endWith0[N].
"""