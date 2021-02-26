import pandas as pd

df_bat = pd.read_csv('war_bat.csv')
df_pitch = pd.read_csv('war_pitch.csv')

df_bat = df_bat[df_bat.pitcher == 'N']
df_bat = df_bat[df_bat.year_ID >= 1995]
df_pitch = df_pitch[df_pitch.year_ID >= 1995]
df_pitch.IPouts = df_pitch.IPouts / 3
df_pitch.rename(columns = {'IPouts':'IP'}, inplace = True)

df_bat = df_bat.drop(columns=['mlb_ID', 'Inn', 'runs_bat', 'runs_br', 'runs_dp',
       'runs_field', 'runs_infield', 'runs_outfield', 'runs_catcher', 'stint_ID',
       'runs_good_plays', 'runs_defense', 'runs_position', 'runs_position_p',
       'runs_replacement', 'runs_above_rep', 'runs_above_avg',
       'runs_above_avg_off', 'runs_above_avg_def', 'WAA', 'WAA_off', 'WAA_def',
       'WAR_def', 'WAR_off', 'WAR_rep', 'teamRpG', 'pitcher',
       'oppRpG', 'oppRpPA_rep', 'oppRpG_rep', 'pyth_exponent',
       'pyth_exponent_rep', 'waa_win_perc', 'waa_win_perc_off',
       'waa_win_perc_def', 'waa_win_perc_rep', 'OPS_plus', 'TOB_lg', 'TB_lg'])
df_pitch = df_pitch.drop(columns=['mlb_ID',
       'stint_ID', 'IPouts_start',
       'IPouts_relief', 'RA', 'xRA', 'xRA_sprp_adj', 'xRA_extras_adj',
       'xRA_def_pitcher', 'PPF', 'PPF_custom', 'xRA_final', 'BIP', 'BIP_perc',
       'RS_def_total', 'runs_above_avg', 'runs_above_avg_adj',
       'runs_above_rep', 'RpO_replacement', 'GR_leverage_index_avg',
       'teamRpG', 'oppRpG', 'pyth_exponent', 'waa_win_perc', 'WAA',
       'WAA_adj', 'oppRpG_rep', 'pyth_exponent_rep', 'waa_win_perc_rep',
       'WAR_rep', 'ERA_plus', 'ER_lg'])

df_bat.to_csv('batter.csv', index=None)
df_pitch.to_csv('pitcher.csv', index=None)