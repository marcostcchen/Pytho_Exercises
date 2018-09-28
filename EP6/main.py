import time
from percolation_stats import PercolationStats


def main():
    '''(None) -> None
    '''
    n = int(input("Digite a dimensão da grade: "))
    T = int(input("Digite o número de experimentos: "))

    # ----------------------------------------------
    inicio = time.time()
    exps = PercolationStats(n, T);
    mean = exps.mean()
    stddev = exps.stddev()
    confidenceLow = exps.confidenceLow()
    confidenceHigh = exps.confidenceHigh()
    fim = time.time()
    # ---------------------------------------------

    # relatorio
    print("mean()           = %f" % mean)
    print("stddev()         = %f" % stddev)
    print("confidenceLow()  = %f" % confidenceLow)
    print("confidenceHigh() = %f" % confidenceHigh)
    print("elapsed time     = %.3fs" % (fim - inicio))


# --------------------------------------------------
if __name__ == '__main__':
    main()