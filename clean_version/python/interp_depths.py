# use after running remove_depth_nans_bad_depth_days.py

# - this plot has inconsistent depth values
fig,ax = plt.subplots(nrows=1, ncols=1, figsize=(22,4))
pc = ax.pcolormesh(Sv['time'].broadcast_like(Sv_depth).values, Sv_depth.values, Sv.where((Sv_pflag==0) & (Sv_pg>pg_thresh)), vmax=0)
ax.set_ylim([Sv_depth.max(),0])
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d:%H')); ax.set_xlabel('')
ax.set_title('BEFORE interp depths / ' + str(ifile) + ' / ' + fname + ' / ' + str(row['cruise_beg_date'].year) + ' / ' + row['geo_region'] + ' / LOCAL SOLAR TIME' );
fig.colorbar(pc, ax=ax, orientation='vertical', pad=0.01);

uniq_depths, ud_idx = np.unique(Sv_depth.values, axis=0, return_inverse=True)
for uniqdepthsnum in np.unique(ud_idx):
    print('num of depths type',uniqdepthsnum,':',np.sum(ud_idx==uniqdepthsnum))
    
if len(uniq_depths)>1:
    most_freq_udidx = np.bincount(ud_idx).argmax()
    uud_idx = np.unique(ud_idx)
    uud_idx = uud_idx[uud_idx!=most_freq_udidx]
    for ud_num in uud_idx:
        old_depth_tidxs = np.argwhere(ud_idx==ud_num)
        old_depth = uniq_depths[ud_num]
        new_depth = uniq_depths[most_freq_udidx]
        good_idxs = np.where(~((new_depth>old_depth.max()) | (new_depth<old_depth.min())))
        for tidx in old_depth_tidxs:
            old_Sv = Sv.isel(time=tidx)
            f = interp1d(old_depth, old_Sv)
            new_Sv = np.array([None]*len(new_depth))
            new_Sv[good_idxs] = f(new_depth[good_idxs])
            new_Sv = new_Sv.astype(float)
            Sv.loc[dict(time=Sv['time'][tidx])] = new_Sv
            Sv_depth.loc[dict(time=Sv['time'][tidx])] = new_depth
            
    uniq_depths, ud_idx = np.unique(Sv_depth.values, axis=0, return_inverse=True)
    for uniqdepthsnum in np.unique(ud_idx):
        print('(AFTER INTERP DEPTH STDIZATION) num of depths new type',uniqdepthsnum,':',np.sum(ud_idx==uniqdepthsnum))