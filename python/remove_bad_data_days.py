# use after running remove_depth_nans_bad_depth_days.py
# and interp_depths.py

if fname=='00001_short.nc':
    #masknow1 = ~((Sv['time'].dt.year==1992) & (Sv['time'].dt.month==11) & (Sv['time'].dt.day==15))
    #masknow2 = ~((Sv['time'].dt.year==1992) & (Sv['time'].dt.month==12) & (Sv['time'].dt.day==5))
    #masknow = masknow1 | masknow2
    # - actually, 11/15 was already removed, so just remove 12/5
    masknow = ~((Sv['time'].dt.year==1992) & (Sv['time'].dt.month==12) & (Sv['time'].dt.day==5))
    Sv = Sv.where(masknow,drop=True); Sv_pflag = Sv_pflag.where(masknow,drop=True)
    Sv_pg = Sv_pg.where(masknow,drop=True); Sv_depth = Sv_depth.where(masknow,drop=True)
    Sv_lon = Sv_lon.where(masknow,drop=True); Sv_lat = Sv_lat.where(masknow,drop=True)