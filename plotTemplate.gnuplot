# set terminal pngcairo dashed enhanced
set term png transparent truecolor
set datafile separator ','

# set xrange [0.5:4.5]
# set yrange [0:5]

# viridis
set style line  1 lt 1 lc rgb '#440154' # dark purple
set style line  2 lt 1 lc rgb '#472c7a' # purple
set style line  3 lt 1 lc rgb '#3b518b' # blue
set style line  4 lt 1 lc rgb '#2c718e' # blue
set style line  5 lt 1 lc rgb '#21908d' # blue-green
set style line  6 lt 1 lc rgb '#27ad81' # green
set style line  7 lt 1 lc rgb '#5cc863' # green
set style line  8 lt 1 lc rgb '#aadc32' # lime green
set style line  9 lt 1 lc rgb '#fde725' # yellow

set xdata time
set timefmt "%Y-%m-%d" # specify our time string format
set format x "%d.%m" # otherwise it will show only MM:SS

set output 'graph.png'
plot \
         "data.csv" using 1:2:(0) with filledcurves linestyle 2 title "Views", \
         "data.csv" using 1:4:(0) with filledcurves linestyle 6 title "Clones", \

# plot \
#          "data.csv" using 1:2:(0) with filledcurves linestyle 1 title "Views", \
#          "data.csv" using 1:3:(0) with filledcurves linestyle 2 title "Unique Views", \
#          "data.csv" using 1:4:(0) with filledcurves linestyle 3 title "Clones", \
#          "data.csv" using 1:5:(0) with filledcurves linestyle 4 title "Unique Clones", \


