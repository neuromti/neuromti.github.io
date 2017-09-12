
This example demonstrates how to load channel positions from _10-5-Channel_Locs.csd_ into Matlab

see also [SCCN-ChanLocFiles-Repository]https://sccn.ucsd.edu/wiki/Channel_Location_Files)
.csd file (storing the positions in azimuthal angle, polar angle, radial distance, radius, x, y,  z, 
importfile (parses) 
mk_sensors_plane (shifts locations to achieve equidistance on 2D-plane) 
can be found in '.\gists\matlab'


```{matlab}
chan.names  = {'Fp1','Fp2','F7','F3','Fz','F4','F8','FC5','FC1','FC2','FC6','T7','C3','Cz','C4','T8','CP5','CP1','CP2','CP6','P7','P3','Pz','P4','P8','O1','Oz','O2','AF7','AF3','AF4','AF8','F5','F1','F2','F6','FT7','FC3','FC4','FT8','C5','C1','C2','C6','TP7','CP3','CPz','CP4','TP8','P5','P1','P2','P6','PO7','PO3','POz','PO4','PO8', 'FCz'};
chan.which  = 1:length(chan.names);
chan.select = chan.names(chan.which);

importfile('.\gists\10-5-Channel_Locs.csd');
for k=1:length(chan.select)
    for i=1:length(data)
        if strcmpi(chan.select(k),textdata{i})
            X(k)=data(i,4);
            Y(k)=data(i,5);
            Z(k)=data(i,6);
        end
    end
end
X=X';
Y=Y';
Z=Z';
for c=1:3
    if c==1
        for r=1:length(chan.select)
            locs_2D(r,c)=X(r);
        end
    elseif c==2
        for r=1:length(chan.select)
            locs_2D(r,c)=Y(r);
        end
    elseif c==3
        for r=1:length(chan.select)
            locs_2D(r,c)=Z(r);
        end
    end
end    
chan.loc_xyz        = locs_2D;
locs_2D             = mk_sensors_plane(locs_2D);
chan.loc_plot       = locs_2D(:,2:3);
chan.loc_shift      = locs_2D(:,4:5);
close all
```
