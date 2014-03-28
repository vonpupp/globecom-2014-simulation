# These variables are used within both scripts with relative paths references!

trace_scenarios = [
    'hybrid1',
    'hybrid2',
    'hybrid3',
    'hybrid4',
    'hybrid5',
    'hybrid6',
    'hybrid7',
#    '../planetlab-workload-traces/20110409/146-179_surfsnel_dsl_internl_net_root',
#    '../planetlab-workload-traces/20110409/host4-plb_loria_fr_uw_oneswarm',
#    '../planetlab-workload-traces/20110420/plgmu4_ite_gmu_edu_rnp_dcc_ufjf',

#    '../planetlab-workload-traces/20110309/planetlab1_fct_ualg_pt_root',
#    '../planetlab-workload-traces/20110325/host3-plb_loria_fr_inria_omftest',
#    '../planetlab-workload-traces/20110412/planetlab1_georgetown_edu_nus_proxaudio',

#    '../planetlab-workload-traces/20110306/planetlab1_dojima_wide_ad_jp_princeton_contdist',
#    '../planetlab-workload-traces/planetlab-selected/planetlab-20110409-filtered_planetlab1_s3_kth_se_sics_peerialism',
#    '../planetlab-workload-traces/20110322/planetlab-wifi-01_ipv6_lip6_fr_inria_omftest'
]

algorithm_scenarios = [
    'EnergyUnawareStrategyPlacement',
    'OpenOptStrategyPlacement',
    'EvolutionaryComputationStrategyPlacement',
    'OpenOptStrategyPlacementMem',
    'EvolutionaryComputationStrategyPlacementCPU',
]

# Setup the scenarios
host_scenarios = range(10, 110, 10)
simulation_scenarios = range(1, 31)
#simulation_scenarios = range(1, 2)
vms_start = 16
vms_stop = 288
vms_step = 16
