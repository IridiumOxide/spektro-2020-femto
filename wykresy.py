from furierowiec import DATASET, Series, Label, plot_stuff

# Rys 1
plot_stuff(
    Series(DATASET.OKE_CCl4, "Delay", "15C"),
    x_label=Label.time,
    y_label=Label.amplitude,
    in_x_min=-1000,
    in_x_max=5000
)

# Rys 2
plot_stuff(
    Series(DATASET.OKE_CCl4, "Delay", "15C"),
    x_label=Label.wavenumber,
    y_label=Label.amplitude,
    in_x_min=100,
    res_x_min=0,
    res_x_max=1000,
    fourierized=True
)

# Rys 3
plot_stuff(
    Series(DATASET.Raman_CCl4, "Wavenumber", "parallel", "parallel"),
    Series(DATASET.Raman_CCl4, "Wavenumber", "perpendicular", "perpendicular"),
    x_label=Label.time,
    y_label=Label.amplitude,
    in_x_min=0,
    in_x_max=1000,
    show_legend=True
)

# Rys 6
plot_stuff(
    Series(DATASET.OKE_CCl4, "Delay", "15C", "CCl4 at 15C"),
    Series(DATASET.OKE_chloroform, "Delay", "15C", "Chloroform at 15C"),
    x_label=Label.time,
    y_label=Label.amplitude,
    in_x_min=-1000.,
    in_x_max=5000.,
    show_legend=True
)

# TODO: cut off Y (1e-4 to 1)
# Rys 7.1
plot_stuff(
    Series(DATASET.OKE_CCl4, "Delay", "15C"),
    x_label=Label.time,
    y_label=Label.amplitude,
    y_scale="log"
)
# Rys 7.2
plot_stuff(
    Series(DATASET.OKE_chloroform, "Delay", "15C"),
    x_label=Label.time,
    y_label=Label.amplitude,
    y_scale="log"
)

# Rys 8
plot_stuff(
    Series(DATASET.OKE_CCl4, "Delay", "15C", "CCl4 at 15C"),
    Series(DATASET.OKE_chloroform, "Delay", "15C", "Chloroform at 15C"),
    x_label=Label.wavenumber,
    y_label=Label.amplitude,
    in_x_min=100.,
    res_x_min=100.,
    res_x_max=1000.,
    fourierized=True,
    show_legend=True
)
