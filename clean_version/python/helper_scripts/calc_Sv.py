mask = (~np.isnan(nc['lon'])) & (~np.isnan(nc['lat']))
Sv_lon = nc['lon'].where(mask, drop=True)
Sv_lon[Sv_lon<0] = Sv_lon[Sv_lon<0] + 360
Sv_lat = nc['lat'].where(mask, drop=True)
Sv_depth = nc['depth'].where(mask, drop=True)
Sv_pflag = nc['pflag'].where(mask, drop=True)
Sv_pg = nc['pg'].where(mask, drop=True)
amp = nc['amp'].where(mask, drop=True)
Tx = nc['tr_temp'].where(mask, drop=True)

row = df[df['fname']==fname].iloc[0]

# -->ASSUMPTION FOR NOW:
# If there's no bandwidth for a file,
# say that it's narrowband
if row['bandwidth']==None:
    row['bandwidth']='narrowband'

Er = get_Er_constant(row,amp)
#print('Er: ',Er)

if 'NB' not in row['instrument_name']:
    Kc = get_Kc_constant(row)
elif 'NB' in row['instrument_name']:
    Kc = get_Kc_tdresolved(row,amp,Tx)
#print('Kc: ',Kc)

LDBM = get_LDBM_constant(row)
#print('LDBM: ',LDBM)

if 'NB' not in row['instrument_name']:
    PDBW = get_PDBW_constant(row)
elif 'NB' in row['instrument_name']:
    #PDBW = get_PDBW_tdresolved(row)
    PDBW = get_PDBW_constant(row)
#print('PDBW: ',PDBW)

R = get_R_tdresolved(row, Sv_depth, method_num=5)
#print('R: ',R)

c = calc_c_tdresolved(Sv_depth,T=25,S=35)
#print('c: ',c)

if 'NB' not in row['instrument_name']:
    C = get_C_constant(row)
elif 'NB' in row['instrument_name']:
    C = get_C_tdresolved(row,c)
#print('C: ',C)

# -->ASSUMPTION FOR NOW:
# temp = 25C, sal = 35psu, pH = 8.1
Tnow = Sv_depth.copy(deep=True)
Tnow.name = 'temperature'
Tnow[:,:] = 25
alpha = calc_alpha_tdresolved(row,Sv_depth,c,Tnow,S=35,pH=8.1)
#print('alpha: ',alpha)

alphaR = calc_alphaR_tdresolved(alpha,R)
#print('alphaR: ',alphaR)

Sv = C + 10*np.log10((Tx+273.16)*R**2) - LDBM + PDBW \
    + 2*alphaR + 10*np.log10(10**(Kc*(amp-Er)/10) - 1)