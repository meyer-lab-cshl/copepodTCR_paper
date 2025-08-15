import pandas as pd
import copepodTCR as cpp
import codepub as cdp

length = 2000
sequence = cpp.random_amino_acid_sequence(length)
lst_all = []
for i in range(0, len(sequence), 5):
    ps = sequence[i:i+17]
    if len(ps) == 17:
        lst_all.append(ps)

n_pools = 18
iters = 6
simulation_results_fixN18_fixI6 = pd.DataFrame(columns = ['Peptide', 'Address', 'Epitope', 'Act Pools',
                                        '# of pools', '# of epitopes', '# of peptides', 'Remained', '# of lost',
                                           'Right peptide', 'Right epitope', 'Len'])

for i in tqdm.tqdm(range(100, 400, 100)):

    b, lines = cdp.bba(m=n_pools, r=iters, n=i)
    lst = lst_all[:i]
    pools, peptide_address = cpp.pooling(lst=lst, addresses=lines, n_pools=n_pools)
    check_results = cpp.run_experiment(lst=lst, peptide_address=peptide_address, ep_length=8,
                              pools=pools, iters=iters, n_pools=n_pools, regime='with dropouts')
    check_results['Len'] = i
    simulation_results_fixN18_fixI6 = pd.concat([simulation_results_fixN18_fixI6, check_results])