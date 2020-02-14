#dfnow = df[df['geo_region'].notnull()]
#dfnow = dfnow[dfnow['geo_region'].str.contains('acific')]
#dfnow.reset_index(inplace=True, drop=True)
#fnamesnow = dfnow['fname'].values

if ifile==0:
    masknow = ~((Sv['time'].dt.year==1992) & (Sv['time'].dt.month==11) & (Sv['time'].dt.day==8))
    Sv = Sv.where(masknow,drop=True); Sv_pflag = Sv_pflag.where(masknow,drop=True)
    Sv_pg = Sv_pg.where(masknow,drop=True); Sv_depth = Sv_depth.where(masknow,drop=True)
    Sv_lon = Sv_lon.where(masknow,drop=True); Sv_lat = Sv_lat.where(masknow,drop=True)
    fig = plt.figure(figsize=(4,4))
    Sv_depth.plot()
    
    masknow = ~np.isnan(Sv_depth)
    Sv = Sv.where(masknow,drop=True); Sv_pflag = Sv_pflag.where(masknow,drop=True)
    Sv_pg = Sv_pg.where(masknow,drop=True); Sv_depth = Sv_depth.where(masknow,drop=True)
    fig = plt.figure(figsize=(4,4))
    Sv_depth.plot()
    
    masknow = ~((Sv['time'].dt.year==1992) & (Sv['time'].dt.month==11) & (Sv['time'].dt.day==15))
    Sv = Sv.where(masknow,drop=True); Sv_pflag = Sv_pflag.where(masknow,drop=True)
    Sv_pg = Sv_pg.where(masknow,drop=True); Sv_depth = Sv_depth.where(masknow,drop=True)
    Sv_lon = Sv_lon.where(masknow,drop=True); Sv_lat = Sv_lat.where(masknow,drop=True)
    fig = plt.figure(figsize=(4,4))
    Sv_depth.plot()
    
else:
    pass