import pstats

stats = pstats.Stats("prof.out")

stats.sort_stats("tottime")

stats.print_stats(10)
