#dfnow = df[df['geo_region'].notnull()]
#dfnow = dfnow[dfnow['geo_region'].str.contains('acific')]
#dfnow.reset_index(inplace=True, drop=True)
#fnamesnow = dfnow['fname'].values

if fname=='00001_short.nc':
    # remove weird day
    masknow = ~((Sv['time'].dt.year==1992) & (Sv['time'].dt.month==11) & (Sv['time'].dt.day==8))
    Sv = Sv.where(masknow,drop=True); Sv_pflag = Sv_pflag.where(masknow,drop=True)
    Sv_pg = Sv_pg.where(masknow,drop=True); Sv_depth = Sv_depth.where(masknow,drop=True)
    Sv_lon = Sv_lon.where(masknow,drop=True); Sv_lat = Sv_lat.where(masknow,drop=True)
    fig,axes = plt.subplots(nrows=1, ncols=3, figsize=(15,4))
    Sv_depth.plot(ax=axes[0],y='depth_cell',yincrease=False)
    
    # remove unnecessary nans at bottom depths now that 1st weird day is gone
    masknow = ~np.isnan(Sv_depth)
    Sv = Sv.where(masknow,drop=True); Sv_pflag = Sv_pflag.where(masknow,drop=True)
    Sv_pg = Sv_pg.where(masknow,drop=True); Sv_depth = Sv_depth.where(masknow,drop=True)
    Sv_depth.plot(ax=axes[1],y='depth_cell',yincrease=False)
    
    # remove another weird day 
    masknow = ~((Sv['time'].dt.year==1992) & (Sv['time'].dt.month==11) & (Sv['time'].dt.day==15))
    Sv = Sv.where(masknow,drop=True); Sv_pflag = Sv_pflag.where(masknow,drop=True)
    Sv_pg = Sv_pg.where(masknow,drop=True); Sv_depth = Sv_depth.where(masknow,drop=True)
    Sv_lon = Sv_lon.where(masknow,drop=True); Sv_lat = Sv_lat.where(masknow,drop=True)
    Sv_depth.plot(ax=axes[2],y='depth_cell',yincrease=False)