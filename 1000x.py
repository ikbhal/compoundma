
def thousand_times():
    print("1000x")

    capital =10000 # 10k  -> 1000x -> 1 cr
    years = 10
    for i in range(0, 10001, 100):
        base  = round(100 + i /10,2)/100
        base = round(base, 2)
        result = pow(base , years)
        result = round(result, 2)

        print(f" i {i} base {base} years {years} result {result}")


if __name__ == '__main__':
    # make 1000x
    # search 1000x
    # distribute 1000x
    # teach 1000x
    thousand_times()